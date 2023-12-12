def palindrome(s):
    news = s.strip()
    news = s.lower()
    newsr = s[::-1]
    return news == newsr


s = ''

print(palindrome(s))