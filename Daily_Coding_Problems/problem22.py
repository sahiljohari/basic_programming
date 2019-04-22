# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
# If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', 
# and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', 
# and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

def get_original_sentence(words, sentence):
    '''
    Time complexity: O(s*w)
    Space complexity: O(w+s) 
    w = size of words dictionary and 
    s = length of sentence
    '''
    buffer_str = ""
    out_list = []
    for c in sentence:
        if buffer_str in words:
            out_list.append(buffer_str)
            buffer_str = c

        else:
            buffer_str += c
    if buffer_str in words:
            out_list.append(buffer_str)

    return out_list


def main():
    words = ['quick', 'brown', 'the', 'fox']
    sentence = "thequickbrownfox"
    print(get_original_sentence(words, sentence))

    words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    sentence = "bedbathandbeyond"
    print(get_original_sentence(words, sentence))

if __name__ == "__main__":
    main()