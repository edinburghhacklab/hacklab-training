# Hacklab training generator

Generate training documentation from Markdown sources.

# Getting started

## Prerequisites

    jinja2
    mistune
    pdflatex
    python3
    texlive-latex-base
    texlive-latex-extra

## Usage

    ./generate.py <syllabus_dir> <output_dir>

# Syllabus layout

The source syllabuses are written in Markdown and should be named `syllabus.md`.

Each syllabus should be in its own directory, and directories may be nested to create categories and sub-categories. A syllabus directory may also include related materials, which may be copied to the output directory in a future version.

## Example

Directory layout:

    ./syllabuses/
        Workshop/
            CNC Mill/
                syllabus.md
                materials/
                    checklist.pdf
            Bandsaw/
                syllabus.md
    ./output/

Run:

    ./generate.py syllabuses/ output/
