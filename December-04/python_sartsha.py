def fibo(nth):
	if nth == 1:
		return 0
	elif nth in [2,3]:
		return 1
	else:
		ans = fibo(nth-1)+fibo(nth-2)
	return ans
n = int(input())
print(fibo(n))
