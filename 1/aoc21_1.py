with open("input","r") as f:
	i = f.readlines()

count = 0
for j in range(1,len(i)):
	if int(i[j]) > int(i[j-1]):
		count +=1

print(count)   