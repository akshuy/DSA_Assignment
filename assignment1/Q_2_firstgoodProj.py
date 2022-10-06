"""2. You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad version
are also bad. Suppose you have n version and you want to find out the first bad one,
which causes all the following ones to be bad. Also, talk about the time complexity of
your code.
Test Cases:
Input: [0,0,0,1,1,1,1,1,1]
Output: 3
Explanation: 0 indicates a good version and 1 indicates a bad version. So, the index of
the first 1 is at 3. Thus, the output is 3
"""

# TODO Linear serch
def linearsearch(myProj):
    for i in range(len(myProj)):
        if myProj[i] == 1:
            return i
myProj = [0,0,0,1,1,1,1,1,1]
num = 1
result = linearsearch(myProj)
print(f"LinearSearch----->>>>>>> index no. _____{result}_____ is your first bad project")

# TODO Binary search
def searchBadproj(myProject,number,left,right,mid):
    for i in range(len(myProject)):

        if myProject[mid-1] > number:
            return mid
        elif myProject[mid] == number: 
            return searchBadproj(myProject, number, left, right,mid-1)

        elif myProject[mid+1] > 0:         
            return mid + 1
        elif myProject[mid] == 0: 
            return searchBadproj(myProject, number, left, right,mid+1)    

        elif myProject[mid] < number:
            return searchBadproj(myProject, number, mid+1, right,mid)
       
        else:
            return searchBadproj(myProject, number, left, mid-1)    
        
myProject = [0,0,0,1,1,1,1,1,1]
number = 1
left = 0
right = len(myProject)-1
mid = left + (right-left)//2
firstgood_Project = searchBadproj(myProject,number,left,right,mid)
print(f"BinarySearch----->>>>>>> index no. _____{firstgood_Project}_____ is your first bad project")