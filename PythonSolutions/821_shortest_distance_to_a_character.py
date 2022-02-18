def shortestToChar(s: str, c: str):
    ans = []
    c_indices = []
    for idx, x in enumerate(s):
        if x == c:
            c_indices.append(idx)

    for i in range(len(c_indices)):
        if i == 0:
            for x in range(c_indices[0]):
                ans.append(abs(x - c_indices[0]))
        else:
            for x in range(c_indices[i - 1], c_indices[i]):
                ans.append(min(abs(x - c_indices[i-1]), abs(x - c_indices[i])))

    for x in range(c_indices[-1], len(s)):
        ans.append(abs(x - c_indices[-1]))
    
    return ans






if __name__ == "__main__":
    print(shortestToChar("aaab", "b"))