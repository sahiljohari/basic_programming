# Implement a trie and use it to efficiently store strings

class Trie(object):
    def __init__(self):
        self.root_node = {}

    def add_word(self, word):
        current_node = self.root_node
        is_new_word = False
        
        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]
            
        if "*" not in current_node:
            is_new_word = True
            current_node["*"] = {}
            
        return is_new_word