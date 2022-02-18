class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(_str: str) -> str:
            char_list = []
            for i, x in enumerate(_str):
                if x == "#":
                    if i and len(char_list): 
                        char_list.pop()
                    else:
                        continue
                else:
                    char_list.append(x)
            return "".join(char_list)
        return process(s)==process(t)

    def backspaceCompare_1(self, s: str, t: str) -> bool:
        def F(S):
            skip = 0
            for c in reversed(S):
                if c == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))


# Checking backwards. 
# "#abc###defg##hi"
# hi stay, two #'s so we know fg will be gone, de stay, abc gone.

    
        
 