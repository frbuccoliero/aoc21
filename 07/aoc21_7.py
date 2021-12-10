with open("input") as i:
	crabsX = [int(x) for x in i.readline().split(",")]

lowerDelta = len(crabsX) * max(crabsX)

for j in range(min(crabsX),max(crabsX)):
	delta = [abs(x-j) for x in crabsY]
	if sum(delta) < lowerDelta:
		lowerDelta = sum(delta)

print(lowerDelta)

