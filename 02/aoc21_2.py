depth = 0
horizPos = 0

with open("input","r") as f:
	pos = f.readlines()

d = {
	'forward':[0,1],
	'down':[1,0],
	'up':[-1,0]
}
for p in pos:
	inst = p.split(" ")[0]
	num = int(p.split(" ")[1])
	depth += (num * d[inst][0])
	horizPos += (num * d[inst][1])

print(depth * horizPos)