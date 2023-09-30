def insertion_sort(array):
    #buatlah fungsi insertion sort
    #[...code here...]
	for i in range(1,len(array)-1):
		number = array[i]
		j = i -1
		while j >= 0 and array[j] > number :
			array[j+1] = array[j]
			j = j -1
		array[j+1] = number
	return array
    #return array

def binarySearch(arr, r, x): 
	
	l = 0

	while l <= r: 

		# Definisikan variable elemen tengah yaitu mid yang merupakan "l + (r - 1) // 2"
		mid = (l + (r-1)) //2
		# Cek apakah nilai x = arr[mid], jika iya kembalikan nilai mid
		if arr[mid] == x :
			return mid

		# Jika nilai x lebih besar dari arr[mid], maka "l = mid + 1"
		if arr[mid] < x:
			l = mid + 1
		else:
			r =mid -1

		# Jika nilai x lebih kecil dari arr[mid], maka "r = mid - 1"
	
	return -1
# array 
arr = [12, 15, 8, 1, 45, 13, 20, 48, 72, 88, 7 ,45, 19, 66, 78, 33, 99, 78, 44, 65, 110, 97, 92] 
  
#panggil fungsi insertion sort
isort = insertion_sort(arr)

# print insertion sort
print(isort)


#panggil fungsi binary search
bs = binarySearch(arr,len(arr)-1,20)

#jika hasil searching bernilai -1, keluarkan info bahwa elemen tidak ditemukan
if bs == -1:
	print("Elemen tidak di temukan")
else:
	print(f"elemen berada di index {bs}")

#jika hasil searching tidak bernilai -1, keluarkan info berada di index ke berapa

