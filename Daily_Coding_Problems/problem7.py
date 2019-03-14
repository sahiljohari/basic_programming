# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

# To-Do: Apply Dynamic programming

# Using Recursion
def decode(msg):
    # Base case
    if len(msg) <= 1:
        return 1
    
    if len(msg) >= 2:
        if int(msg[:2]) >= 1 and int(msg[:2]) <= 26:
            return decode(msg[1:]) + decode(msg[2:])
        return decode(msg[1:])

def main():
    messages = ['111', '11111', '12345', '14252', '92832']

    for msg in messages:
        print("Test-Case:%s Output: %d" % (msg, decode(msg)))

if __name__ == "__main__":
    main()