with open("input") as i:
	digits = i.readlines()
	cleanDigits = []
	count = 0
	for d in digits:
		aL = d.split(" | ")[0].split(" ")
		aL.sort(key=len)
		fD = d.split(" | ")[1].split(" ")
		fD[-1] = fD[-1].replace("\n","")
		cleanDigits.append({
			"availableLetters" : aL,
			"fourDigits" : fD
			})

'''
Number of segments required by each digit
0 : 6 
1 : 2 unique
2 : 5
3 : 5
4 : 4 unique
5 : 5
6 : 6
7 : 3 unique 
8 : 7 unique
9 : 6
'''

# We have to figure out the layout so 
# we focus on the digits with unique number
# of segments

'''
Positions in the posArray
  0
1   2
  3
4   5
  6

'''

numToArr = {
0 : [0,1,2,4,5,6],
2 : [0,2,3,4,6],
3 : [0,2,3,5,6],
5 : [0,1,3,5,6],
6 : [0,1,3,4,5,6],
9 : [0,1,2,3,5,6],
}

outputCount = 0

for cD in cleanDigits:
	allPossiblePosArrays = []
	posArray = ['']*7

	outputArr = [0]*4
	for ind,d in enumerate(cD['fourDigits']):
		if len(d) in [2,3,4,7]:
			if len(d) == 2:
				outputArr[ind] = 1
				
			if len(d) == 3:
				outputArr[ind] = 7
				
			if len(d) == 4:
				outputArr[ind] = 4
				
			if len(d) == 7:
				outputArr[ind] = 8
			cD['fourDigits'][ind] = ''




	# CHANGE APPROACH -> FIND NUMBERS WITH SAME LENGTH AND FIND THE DIFF.
	sixes = [x for x in cD["availableLetters"] if len(x) == 6]
	# 0 or 6 or 9
	# these 3 have in common 0156
	missingInSixes = "" #234
	for l in sixes[0]:
		if l not in sixes[1] or l not in sixes[2]:
			if l not in missingInSixes:
				missingInSixes += l
	for l in sixes[1]:
		if l not in sixes[0] or l not in sixes[2]:
			if l not in missingInSixes:
				missingInSixes += l
	for l in sixes[2]:
		if l not in sixes[0] or l not in sixes[1]:
			if l not in missingInSixes:
				missingInSixes += l

	# cbdgef fgaecd agebfd

	#these two letters in missingInSixes are either in 45 or 54 pos
	fives = [x for x in cD["availableLetters"] if len(x) == 5]
	# 2 or 3 or 5
	# have in common 036
	
	missingInFives = "" #1245
	for l in fives[0]:
		if l not in fives[1] or l not in fives[2]:
			if l not in missingInFives:
				missingInFives += l
	for l in fives[1]:
		if l not in fives[0] or l not in fives[2]:
			if l not in missingInFives:
				missingInFives += l
	for l in fives[2]:
		if l not in fives[0] or l not in fives[1]:
			if l not in missingInFives:
				missingInFives += l

	# fdcge fecdb fabcd

	one = [x for x in cD["availableLetters"] if len(x) == 2][0] #25
	four = [x for x in cD["availableLetters"] if len(x) == 4][0] #1235
	seven = [x for x in cD["availableLetters"] if len(x) == 3][0] #025
	eight = [x for x in cD["availableLetters"] if len(x) == 7][0] #0123456


	print(missingInSixes,missingInFives,one,four,seven,eight)

	## Now we need to make intersections
	for s in seven:
		if s not in one:
			posArray[0] = s

	for s in missingInSixes:
		if s in one:
			posArray[2] = s

	for s in eight:
		if s not in four+seven+missingInFives:
			posArray[6] = s

	for s in missingInFives:
		mis = missingInSixes
		mis = mis.replace(posArray[2],'')
		if s in mis:
			posArray[4] = s

	posArray[5] = one
	posArray[5] = posArray[5].replace(posArray[2],'')

	posArray[3] = missingInSixes
	posArray[3] = posArray[3].replace(posArray[2],'')
	posArray[3] = posArray[3].replace(posArray[4],'')

	for s in four:
		if s not in one + posArray[3]:
			posArray[1] = s
	
	for ind,d in enumerate(cD['fourDigits']):
		if d != "":
			posLetterArray = []
			for l in d:
				posLetterArray.append(posArray.index(l))
			posLetterArray.sort()
			for key, numArr in numToArr.items():
				if posLetterArray == numArr:
					outputArr[ind] = key

	num = (outputArr[3] + (outputArr[2]*10) + (outputArr[1]*100) + (outputArr[0]*1000))
	print(f"{outputArr} -> {num}" )
	outputCount += num

print(outputCount)






















