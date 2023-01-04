import sys

N = int(sys.argv[1])
solutions = []

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print (board[i][j],end=' ')
        print()

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQUtil(board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False

def searchSolution(board):
	if solveNQUtil(board, 0) == False:
		print ("Solution does not exist")
		return False

def solveNQ():
	board = []
	for i in range(N):
		l = []
		for j in range(N):
			l.append(0)
		board.append(l)
	while board[0][-1] == 0 and board[-1][-1] == 0:
		if searchSolution(board) != False:
			solutions.append(board)
			"""
			for i in range(N):
				if i == N-1:
					return True
				if board[-1][i] == 1:
					board[-1][i] = 0
					board[-1][i+1] = 1"""
	return True

solveNQ()
for solution in solutions:
	printSolution(solution)
