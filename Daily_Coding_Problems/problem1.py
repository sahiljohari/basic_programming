# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def two_sum_1(arr, k):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(k-arr[i]) == arr[j]:
                return True
            
    return False

def two_sum_2(arr, k):
    for i in arr:
            if abs(k-i) in arr:
                return True
    return False

if __name__ == "__main__":
    arr = [-1, 19]
    k = 18
    
    print("Output using first approach:",two_sum_1(arr, k))
    print("Output using second approach:",two_sum_2(arr, k))