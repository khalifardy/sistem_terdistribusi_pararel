arr = [1,1,1,1,2,2,2,4,4,4,5,6,9,8,7,4,1,2,3,6,52,1,63,516,5,13,5,416,5,3,1,32,13,21,3,54,55,4,45,73,856,1,74,8,74,8,5,3,85,7,4,1,25,8,693,21,47,8,5,63,32,24,7,8]

#[...code here...]

#print banyaknya nilai 1
def nilai_1(array):
    count = 0
    for i in array:
        if i ==1 :
            count += 1

    return count

print(nilai_1(arr))

#insert nilai -999 pada index ke 3
arr1 = arr.copy()
arr1.insert(3,-999)
print(arr1)

#print index 856
print(arr.index(856))

#print reverse dari list
print(arr[::-1])

#print value index terakhir dari list
print(arr[-1])

#insert value -678
arr2 = arr.copy()
arr2.append(-678)
print(arr2)

#print setengah bagian terdepa dari list

index_mid = len(arr)//2
print(arr[:index_mid+1])
