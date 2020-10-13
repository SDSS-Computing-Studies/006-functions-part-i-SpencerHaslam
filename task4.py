#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
def isInteger(noombar):
    num = float(noombar)
    nam = int (noombar)
    if num == nam:
        answer = True
    
    else:
        answer = False
    return answer
number = 37
number = isInteger(number)
print(number)

