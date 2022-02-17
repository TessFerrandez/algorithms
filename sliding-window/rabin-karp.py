# Rabin-Karp algorithm in python


NCHARS = 4
PRIME = 5381

def search(pattern, text):
    PATTERN_LEN = len(pattern)
    TEXT_LEN = len(text)
    pattern_hash = 0
    text_hash = 0

    h = 1
    for i in range(PATTERN_LEN - 1):
        h = (h * NCHARS) % PRIME

    # Calculate hash value for pattern and text
    for i in range(PATTERN_LEN):
        pattern_hash = (NCHARS * pattern_hash + ord(pattern[i])) % PRIME
        text_hash = (NCHARS * text_hash + ord(text[i])) % PRIME

    print("Pattern Hash:", pattern_hash)

    # Find the match
    for i in range(TEXT_LEN - PATTERN_LEN + 1):
        if pattern_hash == text_hash:
            print(i, "pattern hash == text hash")
            for j in range(PATTERN_LEN):
                if text[i + j] != pattern[j]:
                    break

            j += 1
            if j == PATTERN_LEN:
                print("Pattern is found at position: " + str(i))

        if i < TEXT_LEN - PATTERN_LEN:
            text_hash = (NCHARS * (text_hash - ord(text[i]) * h) + ord(text[i + PATTERN_LEN])) % PRIME

            if text_hash < 0:
                text_hash = text_hash + PRIME

            print(i, text_hash, text[i + 1: i + PATTERN_LEN + 1])


# text = "ABCCDDAEFGCDDDDCD"
# pattern = "BCC"
text = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
pattern = "AAAAACCCCC"
search(pattern, text)
