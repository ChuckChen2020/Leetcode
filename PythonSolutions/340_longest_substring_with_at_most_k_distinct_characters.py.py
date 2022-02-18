# 2021, April 25, 16:30 - 17:16
# The solution below passes the sample cases, but has not been accepted as a submission, since the problem is locked on leetcode.
def lengthOfLongestSubstringKDistinct(s:str, k:int):
        l = r = 0
        dict_s = dict()
        max_len = 0
        while l <= r:
            if len(dict_s.keys()) <= k:
                max_len = max(max_len, r - l)
                if r != len(s):
                    r += 1

                if s[r-1] not in dict_s.keys():
                    dict_s[s[r-1]] = 1
                else:
                    dict_s[s[r-1]] += 1
            else:
                if dict_s[s[l]] == 1:
                    del dict_s[s[l]]
                else:
                    dict_s[s[l]] -= 1
                l += 1

            if r == len(s) and r - l <= max_len:
                break
        return max_len 

if __name__ == "__main__":
    print(lengthOfLongestSubstringKDistinct("aabbbcccsseeekkkk", 4))
