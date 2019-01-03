import string
import itertools
import time
def bruteforce(s):
	print(s)
	print(len(s))
	l2 = []
	l1 = list(itertools.permutations(range(32,127),len(s)))
	#print(str(l1))
	t0 = time.time()
	for tuples in l1:
		tuples = list(tuples)
		for nums in range(len(tuples)):
			tuples[nums] = str(chr(tuples[nums]))
		tuples = ''.join(tuples)
		if s==tuples:
			print('Match found in ' +str(time.time()-t0))
			exit()
	#t0 = time.perf_counter()
	#for password in l2:
	#	if s==password:
	#		print('Match found in ' +str(time.time()-t0))
	#		exit()
				
bruteforce(input('Enter password minimum of 3 letters and maximum of 30'))