#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
def largest(list):
    answer = list.sort()
    answer = list[-1]
    return answer
    
leest = [3,1,4,7,13,9]
big = largest(leest)
print (big)