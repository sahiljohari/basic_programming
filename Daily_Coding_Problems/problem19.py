# A builder is looking to build a row of N houses that can be of K different colors. 
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, 
# return the minimum cost which achieves this goal.
import sys

def findMin(array):
    currMin = sys.maxsize

    for idx in range(len(array)):
        if array[idx] < currMin:
            currMin = array[idx]

    return array.index(currMin)

def minimumCost(arr):
    totalCost = 0
    startMin = findMin(arr[0])
    totalCost += arr[0][startMin]
    
    for row in range(1, len(arr)):
        arr[row][startMin] = sys.maxsize
        startMin = findMin(arr[row])
        totalCost += arr[row][startMin]

    return totalCost


def main():
    arr = [ [9,2,4,3,5],
            [6,1,2,3,8],
            [2,2,2,1,3],
            [3,1,1,4,5]
        ]

    print("Minimum Cost: %d" % (minimumCost(arr)))

if __name__ == "__main__":
    main()
