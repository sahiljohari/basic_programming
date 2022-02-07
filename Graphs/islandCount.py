'''
Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. 
The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.
'''

def island_count(grid):
    '''
    Time: O(r*c)
    Space: O(1)
    '''
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            count += hasIsland(grid, r, c)
        
    return count

def hasIsland(grid, r, c):
    row_inbounds = 0 <= r and r < len(grid)
    col_inbounds = 0 <= c and c < len(grid[0])
    
    if not row_inbounds or not col_inbounds: return False
    if grid[r][c] != 'L': return False

    grid[r][c] = '#'
    hasIsland(grid, r - 1, c)
    hasIsland(grid, r + 1, c)
    hasIsland(grid, r, c - 1)
    hasIsland(grid, r, c + 1)
    
    return True

def main():
    grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
    ]

    assert island_count(grid) == 3
    print("Test case 1 - passed")

    grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
    ]

    assert island_count(grid) == 4
    print("Test case 2 - passed")

    grid = [
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ]

    assert island_count(grid) == 1
    print("Test case 3 - passed")

    grid = [
    ['W', 'W'],
    ['W', 'W'],
    ['W', 'W'],
    ]

    assert island_count(grid) == 0
    print("Test case 4 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()