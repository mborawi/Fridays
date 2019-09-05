#!/usr/bin/env python3

import sys

filename = "./9x9Grid.dat"

size = 9

solutionsIncluded = 0

def printGrid(grid):
	print('\n'.join([''.join(['{:4}'.format(item) for item in row])
		for row in grid]))
	print('\n')

def findLeastSteepPath(grid, x, y, size):
	anythingSmaller = 0
	nextHighestValue = -sys.maxsize - 1
	if (x - 1) >= 0:
		if grid[x-1][y] > nextHighestValue and grid[x-1][y] < grid[x][y]:
			nextHighestValue = grid[x-1][y]
			nextX = (x - 1)
			nextY = y
			anythingSmaller = 1
	if (x + 1) < size:
		if grid[x+1][y] > nextHighestValue and grid[x+1][y] < grid[x][y]:
			nextHighestValue = grid[x+1][y]
			nextX = (x + 1)
			nextY = y
			anythingSmaller = 1
	if (y - 1) >= 0:
		if grid[x][y - 1] > nextHighestValue and grid[x][y - 1] < grid[x][y]:
			nextHighestValue = grid[x][y - 1]
			nextX = x
			nextY = (y - 1)
			anythingSmaller = 1
	if (y + 1) < size:
		if grid[x][y + 1] > nextHighestValue and grid[x][y + 1] < grid[x][y]:
			nextHighestValue = grid[x][y + 1]
			nextX = x
			nextY = (y + 1)
			anythingSmaller = 1
	if anythingSmaller == 0:
		return [grid[x][y]]
	return [grid[x][y]] + findLeastSteepPath(grid, nextX, nextY, size)

correct = 0

with open(filename) as file:
	for i, line in enumerate(file):
		if solutionsIncluded:
			lineSplit = line.split(":")
			solution = [int(i) for i in lineSplit[1].split(",")]
			gridSplit = [int(i) for i in lineSplit[0].split(",")]
		else:
			gridSplit = [int(i) for i in line.split(",")]
		grid = [gridSplit[i * size:(i + 1) * size] for i in range(size)]
		print(i + 1,".")
		printGrid(grid)
		path = findLeastSteepPath(grid, size // 2, size // 2, size)
		if solutionsIncluded:
			print(solution)
			if path == solution:
				correct += 1
		print(path, '\n')

if solutionsIncluded:
	print("Total correct:", correct)