with open("input") as i:
	digits = i.readlines()
	#cleanDigits = []
	count = 0
	for d in digits:
		# aL = d.split(" | ")[0].split(" ")
		fD = d.split(" | ")[1].split(" ")
		fD[-1] = fD[-1].replace("\n","")
		for d in fD:
			if len(d) in [2,3,4,7]:
				count += 1  
		'''
		cleanDigits.append({
			"availableLetters" : aL,
			"fourDigits" : fD
			})
		'''
print(count)

'''
Number of segments required by each digit
0 -> 6 
1 -> 2
2 -> 5
3 -> 5
4 -> 4
5 -> 5
6 -> 6
7 -> 3
8 -> 7
9 -> 6
'''