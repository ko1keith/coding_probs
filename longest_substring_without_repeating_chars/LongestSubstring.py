class LongestSubstring(object):
    def longest_substring(self, s):
        longest = 0
        left, right = 0, 0
        s_dict = set()

        while left < len(s) and right < len(s):
            if s[right] not in s_dict:
                s_dict.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                s_dict.remove(s[left])
                left += 1
        return longest
