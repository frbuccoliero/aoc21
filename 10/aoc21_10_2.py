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
	-4:1,
	-3:2,
	-2:3,
	-1:4
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


allValidScores = []

for line in lines:
	score = 0
	rev = line[::-1]
	# ugly af but who cares
	# to ignore the broken ones
	if -1 in rev or -2 in rev or -3 in rev or -4 in rev:
		pass
	else:
		for c in rev:
			score *= 5
			score += scores[-c]
		allValidScores.append(score)

allValidScores.sort()
print(allValidScores[len(allValidScores) // 2])









