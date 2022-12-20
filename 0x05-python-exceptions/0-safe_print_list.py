#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	elm_nbr = 0
	for i in range(x):
		try:
			print(my_list[i], end="")
			elm_nbr += 1
		except:
			print("\n", end="")
			return elm_nbr
	print("\n", end="")
	return elm_nbr
