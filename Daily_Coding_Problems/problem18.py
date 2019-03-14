# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)

# **TO-DO** : Do this in O(n) time and O(k) space. 
# You can modify the input array in-place and you do not need to store the results. 
# You can simply print them out as you compute them.

def maxSubArray(arr, k):
    if len(arr) < k:
        print("Size of array cannot be less than k...", end="")
    else:
        for i in range(0, len(arr)-k+1):
            print(max(arr[i:i+k]), end=" ")

def main():
    arr1 = [[2, 4, 6, 2, 5], 3]
    arr2 = [[3, 2, 1], 2]
    arr3 = [[3, 4, -1, 1], 2]
    arr4 = [[-1, -2, -3], 2]
    arr5 = [[1, 2, 0], 6]
    arr6 = [[5, -4, -1, -2, 1], 3]
    arr7 = [[5, 1, 1, 5], 3]
    arr8 = [[10, 5, 2, 7, 8, 7], 3]
    
    testCases = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8]
    
    for test in testCases:
        maxSubArray(test[0], test[1])
        print("")

if __name__ == "__main__":
    main()