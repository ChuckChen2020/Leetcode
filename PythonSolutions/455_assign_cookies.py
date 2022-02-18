def findContentChildren(g, s) -> int:
        g = sorted(g, reverse=True)
        satisfied = [False]*len(g)

        for x in s:
            for i in range(len(g)):
                if satisfied[i] == True or x < g[i]:
                    continue
                else:
                    satisfied[i] = True
                    break
        return satisfied.count(True)


if __name__ == "__main__":
    print(findContentChildren([1, 2, 3], [3]))