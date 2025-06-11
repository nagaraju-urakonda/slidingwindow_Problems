def length_of_longest_substring(s: str) -> int:
    a = set()
    max_len = 0
    left = 0

    for i in range(len(s)):
        while s[i] in a:
            a.remove(s[left])
            left += 1
        a.add(s[i])
        max_len = max(max_len, i - left + 1)

    return max_len
string = input().strip()
print(length_of_longest_substring(string))
