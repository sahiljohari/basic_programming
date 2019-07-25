# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding.
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.

class runLength():
    def __init__(self, input_str):
        self.input_str = input_str
        self.output_str = ""

    def encode(self):
        first_char = self.input_str[0]
        char_count = 1

        for char in self.input_str[1:]:
            if char == first_char:
                char_count += 1
            else:
                self.output_str += str(char_count) + first_char
                first_char = char
                char_count = 1
        self.output_str += str(char_count) + first_char
        return self.output_str

    def decode(self):
        if self.output_str == "":
            return self.input_str

        decoded_str = ""
        for i in range(len(self.output_str)):
            if i % 2 == 0:
                for count in range(int(self.output_str[i])):
                    decoded_str += self.output_str[i+1]

        return decoded_str

def main():
    input_str = "AAAABBBCCDAA"
    rle = runLength(input_str)

    assert rle.encode() == "4A3B2C1D2A", "Test case failed"
    assert rle.decode() == input_str, "Test case failed"

    print("All test cases passed!")

if __name__ == "__main__":
    main()