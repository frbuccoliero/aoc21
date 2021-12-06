with open("input") as f:
	rows = f.readlines()
	f.close()

gamma = ""
epsilon = ""

# len(rows[0]) returns 13 instead of 12 because of \n i guess
for i in range(len(rows[0])-1):
	ones = 0
	zeros = 0 
	for j in range(len(rows)):
		ones += (1 if rows[j][i] == "1" else 0)
		zeros += (1 if rows[j][i] == "0" else 0)
	if zeros > ones:
		gamma += "0"
		epsilon += "1"
	else:
		gamma +="1"
		epsilon +="0"

print(gamma,epsilon)