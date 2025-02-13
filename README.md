Bibliography Sort & Check Scripts

Overview

This repository contains Python scripts to:

Sort a .bib bibliography file alphabetically by the first author's last name.

Verify if a .bib file is correctly sorted, ensuring no entries are missing or duplicated.

Files

sort_bib.py: Reads a .bib file and sorts it alphabetically.

sortcheck.py: Compares an original and sorted .bib file to check for errors.

Usage

Sorting a .bib file:

Run the script with:

python sort_bib.py

Input file: references.bib

Output file: sorted_references.bib

Checking Sorting Accuracy:

Run the script with:

python sortcheck.py

Compares references.bib with sorted_references.bib.

Requirements

Python 3.x

No external dependencies (uses built-in re module)

License

This project is licensed under the MIT License.

