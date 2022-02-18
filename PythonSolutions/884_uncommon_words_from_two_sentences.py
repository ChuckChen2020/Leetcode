def uncommonFromSentences(A: str, B: str):
        words_A = A.split(" ")
        words_B = B.split(" ")
        words_A_1 = [x for x in words_A if words_A.count(x) == 1 and words_B.count(x) <= 1]
        words_B_1 = [x for x in words_B if words_B.count(x) == 1 and words_A.count(x) <= 1]
        set_A = set(words_A_1)
        set_B = set(words_B_1)


        return list(set_A.symmetric_difference(set_B))

if __name__ == "__main__":
    print(uncommonFromSentences("s z z z s", "s z ejt"))