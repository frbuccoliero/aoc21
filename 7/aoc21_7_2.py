with open("input") as i:
	crabsX = [int(x) for x in i.readline().split(",")]

def sumOfFirstN(n):
	return ((n+1)*n)//2

lowerDelta = len(crabsX) * sumOfFirstN(max(crabsX))
lowerDeltaPos = 0

for j in range(min(crabsX),max(crabsX)):
	delta = [sumOfFirstN(abs(x-j)) for x in crabsX]
	#print(f"{delta} -> sum: {sum(delta)}")
	if sum(delta) < lowerDelta:
		lowerDelta = sum(delta)
		lowerDeltaPos = j

#print(lowerDeltaPos)
print(lowerDelta)

