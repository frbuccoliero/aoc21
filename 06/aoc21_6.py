days = 80

with open("input") as i:
	fish = i.readline().split(",")
	fish[-1] = fish[-1].split("\n")[0]
	for i in range(len(fish)):
		fish[i] = int(fish[i])

	fishes = {
		"0":sum(map(lambda x : x == 0, fish)),
		"1":sum(map(lambda x : x == 1, fish)),
		"2":sum(map(lambda x : x == 2, fish)),
		"3":sum(map(lambda x : x == 3, fish)),
		"4":sum(map(lambda x : x == 4, fish)),
		"5":sum(map(lambda x : x == 5, fish)),
		"6":sum(map(lambda x : x == 6, fish)),
		"7":sum(map(lambda x : x == 7, fish)),
		"8":sum(map(lambda x : x == 8, fish)),
	}

for d in range(days):
	toMultiply = fishes['0']
	for i in range(8):
		fishes[str(i)] = fishes[str(i+1)]
	fishes['8'] = toMultiply
	fishes['6'] += toMultiply

print(sum(list(fishes.values())))