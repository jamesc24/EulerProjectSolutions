f= [1, 2]

next = 0
sum = 0

while f[-1] < 4000000: # f[-1] = last value in the list
	f.append(f[-1] + f[-2]) # Sum of last two numbers in series

for i in f:
	if (i % 2 == 0):
		sum += i

print(sum)