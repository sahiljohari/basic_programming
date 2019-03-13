# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.
import sys

def firstMissing(arr):
    minNum = sys.maxsize
    for num in arr:
        if num >= 0 and num < minNum:
            minNum = num
    if minNum == sys.maxsize:
        minNum = -1
        
    if minNum == 0 or minNum == 1:
        while minNum in arr:
            minNum += 1
        return minNum
    elif minNum > 1:
        while minNum in arr or minNum > 1:
            minNum -= 1
        return minNum
    else:
        return 1
    
    
if __name__ == "__main__":
    arr1 = [2, 4, 6, 8]
    arr2 = [3, 2, 1]
    arr3 = [3, 4, -1, 1]
    arr4 = [-1, -2, -3]
    arr5 = [1, 2, 0]
    arr6 = [5, -4, -1, -2, 1]
    arr7 = [0, 0, 0, 0, 0]
    
    testCases = [arr1, arr2, arr3, arr4, arr5, arr6, arr7]
    
    for test in testCases:
        print("Test-Case:%s Output: %d" % (test, firstMissing(test)))