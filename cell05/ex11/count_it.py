#!/usr/bin/env python3


# ?> ./count_it.py | cat -e
# none$
# ?> ./count_it.py "Game" "of" "Thrones" | cat -e
# parameters: 3$
# Game: 4$
# of: 2$
# Thrones: 7$
# ?

import sys

if len(sys.argv) == 1:
    print("none")
else:
    params = sys.argv[1:]
    print(f"parameters: {len(params)}")

    for param in params:
        print(f"{param}: {len(param)}")
