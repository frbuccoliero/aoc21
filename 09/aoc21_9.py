with open("input") as i:
	dirtyRows = i.readlines()
	rows = []
	for r in dirtyRows:
		row = []
		# :-1 to ignore \n at last 
		for c in r[:-1]:
			row.append(int(c))
		rows.append(row) 

cont = 0
print((rows[-1]))

for i in range(len(rows)):
	for j in range(len(rows[0])):
		# if adjacent cell exists assign
		# else assign 10 so it's always satisfied
		if i>0:	
			top = rows[i-1][j]
		else:
			top = 10
		if i<(len(rows)-1):
			bottom = rows[i+1][j]
		else:
			bottom = 10
		if j>0:
			left = rows[i][j-1]
		else:
			left = 10
		if j<(len(rows[0])-1):
			right = rows[i][j+1]
		else:
			right = 10

		if rows[i][j] < top and rows[i][j] < bottom and rows[i][j] < left and rows[i][j] < right:
			print(rows[i][j])
			cont += ((rows[i][j]) +1)
print(cont)