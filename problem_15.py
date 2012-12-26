#!/usr/bin/python

'''
Project Euler
Problem 15
http://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
'''

import sys


def create_grid(x, y):
	grid = []
	for i in range(0, x):
		row = []
		for j in range(0, y):
			node = {
				'up': None,
				'down': None,
				'left': None,
				'right': None,
				'location': (i, j),
				'touched': False,
				'known_paths': 0
			}
			if j > 0:
				node['left'] = row[j - 1]
				row[j - 1]['right'] = node
			if i > 0:
				node['up'] = grid[i - 1][j]
				grid[i - 1][j]['down'] = node

			row.append(node)
		grid.append(row)
	return grid


def print_grid(grid, verbose=False):
	node_str = '(%s, %s, %s)'
	for row in grid:
		row_str = ''
		for node in row:
			if verbose:
				row_str = row_str + ' ' + node_str % (node['location'][0], node['location'][1], node['touched'])
			else:
				if node['touched']:
					row_str = row_str + ' 1'
				else:
					row_str = row_str + ' 0'
		print row_str


def traverse_grid(grid, location, end, show_paths=False):
	node = grid[location[0]][location[1]]
	node['touched'] = True
	paths = 0
	if node['known_paths']:
		return node['known_paths']
	if node['location'] == end:
		if show_paths:
			print
			print_grid(grid, verbose=False)
			print
		paths = 1
	else:
		# if node['up'] and not node['up']['touched']:
		# 	paths += traverse_grid(grid, node['up']['location'], end, show_paths)

		if node['right'] and not node['right']['touched']:
			paths += traverse_grid(grid, node['right']['location'], end, show_paths)

		if node['down'] and not node['down']['touched']:
			paths += traverse_grid(grid, node['down']['location'], end, show_paths)

		# if node['left'] and not node['left']['touched']:
		# 	paths += traverse_grid(grid, node['left']['location'], end, show_paths)
	node['known_paths'] = paths
	node['touched'] = False
	return paths


def main():
    '''
    calculate the number of routes for a grid of size side_length x side_length
    '''
    grid = create_grid(21, 21)
    start = (0, 0)
    end = (20, 20)

    paths  = traverse_grid(grid, start, end, show_paths=False)
    print paths


if __name__ == '__main__':
    main()