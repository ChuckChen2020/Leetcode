# 2021, April 25, 10:47 - 13:07
def findLongestWord(s: str, dictionary) -> str:
        achieved = ""
        for word in dictionary:
            ps = pw = 0
            while True:
                if ps != len(s) - 1 and s[ps] != word[pw]:
                    ps += 1
                elif ps == len(s) - 1 and s[ps] != word[pw]:
                    break
                else:
                    pw += 1
                    ps += 1
                    if pw == len(word):
                        if len(word) > len(achieved) or (len(word) == len(achieved) and word < achieved):
                            achieved = word
                            break
                        else:
                            break
                    elif pw != len(word) and ps == len(s):
                        break
                    else:
                        continue
        return achieved
if __name__ == "__main__":
    print(findLongestWord("abpcplea", ["a","b","c"]))