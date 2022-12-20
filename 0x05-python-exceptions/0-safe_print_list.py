#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	elm_nbr = 0
	for i in range(x):
		try:
			print(my_list[i])
			elm_nbr += 1
		except:
			return elm_nbr
	return elm_nbr
