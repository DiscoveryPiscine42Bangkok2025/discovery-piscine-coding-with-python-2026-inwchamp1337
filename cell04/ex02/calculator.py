#!/usr/bin/env python3

num1 = float(input("Give me the first number: "))
num2 = float(input("Give me the second number: "))

print("Thank you!")
print(f"{num1:g} + {num2:g} = {num1 + num2:g}")
print(f"{num1:g} - {num2:g} = {num1 - num2:g}")

if num2 != 0:
    print(f"{num1:g} / {num2:g} = {num1 / num2:g}")
else:
    print("Division by zero is not allowed.")

print(f"{num1:g} * {num2:g} = {num1 * num2:g}")
