"""Build javascript file for livecode options.

This generates mon_school/public/js/livecode-files.js

This file is triggered via make. See Makefile.
"""

from pathlib import Path
import json

def read_file(filename):
    print("reading", filename, "...")
    return Path(__file__).parent.joinpath(filename).read_text()

def write_file(filename, contents):
    print("writing", filename, "...")
    return Path(__file__).parent.joinpath(filename).write_text(contents)

LIVECODE_FILES = None

def get_livecode_files():
    global LIVECODE_FILES
    if LIVECODE_FILES is None:
        filenames = ["start.py", "joy.py", "sketch.py"]
        LIVECODE_FILES = [{"filename": f, "contents": read_file(f)} for f in filenames]

    return LIVECODE_FILES

def main():
    livecode_files = get_livecode_files()
    livecode_json = json.dumps(livecode_files)

    js = f"const LIVECODE_FILES = {livecode_json};"
    write_file("../public/js/livecode-files.js", js)

if __name__ == "__main__":
    main()