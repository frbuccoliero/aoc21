import re
lines = 5

def getNumsBoards():
	with open("input") as f:
		file = f.readlines()
	nums = [int(x) for x in file[0].split(",")]

	boards = []
	for j in range(0,(len(file)-1)//(lines+1)):
		board = []
		for k in range(lines):
			board.append([int(x) for x in re.findall(r'([0-9]+)',file[2 + j*6 + k])])
		boards.append(board)
	return nums,boards

def winningRow(board,nums):
	for row in board:
		w = lines	
		for num in row:
			if num not in nums:
				w -= 1
		if w == lines:
			return True
	return False

def winningCol(board,nums):
	for j in range(lines):
		w = lines
		for num in [x[j] for x in board]:
			if num not in nums:
				w -= 1
		if w == lines:
			return True
	return False

def checkRemaining(board,nums,last):
	totalRemaining = 0
	for row in board:
		for num in row:
			if num not in nums:
				totalRemaining += num
	print(totalRemaining*last)

nums,boards = getNumsBoards()
winningNums = []
for n in nums:
	winningNums.append(n)
	for board in boards:
		if winningCol(board,winningNums) or winningRow(board,winningNums):
			print(board,winningNums)
			checkRemaining(board,winningNums,n)
			exit()
