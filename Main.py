nstart = 2**68
n = 2**68
continuous = True

try:
	f = open("resume.txt")
	# Do something with the file
except IOError:
	print("File not accessible")
	open("resume.txt", "w+")
finally:
	f.close()
ts = open("resume.txt", "a+")
while continuous:
	while (n % 2) != 0:
		n = n * 3 + 1
		print(n)

	while (n % 2) == 0:
		n = n / 2
		print(n)
		if n == 1:
			ts.write(f'test on {nstart} brought us to \n')
			n = n + nstart - 1
			nstart = nstart + 1
		  
