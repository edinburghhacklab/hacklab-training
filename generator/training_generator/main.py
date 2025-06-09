#!/usr/bin/env python3

from datetime import datetime, timezone
import jinja2
import os
import subprocess
from syllabus_processor import SyllabusProcessor
import sys
from tempfile import NamedTemporaryFile
from dataclasses import dataclass, field

SYLLABUS_FILENAME = "syllabus.md"

syllabuses = {}


@dataclass
class Syllabus:
    name: str
    version: str
    commit_date: datetime
    files: dict[str, str] = field(default_factory=dict)


def add_syllabus(result, relpath, output_dir):
    folders = splitpath(relpath)
    dest = os.path.join(output_dir, relpath)
    os.makedirs(dest, exist_ok=True)

    name = folders[-1]
    files = {}

    training_card_filename = "{}-training-card.pdf".format(
        folders[-1].replace(" ", "-")
    )
    files[name + " training card"] = os.path.join(relpath, training_card_filename)
    compile_tex(result.card, os.path.join(dest, training_card_filename))

    training_doc_filename = "{}-training-doc.pdf".format(folders[-1].replace(" ", "-"))
    files[name + " training doc"] = os.path.join(relpath, training_doc_filename)
    compile_tex(result.doc, os.path.join(dest, training_doc_filename))

    if result.risk_assessment is not None:
        risk_assessment_filename = "{}-risk-assessment.pdf".format(
            folders[-1].replace(" ", "-")
        )
        files[name + " risk assessment"] = os.path.join(
            relpath, risk_assessment_filename
        )
        compile_tex(
            result.risk_assessment, os.path.join(dest, risk_assessment_filename)
        )

    version = result.version
    commit_date = result.commit_date

    nested_set(syllabuses, folders, Syllabus(name, version, commit_date, files))


def compile_tex(tex_string, destination_filename):
    with NamedTemporaryFile("w", encoding="utf-8") as f:
        f.write(tex_string)
        f.flush()
        for i in range(5):
            try:
                output = subprocess.check_output(
                    [
                        "pdflatex",
                        "-interaction=nonstopmode",
                        "-output-directory=" + os.path.dirname(destination_filename),
                        "-jobname="
                        + os.path.splitext(os.path.basename(destination_filename))[0],
                        f.name,
                    ],
                    timeout=5,
                )
            except subprocess.CalledProcessError as e:
                print(e.output.decode())
                raise
            if "Rerun LaTeX" not in str(output):
                break


def generate(syallabus_dir, output_dir):
    for root, dirs, files in os.walk(syallabus_dir):
        relpath = os.path.relpath(root, syallabus_dir)
        if SYLLABUS_FILENAME in files:
            dirs.clear()

            sp = SyllabusProcessor(root)
            result = sp.generate()
            if result.success:
                add_syllabus(result, relpath, output_dir)

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.abspath("./templates")),
        extensions=["jinja2.ext.do"],
    )
    site_template = env.get_template("training-site.j2.html")
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(
            site_template.render(
                syllabuses=syllabuses,
                title=None,
                timestr=datetime.now(timezone.utc),
            )
        )


def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def splitpath(path):
    folders = []
    while True:
        path, folder = os.path.split(path)
        if folder != "":
            folders.append(folder)
        else:
            if path != "":
                folders.append(path)
            break
    folders.reverse()
    return folders


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: {} <syllabus_dir> <output_dir>".format(sys.argv[0]))
        sys.exit()
    generate(sys.argv[1], sys.argv[2])
