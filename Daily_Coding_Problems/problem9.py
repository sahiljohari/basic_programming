# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

def maxSum(arr):
    prevMax, currMax = 0, 0

    for num in arr:
        currMax, prevMax = max((prevMax + num), currMax), currMax
    
    return currMax
    
if __name__ == "__main__":
    arr1 = [2, 4, 6, 2, 5]
    arr2 = [3, 2, 1]
    arr3 = [3, 4, -1, 1]
    arr4 = [-1, -2, -3]
    arr5 = [1, 2, 0]
    arr6 = [5, -4, -1, -2, 1]
    arr7 = [5, 1, 1, 5]
    
    testCases = [arr1, arr2, arr3, arr4, arr5, arr6, arr7]
    
    for test in testCases:
        print("Test-Case:%s Output: %d" % (test, maxSum(test)))