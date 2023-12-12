def lengthOfLastWord(s):
    words = s.split()
    last = len(words)
    length = len(words[last - 1])
    return length
