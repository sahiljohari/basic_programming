
def get_median(arr):
    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2
        
    else:
        return arr[mid]

def median(arr1, arr2):
    '''
    Time complexity: O(log n)
    Space complexity: O(1)
    '''
    if len(arr1) == 1:
        return get_median(arr1, arr2[:1])
    
    if len(arr1) == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[-1], arr2[-1])) / 2

    median1 = get_median(arr1)
    median2 = get_median(arr2)

    if median1 == median2:
        return median1

    if median1 > median2:
        return median(arr1[:(len(arr1) // 2) + 1], arr2[(len(arr2) -1) // 2:])
    else:
        return median(arr1[(len(arr1) -1) // 2:], arr2[:(len(arr2) // 2) + 1])

def main():
    assert median([1, 3, 5], [2, 4, 6]) == 3.5, "Test case failure"
    assert median([1, 2, 4, 8, 9], [3, 6, 7, 10, 12]) == 6.5, "Test case failure"
    
    print("All test cases passed.")

if __name__ == "__main__":
    main()