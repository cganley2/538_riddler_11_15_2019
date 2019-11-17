import random as r
############################################
def concat(multDigit,flag):

	oneDigit = makeRandomNum()

	if len(multDigit) == 0:
		if oneDigit != 0:
			multDigit.append(oneDigit)
			return multDigit, flag
		else:
			multDigit.append(oneDigit)
			flag = 1
			return multDigit, flag

	elif oneDigit <= multDigit[len(multDigit)-1] and oneDigit == 0:
		multDigit.append(oneDigit)
		flag = 1
		return multDigit, flag

	elif oneDigit <= multDigit[len(multDigit)-1]:
		multDigit.append(oneDigit)
		return multDigit, flag

	else:
		return multDigit, flag

############################################
def makeRandomNum():

	oneDigit = r.randrange(0,9,1)
	return oneDigit

############################################
def main():

	iterations = 1000000 #one million iterations takes ~20 seconds to run
	numList = []
	for i in range(iterations):
		multDigit = []
		flag = 0
		while flag != 1:
			multDigit, flag = concat(multDigit,flag)
			
		numList.append(multDigit)
	# print(numList)		#numList before making lists into decimals

	print('Max rolls was: ',len(max(numList)))
	
	totalRolls = 0

	for j in range(len(numList)):
		totalRolls = totalRolls + len(numList[j])
		num = int(''.join(map(str,numList[j])))
		exponent = len(numList[j])
		numList[j] = num/(10**exponent)

	print('Average rolls was: ',totalRolls/iterations)

	# for c in range(len(numList)):
	# 	print(numList[c])

	print('Average value was: ',sum(numList)/len(numList)) 
	#obtained average of ~0.4211

main()