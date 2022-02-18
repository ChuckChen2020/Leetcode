# 2021 June 4 14:44

# The solution is based on a rather magical algorithm called:
# Reservoir Sampling

# Naturally, we'd think of traversing over the entire linked-list, and get to
# know the enire length. Random sample and then traverse again to get the 
# element. Or else store the elements in a list. But these makes it either not a 
# "one-pass" solution, or requires additional space.
# 
# Without traversing the entire list FIRST (which eventually the algo will), we
# won't know the number N beforehand. The data comes like a stream, you process
# it as you see it. 
# 
# Reservoir Sampling:
# Suppose we have a stream a, b, c, d, e, f. 
# As we see a, we have a 1/1 probability of recording it as an POTENTIAL
# answer. 

# As we then see b, we have a 1/2 probability of recording b. This makes the
# record remains A to have also 1/2 probability. PROBABILITY IS EQUAL FOR ALL
# ELEMENTS WE HAVE SEEN SO FAR.

# Then we see c, 1/3 probability that we record it. This makes the prob of 
# A staying on the record to be 2/3*1/2= 1/3. Similarly for B it's also 1/3.
# Probabilities are still equal!
# 
# For the mth element, we want a 1/m probability to set it as a record. Then
# the prob for any of the previous elements would be (m-1)/m*1/(m-1) = 1/m.
# It goes like this till the end of the linked list.   

from random import randint
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        cur = self.head
        m = 0
        ans = 0
        while cur:
            rnd = randint(0, m)
            if rnd == 0:
                ans = cur.val
            cur = cur.next
            m += 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()