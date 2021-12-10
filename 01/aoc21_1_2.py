with open("input","r") as f:
	i = f.readlines()

prev = 0
count = -1

l = len(i)
for j in range(l):
	s = int(i[j+1]) if j+1 <= l-1 else 0
	t = int(i[j+2]) if j+2 <= l-1 else 0
	slidingDoorsSum = int(i[j]) + s + t 
	if slidingDoorsSum > prev:
		count +=1
	prev = slidingDoorsSum


print(count)   
