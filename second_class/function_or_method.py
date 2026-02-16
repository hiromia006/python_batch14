# def function name ()
def print_marks():
    for mark in range(1, 11):
        print(mark)


print_marks()


def calculate_sum(a, b):
    return a + b

def calculate_subtract():
    a=89
    b=10
    return a - b

print("calculate_sum ", calculate_sum(10, 2))
print("calculate_sum ", calculate_sum(50, 20))

print("calculate_subtract ", calculate_subtract())
print("calculate_subtract ", calculate_subtract())

def calculate_all(a, b):
    summation=a+b
    subtraction=a-b
    multiplication=a*b
    division=a/b
    return summation,subtraction,multiplication,division

print("calculate_all ", calculate_all(10, 2))
print("calculate_all ", calculate_all(50, 20))

