import math

anumber = 0

try:
    anumber = int(input("Please enter an integer "))
    print(math.sqrt(anumber))
except:
    print("Bad Value for square root")
    print("Using default value instead")
    print(math.sqrt(abs(anumber)))
