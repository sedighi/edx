#  Write a function that accepts a positive integer k and returns a list that contains the first five multiples of k.
#  The multiples should be calculated starting from 1 to 5 (including both 1 and 5). For example the first five
#  multiples of 3 are 3, 6, 9, 12, and 15
'''
def _calc_multiple(k):
	multi = []
	for a in range(1,k*5+1):
		if a % k ==0:
			multi.append(a)

	return multi
print (_calc_multiple(4))
'''
#[4, 8, 12, 16, 20]

# Write a function that accepts two positive integers a and b and returns a list of all the even numbers between
# a and b (including a and not including b).
'''
def _even_list(a,b):
	mlist = []
	for k in range(a,b):
		if k % 2 == 0:
			mlist.append(k)
	return mlist
print (_even_list(2,8))
'''
# Write a function that accepts two positive integers a and b (a is smaller than b)and returns a list that
# contains all the odd numbers between a and b (including a and including b if applicable) in descending order.
'''
def _odd_list(a,b):
	mlist=[]
	for k in range(a,b+1):
		if k % 2 ==1:
			mlist.append(k)
	mlist.sort(reverse=True)
	return mlist
print(_odd_list(11,31))
'''
# Write a function that accepts a positive integer k and returns the ascending sorted list of cube root values
# of all the numbers from 1 to k (including 1 and not including k). [if k is 1, your program should return an
# empty list]
'''
def _root_cube(a):
	mlist=[]
	for k in range(1 ,a):
		k = k ** (1/3)
		mlist.append(k)
	return mlist
print (_root_cube(5))
'''
# Write a function that accepts a positive integer k and returns the list of all the divisors of k.
# Your list should include both 1 and k.
'''
def _divisors(a):
	mlist=[]
	for k in range(1,a+1):
		if a%k==0 :
			mlist.append(k)
	return mlist
print (_divisors(50))
'''
# Write a function that accepts a list as input and returns a new list which includes every other element
#  in the original list. Keep the first element, i.e. input_list[0]. For example if:
#
# input_list = ["we", "love", "python", "so","much"]
# then your function should return a list such as:
# ['we', 'python', 'much']

# def _own_list(a):
# 	d = a[0]
# 	b = a.remove(a[0])
#
# 	return b
# print (_own_list(["we", "love", "python", "so","much"]))


def _every_other_element_sample_(sample_list):
	output = []
	length = len(sample_list)
	output.append(sample_list[0])
	for element in range(1, length):
		if element % 2 == 0:
			output.append(sample_list[element])
	return output
print (_every_other_element_sample_(["we", "love", "python", "so","much"]))
