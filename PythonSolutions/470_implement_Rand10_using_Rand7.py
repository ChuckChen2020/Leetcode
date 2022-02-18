# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# Don't know why the following solution doesn't work on 100000 calls case.
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a, b = rand7() - 1, rand7() - 1
        num = a*7 + b
        if num >= 40:
            self.rand10()
        return num % 10 + 1

# This works
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a= rand7() 
        b= rand7() 
        num = (a-1)*7 + b
        if num >40: 
            return self.rand10()
        return num % 10 + 1

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = 40
        while num >= 40:
            num = (rand7() - 1)*7 + rand7() - 1
        return num % 10 + 1