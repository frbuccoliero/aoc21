with open("input") as inp:
	rows = inp.readlines()
	octo = []
	for r in rows:
		row = []
		for o in r[:-1]:
			row.append(int(o))
		octo.append(row)

steps = 100
l = len(octo)

flashCount = 0

def getAdj(i,j):
	if i>0:	
		top = [i-1,j]
		if j>0:
			topleft = [i-1,j-1]
		else:
			topleft = []
		if j<(l-1):
			topright = [i-1,j+1]
		else:
			topright = []
	else:
		top = []
		topleft = []
		topright = []

	if i<(l-1):
		bottom = [i+1,j]
		if j>0:
			bottomleft = [i+1,j-1]
		else:
			bottomleft = []
		if j<(l-1):
			bottomright = [i+1,j+1]
		else:
			bottomright = []
	else:
		bottom = []
		bottomleft = []
		bottomright = []


	if j>0:
		left = [i,j-1]
	else:
		left = []
	if j<(l-1):
		right = [i,j+1]
	else:
		right = []

	return [top,left,bottom,right,topleft,topright,bottomleft,bottomright]

def addEnergy(i,j):
	octo[i][j] += 1

def updateMatrix():
	count = 0
	forcedZeros = []
	while True:
		newFlashes = False
		for i in range(l):
			for j in range(l):
				if octo[i][j] > 9:
					forcedZeros.append([i,j])
					newFlashes = True
					count += 1
					if [i,j] in forcedZeros:
						diff = 0
					else:
						diff = 10 - octo[i][j]
					octo[i][j] = diff 
					for adj in getAdj(i,j):
						if adj != [] and adj not in forcedZeros:
							addEnergy(adj[0],adj[1])
		if not newFlashes:
			break
	return count 


for s in range(steps):
	for i in range(l):
		for j in range(l):
			addEnergy(i,j)
	flashCount += updateMatrix()

print(flashCount)