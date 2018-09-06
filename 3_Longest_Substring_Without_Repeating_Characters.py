class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record_place = {}
        max_len = 0
        start = 0
        end = 0
        for (i, ch) in enumerate(s):
            if ch not in record_place:
                end += 1
                if max_len < (end - start):
                    max_len = end - start
            else:
                start = record_place[ch] + 1
                end += 1
                if max_len < (end - start):
                    max_len = end - start
            record_place[ch] = i
        return max_len