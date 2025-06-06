import jinja2
from latex_renderer import LatexRenderer
import mistune
import os
from os.path import join
import subprocess


class Item:
    def __init__(self, name, level, section, parent_section):
        self.name = name
        self.level = level
        self.items = []
        self.section_number = section
        self.section_string = parent_section + str(section) + "."
        self.indent = max(level - 3, 0)
        self.children = False

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


class Renderer(TreeRenderer, LatexRenderer):
    pass


def walk(item, level):
    print("\t" * level + item.name)
    for i in item:
        walk(i, level + 1)


class SyllabusResult:
    def __init__(self, success, error="", card="", doc="", version="", commit_date=""):
        self.success = success
        self.error = error
        self.card = card
        self.doc = doc
        self.version = version
        self.commit_date = commit_date


class SyllabusProcessor:
    def __init__(self, path):
        self.path = path

    def generate(self):
        try:
            with open(join(self.path, "syllabus.md"), encoding="utf-8") as f:
                s = f.read()
        except IOError as e:
            return SyllabusResult(
                success=False, error="I/O error({0}): {1}".format(e.errno, e.strerror)
            )

        tree = Renderer()
        md = mistune.Markdown(renderer=tree)
        tree.reset_tree()
        md.parse(s)

        latex_jinja_env = jinja2.Environment(
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
        training_card_template = latex_jinja_env.get_template("training-card.tmpl")
        version = self.get_git_version()
        commit_date = self.get_git_date()
        card = training_card_template.render(
            items=tree.tree[0], version=version, sessions=8
        )

        doc_template = latex_jinja_env.get_template("training-doc.tmpl")
        doc = doc_template.render(content=md(s), title=tree.title, version=version)

        return SyllabusResult(
            success=True, doc=doc, card=card, version=version, commit_date=commit_date
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
