# Simplified loop examples

# Basic for loop
for i in range(10):
    print("i is", i)
print("i is finished")

print("-----------------------------")

# For loop with initial value
for i in range(4, 10):
    print("i is", i)
print("i is finished")

print("======================")

# For loop with step
for i in range(2, 10, 3):
    print("i is", i)

print("======================")

# For loop with negative step
for j in range(20, 0, -5):
    print("j is", j)

print("------ While loop ------")

# While loop with decrement
k = 5
while k > 0:
    print("k is", k)
    k -= 1

# While loop with increment
l = 0
while l <= 10:
    print("l is", l)
    l += 1

from