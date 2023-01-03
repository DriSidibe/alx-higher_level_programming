#!/usr/bin/python3

import sys

class Queen:
	def __init__(self, row, column, grid_size):
		self.__row = row
		self.__column = column
		self.__grid_size = grid_size
		self.inner_cases_list = []

	@property
	def column(self):
		return self.__column

	@column.setter
	def column(self, column):
		if (type(column) is not int):
			raise TypeError("the column pos must be an int")
		if (column < 0 or column >= self.grid_size):
			raise TypeError("the column pos must be positive and < grid_size")
		self.move(self.__row, column)

	@property
	def row(self):
		return self.__row

	@row.setter
	def row(self, row):
		if (type(row) is not int):
			raise TypeError("the row pos must be an int")
		if (row < 0 or row >= self.grid_size):
			raise TypeError("the row pos must be positive and < grid_size")
		self.__row = row

	@property
	def grid_size(self):
		return self.__grid_size

	@grid_size.setter
	def grid_size(self, grid_size):
		raise TypeError("you can't reset the grid size")

	def move(self, row, column):
		update_inner_cases_list(row, column)
		self.__row = row
		self.__column = column

	def update_inner_cases_list(self, row, column):
		for i in range(len(self.inner_cases_list)):
			self.inner_case_list[i][0] += row - self.row
			self.inner_cases_list[i][1] += column - self.colum

	def is_out_of_bounde(self, i, j):
		if i < 0 or j < 0 or i >= self.grid_size or j >= self.grid_size:
			return True
		return False

	def add_diagonals(self):
		i = self.row
		j = self.column
		while not self.is_out_of_bounde(i, j):
			self.inner_cases_list.append((i, j))
			i -= 1
			j += 1
		i = self.row
		j = self.column
		while not self.is_out_of_bounde(i, j):
			self.inner_cases_list.append((i, j))
			i -= 1
			j += 1
		i = self.row
		j = self.column
		while not self.is_out_of_bounde(i, j):
			self.inner_cases_list.append((i, j))
			i -= 1
			j -= 1
		i = self.row
		j = self.column
		while not self.is_out_of_bounde(i, j):
			self.inner_cases_list.append((i, j))
			i += 1
			j += 1

	def init_inner_cases_list(self):
		for i in range(self.grid_size):
			self.inner_cases_list.append((i, self.column))
			self.inner_cases_list.append((self.row, i))
		self.add_diagonals()


class Nqueenproblem:
	def __init__(self, grid_size):
		self.grid_size = grid_size
		self.chess_board = [[[i, j] for j in range(int(grid_size))] for i in range(int(grid_size))]

	def solve(self):
		q1 = Queen(0, 0, self.grid_size)
		q1.init_inner_cases_list()
		print(q1.inner_cases_list)


if __name__ == "__main__":
	grid_size = int(sys.argv[1])
	nQProblem = Nqueenproblem(grid_size)
	for i in nQProblem.chess_board:
		print(i)
	nQProblem.solve()
