def get_summ(one, two, delimiter='&'):
	return str(one).upper() + str(delimiter).upper() + str(two).upper()

#print(get_summ('Learn', 'python', ' '))

sum_string=get_summ('Learn', 'python', ' ')
sum_string
print(sum_string)
