# Given an array of integers, return a new array such that each element at 
# index i of the new array is the product of all the numbers in the original 
# array except the one at i.

# TO-DO: Implement without using division

def product_rest_1(arr):
    out_arr = []
    total_prod = 1
    
    # Compute the product of all the elements in the array
    for i in arr:
        total_prod *= i
        
    # Divide each element by the total product and put into new array
    for i in arr:
        out_arr.append(total_prod//i)
        
    return out_arr
    
    
if __name__ == "__main__":
    arr1 = [2, 4, 6, 8]
    arr2 = [3, 2, 1]
    print(product_rest_1(arr1))
    print(product_rest_1(arr2))