# This problem was asked by Palantir.

# Write an algorithm to justify text.
# Given a sequence of words and an integer line length k,
# return a list of strings which represents each line, fully justified.

# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k.
# Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

# If you can only fit one word on a line, then you should pad the right-hand side with spaces.
# Each word is guaranteed not to be longer than k.

# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
# you should return the following:
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

def pad_spaces(sentence, max_len):
    num_spaces = max_len - len(sentence)
    words = sentence.split(" ")
    
    # edge case: if sentence has only one word
    if len(words) == 1:
        for _ in range(num_spaces):
            sentence += " "
        return sentence

    else:
        repeat = True
        while repeat:
            for i in range(len(words) - 1):
                if num_spaces > 0:
                    words[i] += " "
                    num_spaces -= 1
                else:
                    repeat = False
        
        return " ".join(words)

def justify(input_list, k):
    buffer = []
    temp_str = ""

    for word in input_list:
        if len(temp_str) + len(word) > k:
            buffer.append(temp_str.strip())
            temp_str = word + " "
        else:
            temp_str += word + " "
    buffer.append(temp_str.strip())

    for i in range(len(buffer)):
        if len(buffer[i]) < k:
            buffer[i] = pad_spaces(buffer[i], k)
    return buffer

def main():
    input_list = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    k = 16

    print(justify(input_list, k))
    # ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']

if __name__ == "__main__":
    main()