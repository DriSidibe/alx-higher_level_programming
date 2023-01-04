import sys

class Nqueenproblem:
	def __init__(self):
		self.N = int(sys.argv[1])
		self.board = [[0 for i in range(self.N)] for j in range(self.N)]
		self.cursor = [0, 0]
		self.solutions = []
		self.is_running = True
		self.queen_count = 0
		self.i, self.j = 0, 0

	def set_cursor(self):
		if self.cursor[1] == self.N-1:
			self.cursor = [self.cursor[0]+1, 0]
		else:
			self.cursor[1] += 1

	def is_attacked(self):
		self.queen_count = 0
		for i in range(self.N):
			if self.board[i][self.cursor[1]] == 1 or self.board[self.cursor[0]][i] == 1:
				self.queen_count += 1
			if self.queen_count >= 1:
				return True
		self.test_diagos()
		if self.queen_count >= 1:
			return True
		return False

	def test_diagos(self):
		l, m = self.get_diago(-1)
		while self.is_in_frame(l-1, m+1):
			l -= 1
			m += 1
			if self.board[l][m] == 1:
				self.queen_count += 1
		l, m = self.get_diago(1)
		while self.is_in_frame(l, m):
			if self.board[l][m] == 1:
				self.queen_count += 1
			l -= 1
			m -= 1

	def get_diago(self, k):
		self.i, self.j = self.cursor[0], self.cursor[1]
		while self.is_in_frame(self.i+1, self.j+k):
			self.i += 1
			self.j += k
		return [self.i, self.j]

	def is_in_frame(self, i, j):
		if 0 <= i < self.N and 0 <= j < self.N:
			return True
		return False

	def back(self):
		if self.cursor[1] == self.N-1:
			if self.cursor[0] == 0:
				print("can't solve")
				self.print_solutions(self.solutions)
				exit()
			self.find_new()

	def find_new(self):
		for i in range(self.N):
			if self.board[self.cursor[0]-1][i] == 1:
				if i == self.N-1:
					self.board[self.cursor[0]-1][i] = 0
					self.cursor = [self.cursor[0]-1, i]
					self.find_new()
				self.board[self.cursor[0]-1][i] = 0
				self.cursor = [self.cursor[0]-1, i+1]
				self.solve()

	def solve(self):
		while self.is_running:
			if self.is_attacked():
				self.back()
				self.set_cursor()
			else:
				self.board[self.cursor[0]][self.cursor[1]] = 1
				if self.cursor[0] == self.N-1:
					self.solutions.append(self.board)
					break
				self.cursor = [self.cursor[0]+1, 0]
		self.print_solutions(self.solutions)

	def print_solutions(self, solutions):
		for s in solutions:
			for i in range(self.N):
				for j in range(self.N):
					print(s[i][j], end=" ")
				print("")
			print("-----------------")

nqproblem = Nqueenproblem()
nqproblem.solve()
