def recursiveFibonacci(a):
	if a == 1:
		return 0
	if a == 2:
		return 1
	return recursiveFibonacci(a-1) + recursiveFibonacci(a-2)