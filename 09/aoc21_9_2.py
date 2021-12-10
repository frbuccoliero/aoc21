with open("input") as i:
	dirtyRows = i.readlines()
	rows = []
	for r in dirtyRows:
		row = []
		for c in r:
			try:
				row.append(int(c))
			except:
				pass
		rows.append(row) 

def getAdj(i,j):
	if i>0:	
		top = rows[i-1][j]
	else:
		top = 10
	if i<((len(rows)-1)):
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
	return top,left,bottom,right


def getBasin(i,j,comesFrom,basin):
	if [i,j] not in basin:
		tlbr = []
		for a in getAdj(i,j):
			tlbr.append(a)
		adjs = [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]

		if comesFrom != -100:
			tlbr[comesFrom] = 10
			adjs[comesFrom] = [-100,-100]

		toRem = []

		for t in range(len(tlbr)):
			if tlbr[t] in [9,10]:
				toRem.append(t)

		for tr in toRem:
			tlbr[tr] = 10
			adjs[tr] = [-100,-100]

		#print(f"[{i},{j}] (val={rows[i][j]}) -> Adjs: {adjs}")

		if rows[i][j] not in [9,10]:
			basin.append([i,j])
		else:
			return basin

		for adj in adjs:
			if adj != [-100,-100]:
				new = getBasin(adj[0],adj[1],adjs.index(adj)-2,basin)
				for n in new:
					if n not in basin:
						basin.append(n)
		return basin
	else:
		return []
			

basins = []
for i in range(len(rows)):
	for j in range(len(rows[0])):
		top,left,bottom,right = getAdj(i,j)
		if rows[i][j] < top and rows[i][j] < bottom and rows[i][j] < left and rows[i][j] < right:
			#print (f"i:{i},j:{j} , val -> {rows[i][j]} tlbr:{top} {left} {bottom} {right}")
			basin = getBasin(i,j,-100,[])
			basins.append(basin)

basins.sort(key=len)
basins = basins[-3:]
print(len(basins[0]) * len(basins[1]) * len(basins[2]))