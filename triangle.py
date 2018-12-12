import math

side1 = int(input("Type in a value for the first side of the triangle"))
side2 = int(input("Type in a value for the second side of the triangle"))

side3 = math.sqrt(side1 ** 2 + side2 ** 2)

print(f"The value of the hypotenuse of the triangle is {side3}")