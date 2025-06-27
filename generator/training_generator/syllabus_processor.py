import jinja2
from latex_renderer import LatexRenderer
import mistune
import os
from os.path import join, exists
import subprocess
from dataclasses import dataclass
import latex_renderer

SYLLABUS_FILENAME = "syllabus.md"
RISK_ASSESSMENT_FILENAME = "risk-assessment.md"


class Item:
    def __init__(self, name, level, section, parent_section):
        self.name = name
        self.level = level
        self.items = []
        self.section_number = section
        self.section_string = parent_section + str(section) + "."
        self.indent = max(level - 3, 0)
        self.children = False
        self.text = ""

    def __iter__(self):
        return iter(self.items)

    def add(self, item):
        self.items.append(item)
        self.children = True
        return item

    def __getitem__(self, item):
        return self.items[item]

    def section(self):
        # Trim leading chars (since everything is under root&title header) and trailing "."
        return self.section_string[4:-1]

    def __str__(self):
        return f"<Item name={self.name} level={self.level} section_number={self.section_number} section_string={self.section_string} indent={self.indent} items={list(map(str, self.items))} text='{self.text}'>"


class TreeRenderer(mistune.BaseRenderer):
    def reset_tree(self):
        self.tree = Item("root", 0, 0, "")
        self.node_stack = [self.tree]
        self.level = 0

    def add_node(self, text, level, section):
        parent = self.node_stack[-1]
        new_node = Item(text, level, section, parent.section_string)
        parent.add(new_node)
        self.node_stack.append(new_node)
        self.level = level

    def heading(self, text, level, raw=None):
        self.node_stack[-1].text = self.node_stack[-1].text.removesuffix(text)
        if text not in ["Training", "Evaluation"]:
            if level == self.level + 1:
                # one level deeper: add new node below current one
                self.add_node(text, level, 1)
            elif level == self.level:
                section = self.node_stack.pop().section_number + 1
                self.add_node(text, level, section)
            elif level <= self.level:
                # move up to appropriate parent and add new node there
                section = 0
                while level <= self.level:
                    section = self.node_stack.pop().section_number + 1
                    self.level = self.node_stack[-1].level
                self.add_node(text, level, section)
            else:
                # throw error that new header skips a level
                print("error error error")

        return super(TreeRenderer, self).heading(text, level, raw)  # type:ignore

    def list(self, body, depth, ordered=True):
        out = super(TreeRenderer, self).list(body, depth, ordered)  # type:ignore
        self.node_stack[-1].text += out
        return out

    def paragraph(self, text):
        out = super(TreeRenderer, self).paragraph(text)  # type:ignore
        self.node_stack[-1].text += out
        return out


class Renderer(TreeRenderer, LatexRenderer):
    pass


def walk(item, level):
    print("\t" * level + item.name)
    for i in item:
        walk(i, level + 1)


@dataclass
class SyllabusResult:
    success: bool
    version: str
    commit_date: str
    card: str | None = None
    doc: str | None = None
    risk_assessment: str | None = None


class SyllabusProcessor:
    def __init__(self, path):
        self.path = path
        self.latex_jinja_env = jinja2.Environment(
            block_start_string="\\BLOCK{",
            block_end_string="}",
            variable_start_string="\\VAR{",
            variable_end_string="}",
            comment_start_string="\\#{",
            comment_end_string="}",
            line_statement_prefix="%%",
            line_comment_prefix="%#",
            trim_blocks=True,
            autoescape=False,
            loader=jinja2.FileSystemLoader(os.path.abspath("./templates")),
        )

    def generate(self):
        card = None
        doc = None
        version = self.get_git_version()
        commit_date = self.get_git_date()
        if exists(join(self.path, SYLLABUS_FILENAME)):
            with open(join(self.path, SYLLABUS_FILENAME), encoding="utf-8") as f:
                s = f.read()

            tree = Renderer()
            md = mistune.Markdown(renderer=tree)
            tree.reset_tree()
            md.parse(s)

            card = self.latex_jinja_env.get_template("training-card.j2.tex").render(
                items=tree.tree[0], version=version, sessions=8
            )
            doc = self.latex_jinja_env.get_template("training-doc.j2.tex").render(
                content=md(s), title=tree.title, version=version
            )

        risk_assessment = None
        if exists(join(self.path, RISK_ASSESSMENT_FILENAME)):
            tree = Renderer()
            md = mistune.Markdown(renderer=tree)
            tree.reset_tree()
            with open(join(self.path, RISK_ASSESSMENT_FILENAME), encoding="utf-8") as f:
                md.parse(f.read())

            risk_assessment = self.latex_jinja_env.get_template(
                "risk-assessment.j2.tex"
            ).render(items=tree.tree[0], title=tree.title, version=version)

        return SyllabusResult(
            success=True,
            doc=doc,
            card=card,
            version=version,
            commit_date=commit_date,
            risk_assessment=risk_assessment,
        )

    def get_git_date(self):
        return (
            subprocess.check_output(
                ["git", "log", "-n1", "--pretty=%ci", os.path.abspath(self.path)],
                cwd=self.path,
            )
            .strip()
            .decode("ascii")
        )

    def get_git_version(self):
        return (
            subprocess.check_output(
                ["git", "log", "-n1", "--pretty=%h", os.path.abspath(self.path)],
                cwd=self.path,
            )
            .strip()
            .decode("ascii")
        )


if __name__ == "__main__":
    sp = SyllabusProcessor(".")
    sp.generate()
