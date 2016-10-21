from math import sqrt, floor
#won't work on smaller numbers (<9), but it will work on larger numbers.
def isPrime(number):
	for x in range(2, int(sqrt(number))): #To save computation time, only go to the square of the provided number
		result = float(number) / float(x)
		if result - floor(result) == 0: #To avoide the floating point accuracy problem that'd come with modulo, I found a work around.
			return False #Stop if it's found to not be prime
	return True #Return true if prime

#load and store e as a string
e = ""
with open("e.txt") as inFile:
	for line in inFile:
		e = line.rstrip()

firstDigit = 2 #Location of first digit

while (firstDigit < len(e)-10):
	numberToTest = e[firstDigit:firstDigit+10] #Get a substring the number to test.
	if isPrime(int(numberToTest)): #If the number is prime print it out and exit.
		print numberToTest
		exit()
	firstDigit += 1