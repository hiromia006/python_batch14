import os
from pathlib import Path

current_dir = Path.cwd()
print(current_dir)

current_dir = os.getcwd()
print(current_dir)

fileName="/home/jannat-mugdho/PycharmProjects/python_batch14/number.txt"
with open(fileName, "w") as file:
    file.write("Hello World1")

with open(fileName, "a") as file1:
    file1.write("\nHello World2")

with open(fileName, "r") as file2:
    print( file2.read())

