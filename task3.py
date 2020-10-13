#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""
def perimeter(lisst):
    num = 0
    for x in lisst:
        num = num + x
    answer = num
    return answer

leest = [5,2,6]
last = perimeter(leest)
print(last) 