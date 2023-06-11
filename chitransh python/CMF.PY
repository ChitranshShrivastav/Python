def binary_search(arr,low,high,x):
    if high >=low:
        mid = (high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid>x]:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
        
    else:
        return -1
arr=[1,2,3,4,5,6,7,8,9]
x=int(input("enter the no.: "))
result=binary_search(arr,0,len(arr)-1,x)
if result != -1:
    print("element is present at index:12 ",str(result))
else:
    print("get lost!!!!")

        

