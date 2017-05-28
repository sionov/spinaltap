def isPrime (x):
	for a in range (2, int(x/2)):
		if (x % a == 0):
			return False
	return True

def pLogger(n):
	numPrimes = 0
	i = 1
	while (numPrimes < n):
		if isPrime(i):
			numPrimes+=1
			print(i)
		i+=1

pLogger(10)