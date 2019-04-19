# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
# find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
# -----------------------------------------------------------------------------------------------------


# Approach:
# 1. Create a sorted list of numbers from the input
# 2. Assign start/end flags to each number in the sorted list
# 3. Use count and max_count, both equal to 0 initially
# 4. Increment count by 1 when we see a start, and decrement by 1 when we see an end
# 5. Update max_count based on the count value

def min_rooms(arr):
    '''
    Time Complexity: O(n + nlogn)
    Space Complexity: O(2n)
    '''
    sorted_list = []
    # Step 1
    for interval in arr:
        sorted_list.append(interval[0])
        sorted_list.append(interval[1])

    # Assuming this is a Quick-sort [O(nlogn)]
    sorted_list = sorted(sorted_list)

    # Step 2
    for s, e in arr:
        sorted_list[sorted_list.index(s)] = "s"
        sorted_list[sorted_list.index(e)] = "e"

    # Step 3
    count, max_count = 0, 0

    # Step 4
    for char in sorted_list:
        if char == "s":
            count += 1
        else:
            count -= 1
        # Step 5
        if count > max_count:
            max_count = count

    return max_count

def main():
    arr = [(30, 75), (0, 50), (60, 150)] # 2 rooms
    arr = [(0, 10), (5, 40), (45, 100), (80, 120), (90, 150), (110, 140)] # 3 rooms

    print("Minimum rooms required: %d" % (min_rooms(arr)))

if __name__ == "__main__":
    main()