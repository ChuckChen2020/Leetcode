# 2021 June 9 12:42 - surrendered

# Important Notes:
# 1) char existence representation in 26 bits.
# 2) how bit-wise-and not zero indicates common letters.

# The idea involved here is to represent the existence of a char in a word
# as a bit in an integer, of which the rightmost 26 bits corresponds to the
# 26 lower case letters.

# The bitwise and of two of these integers, if equal to 1 at some bit, would 
# mean that there is a common letter in these two words, the value of such an
# integer would be non-zero. Words without any common letters, their integer 
# representations' bit and would give 0.

from typing import List
from collections import defaultdict
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mapping = defaultdict(int)
        ans = 0
        for word in words:
            bin_repr, word_size = 0, len(word)
            for c in word:
                bin_repr |= 1 << ord(c) - ord('a')
            # Compare the word with all we have in the hash table so far.
            for bin_num, size in mapping.items():
                if bin_num & bin_repr == 0:
                    ans = max(ans, size*word_size)
            # if two words' representations are the same, keep the longer size.
            mapping[bin_repr] = max(mapping[bin_repr], word_size)
        return ans


                

if __name__ == "__main__":
    print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
    print(Solution().maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
    print(Solution().maxProduct(["a","aa","aaa","aaaa"]))