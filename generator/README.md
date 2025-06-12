# Hacklab training generator

Generates training documentation from Markdown sources.

# Getting started

## Prerequisites

Python dependencies are handled by `uv`. non-python dependencies are:

 -  pdflatex
 -  texlive-latex-base
 -  texlive-latex-extra

For most development, it's easiest to run `just build-devcontainer` and `just devcontainer`, then `uv run ./training_generator main.py .. out/`.

Please also use `just fmt lint` before PRing.

## Usage

    ./training_generator/main.py <syllabus_dir> <output_dir>

# Syllabus layout

The source syllabuses are written in Markdown and should be named `syllabus.md`.

Each syllabus should be in its own directory, and directories may be nested to create categories and sub-categories. A syllabus directory may also include related materials, which may be copied to the output directory in a future version.
