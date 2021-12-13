folds = []
dots = []

# for clarity since the matrix is going to be
# an array of arrays (rows)
# we will use the notation [y,x]

with open('input') as inp:
	lines = inp.readlines()
	for l in lines:
		if "fold" in l:
			rsp = l.split(" ")[2].split("=")
			coord = rsp[0]
			val = int(rsp[1])
			if coord == "x":
				folds.append([0,val])
			else:
				folds.append([val,0])
		elif ',' in l:
			values = l.split(',')
			dots.append([int(values[1]),int(values[0])])

maxx = max([x[1] for x in dots])+1
maxy = max([x[0] for x in dots])+1

m = [([0]*maxx) for i in range(maxy)]

for dot in dots:
	m[dot[0]][dot[1]] = 1

for fold in folds:
	foldsOverY = (fold[0] != 0)
	val = fold[0] if foldsOverY else fold[1]
	maxval = maxy if foldsOverY else maxx
	for j in range(val,maxval):
		oppPos = val-(j-val)
		if foldsOverY:
			for x in range(maxx):
				if m[oppPos][x] == 0:
					if m[j][x] == 1:
						m[oppPos][x] = 1
				m[j][x] = 0
		else:
			for y in range(maxy):
				if m[y][oppPos] == 0:
					if m[y][j] == 1:
						m[y][oppPos] = 1
				m[y][j] = 0
		break

cont = 0
for r in m:
	cont += r.count(1)
print(cont)
