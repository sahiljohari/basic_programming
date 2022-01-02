import heapq

class Merge:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def merge_two(self, arr1, arr2):
        result = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        for i in range(i, len(arr1)):
            result.append(arr1[i])
        
        for i in range(j, len(arr2)):
            result.append(arr2[i])

        return result
    
    def merge_k(self, arr):
        k = len(arr)
        q = []
        result = []

        # construct a min-heap for the format (first value of kth array, index of kth array)
        for index in range(k):
            if arr[index]:
                heapq.heappush(q, (arr[index][0], index))

        current_index = 0
        while not q:
            value, list_index = heapq.heappop()
            result.append(value)
            list_index[current_index] += 1

            if list_index[current_index]:
                heapq.heappush(q, (arr[list_index][current_index], list_index))

        return result

def main():
    merge = Merge()
    arr1 = [2, 5, 8, 9]
    arr2 = [4, 6, 7, 10]
    
    print(merge.merge_two(arr1, arr2))

    arr = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(merge.merge_k(arr))

if __name__ == "__main__":
    main()