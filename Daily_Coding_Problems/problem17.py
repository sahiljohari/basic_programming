# Suppose we represent our file system by a string in the following manner:
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# dir
#     subdir1
#     subdir2
#         file.ext

# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext

# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
# Note:
# The name of a file contains at least a period and an extension.
# The name of a directory or sub-directory will not contain a period.

def longest_absolute_path(in_str):
    # Split the string by "\n"
    pathElements = in_str.split("\n")
    deepest_idx = 0
    depth = 1

    # Find the deepest element
    for i in range(1, len(pathElements)):
        current_depth = pathElements[i].count("\t")
        if depth < current_depth:
            depth = current_depth
            deepest_idx = i

    longest_path = []
    # append the deepest element to the longest path list
    longest_path.append(pathElements[deepest_idx].strip("\t"))

    # iterate backwards to check for ancestors of current element
    for i in range(deepest_idx, 0, -1):
        if pathElements[i-1].count("\t") == depth-1:
            longest_path.append(pathElements[i-1].strip("\t"))
            depth -= 1
    
    print(longest_path) # this will be in reverse order
    return len("/".join(longest_path))
        

def main():
    in_str = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(longest_absolute_path(in_str))
    

    in_str="dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tparent\n\t\tsubdir2\n\t\t\tsubsubdir2\n\t\t\t\tfile2.ext\n\t\tchild.as"
    print(longest_absolute_path(in_str))
    
if __name__ == "__main__":
    main()