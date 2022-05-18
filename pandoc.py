from panflute import *
from sys import stderr

headers = []


def bold(doc):
    doc.replace_keyword("BOLD", Strong(Str("BOLD")))


def duplicateHeaders(elem, doc):
    if type(elem) == Header:
        text = stringify(elem)
        if text in headers:
            print("Duplicate headers", file=stderr)
        else:
            headers.append(text)


def upper_str(elem, doc):
    if type(elem) == Str:
        elem.text = elem.text.upper()


def upper_header(elem, doc):
    if type(elem) == Header and elem.level > 2:
        return elem.walk(upper_str)


if __name__ == "__main__":
    run_filters([upper_header, duplicateHeaders], prepare=bold)

