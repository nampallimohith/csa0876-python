def find_powers(number):
    square = number ** 2
    cube = number ** 3
    return square, cube
number = 5
square, cube = find_powers(number)
print(f"The square of {number} is {square}")
print(f"The cube of {number} is {cube}")
