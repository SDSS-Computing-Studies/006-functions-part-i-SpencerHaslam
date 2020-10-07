#!python3

def sum(a,b):
    #inputs
    # a : float 
    # b : float
    # return value: returns the sum of the 2 numbers
    answer = a + b
    return answer

def power(a,b):
    answer = a**b
    return answer

def input2Float():
    a = input("Enter a float:")
    b = input("Enter another float:")
    a = float(a)
    b = float(b)
    return [a,b]

def output(value):
    print("The answer is " + str(value))
#this should return a value of 7
x = sum(3,4)

#this should return a value of 12.5
y = sum(11,1.5)
print(x)
print(y)

print("\n\n")



x,y = input2Float()
answer = sum(x,y)
output(answer)
