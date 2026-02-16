#  Arithmetic Operators +, -, *, /, %, **, //
a = 10
b = 3
print("==================Arithmetic Operators:===========================")
print("Addition:", a)
print("Subtraction:", b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
# Comparison Operators ==, !=, >, <, >=, <=
print("==================Comparison Operators:===========================")

print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)

# Logical Operators and, or, not
print("==================Logical Operators:===========================")
print("Logical AND:", (a > 5) and (b < 5))
print("Logical AND:", (a > 15) and (b < 5))
print("Logical OR:", (a > 5) or (b > 5))
print("Logical NOT:", not(a > 5))

# Assignment Operators =, +=, -=, *=, /=, %=, **=, //=
print("==================Assignment Operators:===========================")
c = 15
print("Initial value of c:", c)
c += 2 # Equivalent to c = c + 2
print("After c += 2:", c)
c -= 1
print("After c -= 1:", c)
c *= 3  # Equivalent to c = c * 3
print("After c *= 3:", c)
c /= 2
print("After c /= 2:", c)
c %= 4
print("After c %= 4:", c)
c **= 2 # c^=2 is equivalent to c = c ** 2
print("After c **= 2:", c)
c //= 3
print("After c //= 3:", c)
