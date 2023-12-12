def longestCommonPrefix(strs):
    if not strs:
        return ""

    min_len = min(len(s) for s in strs)
    prefix = []

    for i in range(min_len):
        common_char = strs[0][i]
        samechar = True

        for s in strs[1:]:
            if s[i] != common_char:
                samechar = False
                break

        if samechar:
            prefix.append(common_char)
        else:
            break

    return "".join(prefix)

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
