import random as r
############################################
def concat(multDigit,flag):

	oneDigit = makeRandomNum()

	if len(multDigit) == 0:
		multDigit.append(oneDigit)
		# print('len0',multDigit)
		return multDigit, flag

	elif multDigit[len(multDigit)-1] >= oneDigit:
		multDigit.append(oneDigit)
		# print(multDigit)
		return multDigit, flag

	else:
		flag = 1
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
	
	for j in range(len(numList)):
		num = int(''.join(map(str,numList[j])))
		exponent = len(numList[j])
		numList[j] = num/(10**exponent)

	# for c in range(len(numList)):
	# 	print(numList[c])
	print(sum(numList)/len(numList)) #obtained average of ~0.4155

main()