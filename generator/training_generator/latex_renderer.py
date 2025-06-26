import mistune
from typing import Any

BEGIN = r"\begin{%s}"
END = r"\end{%s}"


def enclose(t, s):
    return "\n%s\n%s\n%s\n" % (BEGIN % (t,), s, END % (t,))


def escape(s: str) -> str:
    return s.replace("&", "\\&")


class LatexRenderer(mistune.BaseRenderer):
    def block_code(self, code, lang=None):
        return enclose("verbatim", code)

    def block_quote(self, text):
        return enclose("quotation", text)

    def heading(self, text: str, level: int, raw=None):
        if level == 1:
            self.title = text
            return ""
        elif level < 5:
            return "\\" + "sub" * (level - 2) + "section" + "{%s}\n" % (text)
        else:
            return "\\" + "sub" * (level - 5) + "paragraph" + "{%s}\n" % (text)

    def list(self, body, depth, ordered=True):
        return enclose("itemize", body)

    def list_item(self, text):
        return r"\item " + escape(text) + "\n"

    def paragraph(self, text):
        return text + "\n\n"

    def linebreak(self):
        return "\n"

    def strong(self, text):
        return r"\textbf{%s}" % (text,)

    def emphasis(self, text):
        return r"\textit{%s}" % (text,)

    def codespan(self, text):
        return r"\texttt{%s}" % (text,)

    def hrule(self):
        return r"\hrulefill"

    def footnotes(self, text):
        print(text)
        return text

    def footnote_ref(self, key, index):
        print(key, index)
        return r"\footnotemark[%s]" % (key,)

    def footnote_item(self, key, text):
        return r"\footnotetext[%s]{%s}" % (key, escape(text))

    def reference(self, key):
        return r"\cite{%s}" % (key,)

    def image(self, src, title, text):
        return "\n".join(
            [
                r"\begin{figure}",
                r"\includegraphics{%s}" % (src,),
                r"\caption{%s}" % (escape(title),),
                r"\label{%s}" % (escape(text),),
                r"\end{figure}",
            ]
        )

    def text(self, text):
        return escape(text)

    def block_text(self, text):
        return escape(text)

    def block_html(self, _text):
        return ""

    def blank_line(self):
        return "\n"

    def softbreak(self):
        return ""

    # HACK: Copied from the HTML renderer, seems to indicate something is using an old API somewhere?
    def render_token(self, token: dict[str, Any], state) -> str:
        func = self._get_method(token["type"])
        attrs = token.get("attrs")

        if "raw" in token:
            text = token["raw"]
        elif "children" in token:
            text = self.render_tokens(token["children"], state)
        else:
            if attrs:
                return func(**attrs)
            else:
                return func()
        if attrs:
            return func(text, **attrs)
        else:
            return func(text)
