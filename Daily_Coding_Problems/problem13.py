# Given an integer k and a string s, find the length of the 
# longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring 
# with k distinct characters is "bcb".

def maxSubString(s, k):
    if len(s) <= k:
        return 0
    else:
        start, end, maxLength = 0, k, k

        while end < len(s):
            end += 1

            while True:
                distinct_chars = len(set(s[start:end]))

                if distinct_chars <= k:
                    break

                start += 1
            
            maxLength = max(maxLength, end-start)

        return maxLength

def main():
    
    s1 = ['aabbcc', 2]
    s2 = ['aabbcc', 3]
    s3 = ['abcba', 2]
    s4 = ['cbebebe', 3]
    s5 = ['qwertytrewq', 3]
    s6 = ['xyzyxabxy', 2]
    
    testCases = [s1,s2,s3,s4,s5,s6]
    
    for test in testCases:
        print("Test-Case:%s Output: %d" % (test[0], maxSubString(test[0], test[1])))


if __name__ == "__main__":
    main()