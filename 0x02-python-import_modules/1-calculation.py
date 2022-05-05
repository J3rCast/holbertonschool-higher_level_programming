#!/usr/bin/python3
import calculator_1 as calculator
a = 10
b = 5

if __name__ == "__main__":
    print(f"10 + 5 = {calculator.add(a, b)}")
    print(f"10 - 5 = {calculator.sub(a, b)}")
    print(f"10 * 5 = {calculator.mul(a, b)}")
    print(f"10 / 5 = {calculator.div(a, b)}")
