'''
Program to implement Sequential and Binary search
'''

class algo:
    def __init__(self):
        pass
    
    # Sequential search (when input array is sorted)
    def sequential_search(self, arr, val):
        pos = 0
        found = stop = False

        while pos < len(arr) and not found and not stop:
            if arr[pos] == val:
                found = True
            else:
                if arr[pos] > val:
                    stop = True
                else:
                    pos += 1

        return found

    # Binary search
    def binary_search(self, arr, val):
        if len(arr) == 0:
            return False
        else:
            mid = len(arr)//2
            if arr[mid] == val:
                return True
            else:
                if val < arr[mid]:
                    return self.binary_search(arr[:mid], val)
                else:
                    return self.binary_search(arr[mid+1:], val)


# Driver program
if __name__=='__main__':
    solver = algo()
    arr=[1,2,3,4,5,6,7,10,12]
    val = 10
    print('Using sequential search:',solver.sequential_search(arr, val))
    print('Using binary search:',solver.binary_search(arr, val))