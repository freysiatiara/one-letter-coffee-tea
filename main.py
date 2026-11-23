"""One Letter: Coffee or Tea — entry B (tea).

The program writes exactly one letter, "B" for tea, to
/output/entry.txt and nothing else. No word, no explanation,
no punctuation: a single byte, so the gate (UTF-8, exactly
1 character, not whitespace) passes and the judge reads the
letter as a whole answer for tea.
"""

import os
import sys

# The single letter this entry sends: B stands for tea.
LETTER = "B"

# Where the harness reads the entry from. Overridable with
# ENTRY_OUTPUT only for local verification; the graded run
# always uses the default /output/entry.txt.
DEFAULT_OUTPUT = "/output/entry.txt"
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)


def validate(path=OUTPUT_PATH, letter=LETTER):
    """Read the written file back and prove it holds exactly one
    letter: the expected character, a single UTF-8 code point,
    and not whitespace. Returns True only when every check holds.
    """
    with open(path, "r", encoding="utf-8") as handle:
        content = handle.read()
    if len(content) != 1:
        return False
    if content != letter:
        return False
    if content.isspace():
        return False
    return True


def write_letter(path=OUTPUT_PATH, letter=LETTER):
    """Write exactly one letter to path, no trailing newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(letter)
    return path


if __name__ == "__main__":
    write_letter()
    # Tea is the quieter answer: one letter, no steam, no fuss.
    # The gate only cares that the file holds exactly "B".
    if not validate():
        print("validation failed: /output/entry.txt is not exactly 'B'",
              file=sys.stderr)
        sys.exit(1)
    sys.exit(0)
