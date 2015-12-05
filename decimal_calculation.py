#! /usr/bin/env python3

import decimal

decimal.getcontext().prec = 4

print(decimal.Decimal(250.05) + 33.25)  # error, unsupported operand types, Decimal and float

print(decimal.Decimal(250.05) + decimal.Decimal(33.25))

# if you use decimal.Decimal objects, all operands need to decimal.Decimal
