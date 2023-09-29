"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
length = len(numbers)
if length % 2 == 0:
    mid = (numbers[length//2] + numbers[(length//2)-1])/2
    print(mid)
else:
    print(numbers[length//2])
