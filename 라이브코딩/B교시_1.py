max = int(input())

for n in range(2,max+1):
	for f in range(2,n):
		if n % f == 0:
			break;
	else:
		print(n, end=' ')
print()
