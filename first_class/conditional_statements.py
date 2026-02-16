# Simple if
temperature = - 25
if temperature > 20:
    print("It's a warm day.")
print("Simple if  statement executed.")

# nested if
age = 25
if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are eligible to work.")
print("Nested if statement executed.")

# if-elif-else
marks = 90
if marks > 90 & marks <= 100:
    print("Grade: A")
elif marks >= 80 & marks < 90:
    print("Grade: B")
elif marks >= 70 & marks < 80:
    print("Grade: C")
else:
    print("Grade: F")
print("if-elif-else statement executed.")

