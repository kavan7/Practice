def strStr(haystack, needle):
        chars = []
        for i, val  in enumerate(haystack):
            if needle in haystack:
                chars.append(i)
        print(chars)
            

haystack = "sadbutsad"
needle = "sad"

print(strStr(haystack, needle))
