'''def longest_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len'''


def longest_substring(s):
    freq = {}
    left = 0
    max_len = 0

    for i in range(len(s)):
        ch = s[i]

        if ch in freq:                          
            left = max(left, freq[ch] + 1)      

        freq[ch] = i                            
        max_len = max(max_len, i - left + 1)    

    return max_len


s = "pwwkew"
print(longest_substring(s))  # Output: 3


s = "pwwkew"
print(longest_substring(s))  # Output: 3
