#2021 April 23, 17:43 - 19:03
# The solution below seems correct, but TLE.
def minWindow(s: str, t: str) -> str:
        def contains(s1:str, s2:str)-> bool:
            for c in s2:
                if s1.count(c) < s2.count(c):
                    return False
            return True

        if s == "" or t == "" or len(s) < len(t):
            return ""

        min_length = len(t)
        poss_index = []
        for idx, c in enumerate(s):
            if c in t:
                poss_index.append(idx)

        while min_length != len(s) + 1:
            for index in poss_index:
                for i in range(min_length):
                    start = index - i
                    end = index + min_length - i
                    if len(s[start:end]) == min_length and contains(s[start:end],t):
                        return s[start:end] 
            min_length += 1
        
        return ""

# Still TLE on case 265, the char tallying should not be done with every new string, rather, it should be updated. 
def  minWindow_1(s: str, t: str) -> str:
        def contains(d1:dict, d2:dict)-> bool:
            for key, value in d2.items():
                if key not in d1.keys() or d1[key] < value:
                    return False
            return True

        def char_counter(s:str) -> dict:
            dic = {}
            for c in s:
                if c in dic.keys():
                    dic[c] += 1
                else:
                    dic[c] = 1
            return dic

        if s == "" or t == "" or len(s) < len(t):
            return ""

        dict_t = char_counter(t)

        l = 0
        r = 0

        res = ""
        while r != len(s) + 1:
            if not contains(char_counter(s[l:r]), dict_t):
                r += 1
            else:
                if len(res) == 0 or r-l < len(res):
                    res = s[l:r]
                if l < r:
                    l += 1
        return res    


def  minWindow_2(s: str, t: str) -> str:
        def contains(d1:dict, d2:dict)-> bool:
            for key, value in d2.items():
                if key not in d1.keys() or d1[key] < value:
                    return False
            return True

        if s == "" or t == "" or len(s) < len(t):
            return ""

        dict_t = dict()
        for c in t:
            if c in dict_t.keys():
                dict_t[c] += 1
            else:
                dict_t[c] = 1

        tally = dict()

        l = 0
        r = 0

        res = ""
        while True:
            if not contains(tally, dict_t):
                r += 1
                if r != len(s) + 1:
                    if s[r-1] in tally.keys():
                        tally[s[r-1]] += 1
                    else:
                        tally[s[r-1]] = 1
                else:
                    break
            else:
                if len(res) == 0 or r-l < len(res):
                    res = s[l:r]
                if l < r:
                    tally[s[l]] -= 1
                    l += 1
        return res 


if __name__ == "__main__":
    print(minWindow_2("a", "a"))