#!/usr/bin/env python3
# ?> ./string_are_arrays.py | cat -e
# none$
# ?> ./string_are_arrays.py "The character Z is not found in this string" | cat -e
# none$
# ?> ./string_are_arrays.py "The character z is found in this string" | cat -e
# z$
# ?> ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat-e
# zzz$
# ?
import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    count = text.count("z")

    if count == 0:
        print("none")
    else:
        print("z" * count)
