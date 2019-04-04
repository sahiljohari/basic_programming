# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
def two_sum(num_list, k):
    num_seen = set()
        
    for first_num in num_list:
        second_num = k - first_num
        if second_num in num_seen:
            return True
        num_seen.add(first_num)
    return False

if __name__ == "__main__":
    arr = [1,2,3,5,10,13,15]
    k = 18
    
    print("Output using first approach:",two_sum(arr, k))