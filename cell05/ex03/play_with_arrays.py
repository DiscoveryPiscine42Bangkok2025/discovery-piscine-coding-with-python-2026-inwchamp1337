#!/usr/bin/env python3
# ?> ./play_with_arrays.py | cat -e
# [2, 8, 9, 48, 8, 22,-12, 2]$
# {24, 10, 11, 50}$
# ?
original = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []

for num in original:
    if num > 5: 
        new_array.append(num + 2) #new_array = [10, 11, 50, 10, 24]

result = set(new_array)

print(original)
print(result)
