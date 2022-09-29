"""3. Given a positive integer num, write a program that returns True if num is a perfect
square else return False. Do not use built-in functions like sqrt. Also, talk about the time
complexity of your code.
Test Cases:
Input: 16
Output: True
Input: 14
Output: False"""

# TODO Linear search
def checkPerfectsqr_linear(number):
    for i in range(1,num):
        if i*i==num:
            return True
    return False    

num = 11
result = checkPerfectsqr_linear(num)
print(f"linear Search result {result}")

# TODO Binary search
def checkPerfectsqr_Binary(number,left,right,mid):
    for i in range(1,number):        
        if i*i == number:
            return True
        elif i*i < number:
            left = mid-1
        else:
           right = mid+1
    return False
number = 144
left = 0
right = number-1
mid = left + (right-left)//2
result = checkPerfectsqr_Binary(number, left, right, mid)
print(f"Binary Search result {result}")