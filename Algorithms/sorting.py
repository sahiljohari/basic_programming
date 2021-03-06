'''
Implement fundamental sorting algorithms
'''

class sort:
    def __init__(self):
        pass
    
    # Bubble sort
    def bubble_sort(self, arr):
        for passnum in range(len(arr)-1, 0, -1):
            for i in range(passnum):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]

        return arr

    # Short bubble sort
    def short_bubble_sort(self, arr):
        exchanges = True
        passnum = len(arr)-1

        while passnum > 0 and exchanges:
            exchanges = False
            for i in range(passnum):
                if arr[i] > arr[i+1]:
                    exchanges = True
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            passnum -= 1
        return arr

    # Selection sort
    def selection_sort(self, arr):
        for i in range(len(arr)):
            position_min = i
            for j in range(i+1, len(arr)):
                if arr[position_min] > arr[j]:
                    position_min = j

            arr[i], arr[position_min] = arr[position_min], arr[i]

        return arr

    # Insertion sort
    def insertion_sort(self, arr):
        for idx in range(1, len(arr)):
            current_val = arr[idx]
            pos = idx
            while pos > 0 and arr[pos-1] > current_val:
                arr[pos] = arr[pos-1]
                pos -= 1
            arr[pos] = current_val

        return arr

    # Merge sort
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return arr

    # Quick sort
    def quick_sort(self, arr):
        self.quick_sort_helper(arr, 0, len(arr)-1)
        
    def quick_sort_helper(self, arr, first, last):
        if first < last:
            split_point = self.partition(arr, first, last)
            self.quick_sort_helper(arr, first, split_point-1)
            self.quick_sort_helper(arr, split_point+1, last)

    def partition(self, arr, first, last):
        pivot = arr[first]
        left_mark = first+1
        right_mark = last

        done = False
        while not done:
            while left_mark <= right_mark and arr[left_mark] <= pivot:
                left_mark += 1
            while right_mark >= left_mark and arr[right_mark] >= pivot:
                right_mark -= 1
            if right_mark < left_mark:
                done = True
            else:
                arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]
            
        arr[first], arr[right_mark] = arr[right_mark], arr[first]

        return right_mark

if __name__=='__main__':
    s = sort()
    arr = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
    arr1 = [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
    # print(s.merge_sort(arr1))
    s.quick_sort(arr1)
    print(arr1)