def removeOC(l):
	while "()" in l or "[]" in l or "{}" in l or "<>" in l:
		l = l.replace("()","")
		l = l.replace("[]","")
		l = l.replace("{}","")
		l = l.replace("<>","")
	return l

d = {
	'<' : 1,
	'{' : 2,
	'[' : 3,
	'(' : 4,
	'>' : -1,
	'}' : -2,
	']' : -3,
	')' : -4
}

scores = {
	-4:3,
	-3:57,
	-2:1197,
	-1:25137
}

with open("input") as i:
	lines = []
	for l in i.readlines():
		line = []
		l = removeOC(l)
		# :-1 to remove \n
		for c in l[:-1]:
			line.append(d[c])
		lines.append(line)

count = 0
for line in lines:
	for n in line:
		if n<0:
			print(n)
			count += scores[n]	
			break

print(count)









