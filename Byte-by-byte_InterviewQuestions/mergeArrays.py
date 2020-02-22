# Given 2 sorted arrays A and B, where A is long enough to hold elements of both A and B
# write a function to merge them without using any additional storage/memory.
# For example, merge([1,3,5,0,0,0], [2,4,6]) = [1,2,3,4,5,6]

def merge(A, B):
    '''
    Time complexity: O(max(A,B)), where A and B are the lengths of arrays A and B
    Space complexity: O(1)
    '''
    i, j, k = len(A) - len(B) - 1, len(B) - 1, len(A) - 1
    
    while i >=0 and j >= 0:
        if B[j] >= A[i]:
            A[k] = B[j]
            j -= 1
        else:
            A[k] = A[i]
            i -= 1
        k -= 1

    return A

def main():
    assert merge([1, 3, 5, 0, 0, 0], [2, 4, 6]) == [1, 2, 3, 4, 5, 6], "Test case failure"
    assert merge([1, 3, 5, 0, 0, 0], [1, 3, 5]) == [1, 1, 3, 3, 5, 5], "Test case failure"
    assert merge([1, 3, 5, 0, 0, 0], [1, 1, 1]) == [1, 1, 1, 1, 3, 5], "Test case failure"
    assert merge([0, 3, 5, 0, 0, 0], [1, 1, 1]) == [0, 1, 1, 1, 3, 5], "Test case failure"
    assert merge([0, 0, 0, 0, 0, 0], [1, 1, 1]) == [0, 0, 0, 1, 1, 1], "Test case failure"
    assert merge([1, 3, 5, 6, 0, 0, 0], [2, 4, 6]) == [1, 2, 3, 4, 5, 6, 6], "Test case failure"
    
    print("All test cases passed.")

if __name__ == "__main__":
    main()