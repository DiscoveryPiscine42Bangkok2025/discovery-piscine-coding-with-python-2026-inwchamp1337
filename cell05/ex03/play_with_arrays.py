#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []

for num in original:
    if num > 5:
        new_array.append(num + 2)

result = set(new_array)

print(original)
print(result)
