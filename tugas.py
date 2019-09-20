def BinarySearch(list1,key):
    low = 0
    high = len(list1)-1
    Found = False
    while low <= high and not Found:
        mid = (low+high)//2
        if key == list1[mid]:
            Found = True
        elif key > list1[mid]:
            low = mid+1
        else:
            high = mid-1
    if Found == True:
        print("1")
    else:
        print("0")

list1 = [4,7,9,13,16,18,20]
print(list1)
key = int(input("enter the number"))
BinarySearch(list1,key)