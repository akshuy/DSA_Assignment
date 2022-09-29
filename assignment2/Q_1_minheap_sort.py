def heapify(arr,n,i):
    smallest = i
    l = 2 * i + 1        
    r = 2 * i + 2  
    
    if l < n and arr[l] > arr[smallest]:
        smallest = l      

    if r < n and arr[r] > arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # swap     
        heapify(arr, n, smallest)      
def buildheap(arr,n):
    startindex = (n//2)-1
    for i in range(startindex,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    buildheap(arr,n)
    print("sort into minheap : ")
    for i in range(n):
        print("%d" % arr[i], end=" ")