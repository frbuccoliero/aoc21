depth = 0
horizPos = 0
aim = 0

with open("input","r") as f:
	pos = f.readlines()

d = {
	# [D, H , A]
	'forward':[1,1,0],
	'down':[0,0,1],
	'up':[0,0,-1]
}
for p in pos:
	inst = p.split(" ")[0]
	num = int(p.split(" ")[1])
	aim += (num * d[inst][2])
	horizPos += (num * d[inst][1])
	depth += (num * aim * d[inst][0])	

print(depth*horizPos)