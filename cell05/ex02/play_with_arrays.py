#!/usr/bin/env python3

og_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []

for num in og_array:
    if num > 5:
        new_array.append(num + 2)

print(og_array)
print(new_array)
