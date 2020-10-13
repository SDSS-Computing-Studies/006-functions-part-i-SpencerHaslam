#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math
def hypotenuse(a,b,c):
    if c == True:
        answer = math.sqrt((a**2) + (b**2))
    else:
        nums = [a,b]
        nums = nums.sort()
        num1 = nums[0]
        num2 = nums[1]
        answer = math.sqrt((num1**2) - (num2**2))
    return answer


a = 3
b = 4
c = True
print(hypotenuse(a,b,c))

