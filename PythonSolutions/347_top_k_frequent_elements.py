# 2021 April 29, 20:11 - 20:37
from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
        def partition(freq: List[List[int]], l: int, r:int)-> int:
            if l > r:
                return
            pivot = freq[r][1]
            p_index = l
            for i in range(l,r):
                if freq[i][1] < pivot:
                    freq[i], freq[p_index] = freq[p_index], freq[i]
                    p_index += 1
            freq[r], freq[p_index] = freq[p_index], freq[r]
            return p_index, r - p_index + 1

        counter = dict()
        for x in nums:
            if x in counter.keys():
                counter[x] += 1
            else:
                counter[x] = 1
        freq = []
        for key, val in counter.items():
            freq.append([key,val])

        l = 0
        r = len(freq) - 1
        while True:
            p, length = partition(freq, l, r)
            if length > k:
                l = p + 1
            elif length < k:
                k -= length
                r = p - 1
            else:
                return [x[0] for x in freq[p:]]


from collections import Counter
def topKFrequent_counter(nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return list(map(lambda x: x[0], counter.most_common(k)))

# heap solution might be a bit hard to apply on a certain key, esepcially with heapq. But stackoverflow gave a solution of overriding < and >.
import heapq
from collections import Counter
def topKFrequent_heap(nums: List[int], k: int) -> List[int]: 
        class WordFreq(object):
            def __init__(self, num, freq):
                self.num = num
                self.freq = freq
            def __lt__(self, other):
                return self.freq < other.freq
            def __gt__(self, other):
                return self.freq > other.freq
            def getter(self):
                return self.num

        counter = Counter(nums)
        heap = []
        for num, freq in counter.items():
            heap.append(WordFreq(num, freq))
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return list(map(lambda x: x.getter(), heap))


if __name__ == "__main__":
    print(topKFrequent([1], 1))
    print(topKFrequent_counter([1], 1))
    print(topKFrequent_heap([1,1,1,2,2,3], 2))