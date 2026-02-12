#!/usr/bin/env python3

# ?> ./aff_rev_params.py | cat -e
# none$
# ?> ./aff_rev_params.py "coucou" | cat-e
# none$ 
# ?> ./aff_rev_params.py "Python" "piscine" "hello" | cat -e
# hello$
# piscine$
# Python$
# ?>

import sys

if len(sys.argv) < 3:
    print("none")
else:
    for arg in reversed(sys.argv[1:]):
        print(arg)
