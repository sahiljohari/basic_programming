# Asked in an online assessment
# Find the minimum number of steps to reach an obstable (represented as 9) from the top-left corner
def removeObstacle(numRows, numColumns, lot):
    target_x = 0
    target_y = 0
    # find the coordinates of the target obstacle first
    for i in range(numRows):
        for j in range(numColumns):
            if lot[i][j] == 9:
                target_x = i
                target_y = j
    
    # track the path in a separate 2D array
    visited = [[0 for j in range(numColumns)] for i in range(numRows)]
    
    # starting with the maximum possible distance
    max_distance = numRows * numColumns + 1
    # get the minimum distance to reach the target obstacle
    min_distance = removeObstacleUtil(numRows, numColumns, lot, visited, 0, 0, target_x, target_y, max_distance, 0)
    print(min_distance)
    # if obstacle found
    if min_distance != max_distance:
        return min_distance
    return -1
    
def removeObstacleUtil(numRows, numColumns, lot, visited, x, y, i, j, min_distance, distance):
    # if the obstacle target is reached
    if i == x and j == y:
        return min(distance, min_distance)
    # mark the current position as visited  
    visited[x][y] = 1
    
    # move down
    if isValid(x, y+1, numRows, numColumns) and isSafe(lot, visited, x, y+1):
        min_distance = removeObstacleUtil(numRows, numColumns, lot, visited, x, y+1, i, j, min_distance, distance+1)
    # move right    
    if isValid(x+1, y, numRows, numColumns) and isSafe(lot, visited, x+1, y):
        min_distance = removeObstacleUtil(numRows, numColumns, lot, visited, x+1, y, i, j, min_distance, distance+1)
    # move left   
    if isValid(x-1, y, numRows, numColumns) and isSafe(lot, visited, x-1, y):
        min_distance = removeObstacleUtil(numRows, numColumns, lot, visited, x-1, y, i, j, min_distance, distance+1)
    # move up     
    if isValid(x, y-1, numRows, numColumns) and isSafe(lot, visited, x, y-1):
        min_distance = removeObstacleUtil(numRows, numColumns, lot, visited, x, y-1, i, j, min_distance, distance+1)

    visited[x][y] = 0
    return min_distance
    
def isSafe(lot, visited, x, y):
    return not(lot[x][y] == 0 or visited[x][y] != 0)
    
def isValid(x, y, numRows, numColumns):
    return x < numRows and y < numColumns and x >= 0 and y >= 0

def main():
    lot = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 9, 1]
    ]

    print(removeObstacle(3, 3, lot))

main()