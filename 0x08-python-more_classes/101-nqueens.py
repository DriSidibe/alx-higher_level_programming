#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
	print("Usage: nqueens N")
	exit(1)
try:
	if int(sys.argv[1]) < 4:
		print("N must be at least 4")
		exit(1)
except ValueError:
	print("N must be a number")
	exit(1)


class Nqueenproblem:
	"""  comment """
	def __init__(self):
		"""comment"""
		self.N = int(sys.argv[1])
		self.board = [[0 for i in range(self.N)] for j in range(self.N)]
		self.cursor = [0, 0]
		self.solutions = []
		self.is_running = True
		self.queen_count = 0
		self.is_found = False
		self.continue_finding = False
		self.recursion = False
		self.solution_count = 0
		self.i, self.j = 0, 0

	def set_cursor(self):
		"""comment"""
		if self.cursor[1] == self.N-1:
			self.cursor = [self.cursor[0]+1, 0]
		else:
			self.cursor[1] += 1

	def is_attacked(self):
		"""comment"""
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
		"""comment"""
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
		"""comment"""
		self.i, self.j = self.cursor[0], self.cursor[1]
		while self.is_in_frame(self.i+1, self.j+k):
			self.i += 1
			self.j += k
		return [self.i, self.j]

	def is_in_frame(self, i, j):
		"""comment"""
		if 0 <= i < self.N and 0 <= j < self.N:
			return True
		return False

	def solve(self):
		"""comment"""
		while self.is_running:
			self.recursion = False
			if self.is_attacked():
				if self.cursor == [self.N-1, self.N-1]:
					if self.board[0][self.N-1] == 1:
						exit()
				if self.cursor[1] == self.N-1:
					if self.cursor[0] == 0:
						exit()
					self.is_found = False
					self.continue_finding = False
					while not self.is_found:
						for i in range(self.N):
							if self.board[self.cursor[0]-1][i] == 1:
								if i == self.N-1:
									self.board[self.cursor[0]-1][i] = 0
									self.cursor = [self.cursor[0]-1, i]
									self.continue_finding = True
									break
								self.board[self.cursor[0]-1][i] = 0
								self.cursor = [self.cursor[0]-1, i+1]
								self.continue_finding = False
								self.recursion = True
								break
						if not self.continue_finding:
							self.is_found = True
				if not self.recursion:
					self.set_cursor()
			else:
				self.board[self.cursor[0]][self.cursor[1]] = 1
				if self.cursor[0] == self.N-1:
					self.solution_count += 1
					self.print_solutions([self.board])
					self.board[self.cursor[0]][self.cursor[1]] = 0
					if self.cursor[1] is not self.N-1:
						self.cursor[1] += 1
					else:
						self.cursor = [self.cursor[0]-1, self.board[self.cursor[0]-1].index(1)]
						self.board[self.cursor[0]][self.cursor[1]] = 0
						self.cursor[1] = self.cursor[1]+1
				else:
					self.cursor = [self.cursor[0]+1, 0]

	def print_solutions(self, solutions):
		"""comment"""
		solution = []
		for s in solutions:
			for i in range(self.N):
				for j in range(self.N):
					if s[i][j] == 1:
						solution.append([i, j])
		print(solution)


nqproblem = Nqueenproblem()
nqproblem.solve()
