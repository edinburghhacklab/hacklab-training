#!/usr/bin/env python3
import os
import subprocess
import sys
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from os import listdir
from os.path import isfile
from os.path import join
from shutil import copytree
from tempfile import NamedTemporaryFile

import jinja2
from syllabus_processor import RISK_ASSESSMENT_FILENAME
from syllabus_processor import SYLLABUS_FILENAME
from syllabus_processor import SyllabusProcessor

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

    print(folders[-1])
    if result.card is not None:
        training_card_filename = "{}-training-card.pdf".format(
            folders[-1].replace(" ", "-")
        )
        files["Training card"] = os.path.join(relpath, training_card_filename)
        print("    training card")
        compile_tex(result.card, os.path.join(dest, training_card_filename))

    if result.doc is not None:
        training_doc_filename = "{}-training-doc.pdf".format(
            folders[-1].replace(" ", "-")
        )
        files["Training doc"] = os.path.join(relpath, training_doc_filename)
        print("    training doc")
        compile_tex(result.doc, os.path.join(dest, training_doc_filename))

    if result.risk_assessment is not None:
        risk_assessment_filename = "{}-risk-assessment.pdf".format(
            folders[-1].replace(" ", "-")
        )
        files["Risk assessment"] = os.path.join(relpath, risk_assessment_filename)
        print("    risk assessment")
        compile_tex(
            result.risk_assessment, os.path.join(dest, risk_assessment_filename)
        )

    version = result.version
    commit_date = result.commit_date

    nested_set(syllabuses, folders, Syllabus(name, version, commit_date, files))


def compile_tex(tex_string, destination_filename):
    BUILD_LIMIT = 10
    RERUN_STRINGS = ["Rerun LaTeX", "Rerun to get the"]
    with NamedTemporaryFile("w", encoding="utf-8") as f:
        f.write(tex_string)
        f.flush()
        output = "Rerun LaTeX"
        num_builds = 0
        while any([s in (output) for s in RERUN_STRINGS]):
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
                ).decode("utf-8")
            except subprocess.CalledProcessError as e:
                print(e.output.decode())
                raise
            num_builds += 1
            if num_builds > BUILD_LIMIT:
                raise


def generate(syallabus_dir, output_dir, folder_filter):
    print("Rendering training documentation...")

    syllabi = []
    for root, dirs, files in os.walk(syallabus_dir):
        relpath = os.path.relpath(root, syallabus_dir)
        if (
            any([f in [SYLLABUS_FILENAME, RISK_ASSESSMENT_FILENAME] for f in files])
            and folder_filter.lower() in root.lower()
        ):
            dirs.clear()

            sp = SyllabusProcessor(root)
            result = sp.generate()
            if result.success:
                syllabi.append((result, relpath, output_dir,))

    sorted_syllabi = sorted(syllabi, key=lambda x: x[1])
    for item in sorted_syllabi:
        add_syllabus(item[0], item[1], item[2])

    print("Rendering landing page...")
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.abspath("./templates")),
        extensions=["jinja2.ext.do"],
    )

    background_dir = "assets/backgrounds"    
    copytree(background_dir, os.path.join(output_dir, "backgrounds"), dirs_exist_ok=True)
    onlyfiles = [f"./backgrounds/{f}" for f in listdir(background_dir) if isfile(join(background_dir, f))]

    site_template = env.get_template("training-site.j2.html")
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(
            site_template.render(
                syllabuses=syllabuses,
                title=None,
                timestr=datetime.now(timezone.utc),
                images=onlyfiles
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
        print("Usage: {} <syllabus_dir> <output_dir> [filter]".format(sys.argv[0]))
        sys.exit()
    generate(
        sys.argv[1], sys.argv[2], " ".join(sys.argv[3:]) if len(sys.argv) >= 4 else ""
    )
