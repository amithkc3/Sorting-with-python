import random
import os
import time

def test_sorted(arr):
	flag = True
	for i in range(len(arr)-1):
		if(arr[i] > arr[i+1]):
			flag = False
			break
	return flag

count_merge = 0
def merge_sort(arr):
	def merge(left_arr,right_arr):
		global count_merge
		result = []
		while(left_arr and right_arr):
			count_merge += 1
			elem = (left_arr.pop(0) if(left_arr[0] < right_arr[0]) else right_arr.pop(0))
			result.append(elem)
		return (result+left_arr+right_arr,count_merge)


	if(len(arr) <= 1):
		return (arr,count_merge)
	mid = len(arr)//2

	return merge(merge_sort(arr[:mid])[0],merge_sort(arr[mid:])[0])

count_bub = 0
def bubble_sort(arr):
	global count_bub
	n = len(arr)
	for i in range(n-1):
		for j in range(0,n-1-i):
			count_bub += 1
			if(arr[j] > arr[j+1]):
				arr[j],arr[j+1] = arr[j+1],arr[j]
		# print(count_bub,end=' ')
	return (arr,count_bub)

count_selection = 0
def selection_sort(arr):
	global count_selection
	n = len(arr)
	min = 0
	for i in range(0,n-1):
		min = i
		for j in range(i+1,n):
			count_selection += 1
			if(arr[min] > arr[j]):
				min = j
		arr[min],arr[i] = arr[i],arr[min]
		# print(count_selection,end=' ')
	return (arr,count_selection)

def quick_sort(arr,low,high):
	def partion(arr,low,high):
		i= low-1
		pivot = arr[high]				#last pivot
		for j in range(low,high):		#from low to high-1
			if(arr[j] <= pivot):
				i+=1
				arr[i],arr[j] = arr[j],arr[i]

		arr[i+1],arr[high] = arr[high],arr[i+1]

		return i+1


	if(low < high):
		p = partion(arr,low,high)
		quick_sort(arr,low,p-1)
		quick_sort(arr,p+1,high)





if __name__ == '__main__':
	n = int(input("Enter n :"))
	a = [random.randint(0,10) for i in range(n)]
	os.system('cls')
	print(len(a))
	print("Sorted TEST= "+str(test_sorted(a)))
	# print(a)

	print("\n\nQuick : ")
	q_t1=time.time()
	q=a[:]
	quick_sort(q,0,n-1)
	q_t2=time.time()
	print(q_t2-q_t1)
	print("Quick TEST= "+str(test_sorted(q)))

	_ = input("Proceed : ")

	print("\n\nMerge : ")
	k_t1=time.time()
	k=merge_sort(a[:])
	k_t2=time.time()
	# print(k[0])
	print("count_merge="+str(k[1]))
	print(k_t2-k_t1)
	print("Merge TEST= "+str(test_sorted(k[0])))

	_ = input("Proceed : ")

	print("\n\nBubble: ")
	b_t1=time.time()
	b = bubble_sort(a[:])
	b_t2=time.time()
	# print(b[0])
	print("count_bubble= " + str(b[1]))
	print(b_t2-b_t1)
	print("Bubble TEST= "+str(test_sorted(b[0])))

	_ = input("Proceed : ")

	print("\n\nSelection: ")
	s_t1=time.time()
	s = selection_sort(a[:])
	s_t2=time.time()
	# print(s[0])
	print("count_selection= " + str(s[1]))
	print(s_t2-s_t1)
	print("Selection TEST= "+str(test_sorted(s[0])))
