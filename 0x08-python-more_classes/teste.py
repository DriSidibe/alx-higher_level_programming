import sys

N = int(sys.argv[1])
board = [[0 for i in range(N)] for j in range(N)]
cursor = [0, 0]
solutions = []
is_running = True
queen_count = 0
i, j = 0, 0

def set_cursor(board):
	global cursor
	if cursor[1] == N-1:
		cursor = [cursor[0]+1, 0]
	else:
		cursor[1] += 1

def is_attacked(cursor):
	global queen_count
	board[cursor[0]][cursor[1]] = 0
	for i in range(N):
		if board[i][cursor[1]] == 1:
			queen_count += 1
		if board[cursor[0]][i] == 1:
			queen_count += 1
		if queen_count > 1:
			return True
	test_diagos()
	board[cursor[0]][cursor[1]] = 1
	if queen_count > 1:
		return True
	return False

def test_diagos():
	global queen_count
	l, m = get_diago(-1)
	while is_in_frame(l-1, m+1):
		l -= 1
		m += 1
		if board[l][m] == 1:
			queen_count += 1
	l, m = get_diago(1)
	while is_in_frame(l, m):
		if board[l][m] == 1:
			queen_count += 1
		l -= 1
		m -= 1

def get_diago(k):
	global i, j
	i, j = cursor[0], cursor[1]
	while is_in_frame(i+1, j+k):
		i += 1
		j += k
	return [i, j]

def is_in_frame(i, j):
	if 0 <= i < N and 0 <= j < N:
		return True
	return False

def solve(board):
	global cursor
	while is_running:
		if is_attacked(cursor):
			set_cursor(board)
		else:
			board[cursor[0]][cursor[1]] = 1
			if cursor[0] == N-1:
				break
			cursor = [cursor[0]+1, 0]
	print_solutions(solutions)

def print_solutions(solutions):
	for s in solutions:
		for i in range(N):
			for j in range(N):
				print(s[i][j], end=" ")
			print("")
		print("-----------------")

solve(board)
