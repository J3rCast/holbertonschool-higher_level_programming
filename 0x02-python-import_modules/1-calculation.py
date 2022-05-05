#!/usr/bin/python3
import calculator_1 as calculator
a = 10
b = 5

dict = {'add': '+', 'sub': '-', 'mul': '*', 'div': '/'}

print(f"{a} {dict['add']} {b} = {calculator.add(a, b)}")
print(f"{a} {dict['sub']} {b} = {calculator.add(a, b)}")
print(f"{a} {dict['mul']} {b} = {calculator.add(a, b)}")
print(f"{a} {dict['div']} {b} = {calculator.add(a, b)}")
