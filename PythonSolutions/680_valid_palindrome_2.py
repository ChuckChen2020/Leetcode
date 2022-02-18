#2021, April 23, 22:25 - 23:14
def validPalindrome(s: str) -> bool:
        def isPalindrome(_string: str) -> bool:
            l = 0
            r = len(_string) - 1
            while l < r:
                if _string[l] != _string[r]:
                    return False
                l += 1
                r -= 1
            return True

        l = 0
        r = len(s) - 1
        cnt = 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r] and cnt == 1:
                if s[l+1] == s[r] and s[l] != s[r-1]:
                    return isPalindrome(s[l+1:r+1])
                elif s[l+1] != s[r] and s[l] == s[r-1]:
                    return isPalindrome(s[l:r])
                elif s[l+1] == s[r] and s[l] == s[r-1]:
                    return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
                else:
                    return False
            else:
                return False
        return True

if __name__ == "__main__":
    print(validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))