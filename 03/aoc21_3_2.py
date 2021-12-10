with open("input") as f:
	rows = f.readlines()
	f.close()

def mostAndLeastCommonBitInCol(rows,i):
	# len(rows[0]) returns 13 instead of 12 because of \n i guess
	ones = 0
	zeros = 0 
	for j in range(len(rows)):
		ones += (1 if rows[j][i] == "1" else 0)
		zeros += (1 if rows[j][i] == "0" else 0)
	if zeros > ones:
		return "0","1"
	else:
		return "1","0"

def applyRule(rows,ml):
	remaining = rows
	i = 0
	while len(remaining) > 1:
		m,l = mostAndLeastCommonBitInCol(remaining,i)
		print(m,l)
		temp = []
		mlc = m if ml == "m"  else l
		for n in remaining:
			if n[i] == mlc:
				temp.append(n)
		remaining = temp
		i += 1
	return remaining[0]

print(applyRule(rows,"m"),applyRule(rows,"l"))
