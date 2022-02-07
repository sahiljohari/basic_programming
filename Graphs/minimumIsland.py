'''
Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. 
The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.
'''

def minimum_island(grid):
    '''
    Time: O(r*c)
    Space: O(1)
    '''
    rows, cols = len(grid), len(grid[0])
    min_size = float('inf')

    for r in range(rows):
        for c in range(cols):
            size = island_size(grid, r, c)
            if size > 0:
                min_size = min(size, min_size)

    return min_size

def island_size(grid, r, c):
    row_inbounds = 0 <= r and r < len(grid)
    col_inbounds = 0 <= c and c < len(grid[0])

    if not row_inbounds or not col_inbounds: return 0
    if grid[r][c] != 'L': return 0

    grid[r][c] = '#'
    
    size = 1
    size += island_size(grid, r - 1, c)
    size += island_size(grid, r + 1, c)
    size += island_size(grid, r, c - 1)
    size += island_size(grid, r, c + 1)

    return size

def main():
    grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
    ]

    assert minimum_island(grid) == 2
    print("Test case 1 - passed")

    grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
    ]

    assert minimum_island(grid) == 1
    print("Test case 2 - passed")

    grid = [
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ]

    assert minimum_island(grid) == 9
    print("Test case 3 - passed")

    grid = [
    ['W', 'W'],
    ['L', 'L'],
    ['W', 'W'],
    ['W', 'L']
    ]

    assert minimum_island(grid) == 1
    print("Test case 4 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()