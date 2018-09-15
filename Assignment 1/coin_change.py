#Given infinite number of 2 and 5 rupee coins and amount (inputed by user).
#Program should tender change such that the number of coins of each denomination are (almost) same.

amount = input("Enter the amount = ")

count_2 = count_5 = amount / 7

res = amount % 7
pos = 1
if res == 1:
	if count_2 >= 2:
		count_2 -= 2
		count_5 += 1
	else:
		print "Cannot tender change!"
		pos = 0
elif res == 2:
	count_2 += 1
elif res == 3:
		if count_2 >= 1:
			count_2 -= 1
			count_5 += 1
		else:
			print "Cannot tender change!"
			pos = 0
elif res == 4:
		count_2 += 1
elif res == 5:
		count_5 += 1
elif res == 6:
		count_2 += 3

if pos == 1:
	print "2 rupee coins = ", count_2,"\n5 rupee coins = ", count_5
