with open("input") as file:
	rows = file.readlines()

bigNum = 1000

def getCoords(coordsString):
	c1,c2 = coordsString.split(" -> ")
	c1 = [int(x) for x in c1.split(",")]
	c2 = [int(x) for x in c2.split(",")]
	return c1,c2

def step(xy1,xy2):
	if xy1 < xy2:
		return 1
	else:
		return -1

m = [([0]*bigNum) for i in range(bigNum)]

def getInbetweens(c1,c2):
	if(c1[0] == c2[0]):
		for i in range(min(c1[1],c2[1]),max(c1[1],c2[1])+1):
			m[c1[0]][i] += 1
	else:
		for i in range(min(c1[0],c2[0]),max(c1[0],c2[0])+1):
			m[i][c1[1]] += 1

for row in rows:
	c1,c2 = getCoords(row)
	if c1[0] == c2[0] or c1[1] == c2[1]:
		getInbetweens(c1,c2)

c=0
for i in range(bigNum):
	for j in range(bigNum):
		if m[i][j] > 1:
			c += 1

print(c)
