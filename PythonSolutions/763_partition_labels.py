#16:39 - 17:03
def partitionLabels(S: str):
        dic = dict()
        for i, c in enumerate(S):
            dic[c] = i
        end_pos = 0

        ret = []
        i = 0
        while i <= len(S) - 1:
            start = i
            end_pos = dic[S[i]]
            while i != end_pos:
                end_pos = max(end_pos, dic[S[i]])
                i += 1
            ret.append(end_pos - start + 1)
            i = end_pos + 1

        return ret 


if __name__ == "__main__":
    print(partitionLabels("ababcbacadefegdehijhklij"))