def is_palindrome_iterative(word):
    if word == "":
        return False
    n = len(word) - 1
    word = word.lower()
    for index, char in enumerate(word):
        if index >= n / 2:
            return True
        if char is not word[n - index]:
            return False
    return True
