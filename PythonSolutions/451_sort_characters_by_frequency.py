# 2021 April 29, 22:45 - 23:03
from collections import Counter
def frequencySort(s: str) -> str:
        counter = Counter(s)
        ret = []
        for char, freq in counter.most_common():
            for _ in range(freq):
                ret.append(char)
        return "".join(ret)

if __name__ == "__main__":
    print(frequencySort("Aabb"))