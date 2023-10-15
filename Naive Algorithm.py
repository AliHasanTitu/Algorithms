# Python3 program for Naive Pattern
# Searching algorithm

def search(pat, txt): # Define a function
    length_of_pattern = len(pat)
    length_of_string = len(txt)

    # A loop to slide pat[] one by one */
    for i in range(length_of_string - length_of_pattern + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        while (j < length_of_pattern):
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == length_of_pattern):
            print("Pattern found at index ", i)


# Driver's Code
if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"

    # Function call
    search(pat, txt)