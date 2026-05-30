def reverseArray(arr):
    l=0
    r=len(arr)-1
    while l<r:
      arr[l] ,arr[r]= arr[r],arr[l]
      l +=1
      r -=1

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")