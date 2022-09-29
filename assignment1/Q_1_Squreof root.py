"""1. Compute and return the square root of x, where x is guaranteed to be a non-negative
integer. And since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned. Also, talk about the time complexity of your
code.
Test Cases:
Input: 4
Output: 2
Input: 8
Output: 2
Explanation: The square root of 8 is 2.8284…., the decimal part is truncated and 2 is
returned.
Hint: Try to use a modified binary search approach for an optimized solution
"""
import math
number = int(input("enter the no : "))
root = int(math.sqrt(number))
print(root)
# timecomplixity = O(1)