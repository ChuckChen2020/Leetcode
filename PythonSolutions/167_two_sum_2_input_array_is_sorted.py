#2021, April 23, 11:46 - 12:16
# Rather nasty and slow solution.
def twoSum(numbers, target: int):
        for idx, num in enumerate(numbers):
            obj = target - num
            if (obj == num):
                if numbers[idx + 1] == obj:
                    return [idx + 1, idx + 2]
                else:
                    continue
            try:
                index = numbers.index(obj)
                return [idx + 1, index + 1]
            except ValueError:
                continue
        return [-1,-1]

# The one below is smarter!
def twoSum_two_pointers(numbers, target: int):
        '''
            starting from head and tail. if summation g.t. target, right index move left-wards, if summation l.t. target, left index move right-wards.
            The two pointers won't skip the only valid answer. e.g.,
            .............. a[i] ................ a[j] ..............
            ......... ^ ...................^........................
            won't be possible. Because when the left pointer is to the left
            of a[i], at the time when right pointer was still at a[j], the sum would be less, thus the left pointer would be required to 
            move rightwards, instead of right p. being required to move leftwards. 
        '''
        index_1 = 0
        index_2 = len(numbers) - 1
        while True:
            summation = numbers[index_1] + numbers[index_2]
            if summation > target:
                index_2 -= 1
            elif summation < target:
                index_1 += 1
            else:
                return [index_1 + 1, index_2 + 1] 



if __name__ == "__main__":
    print(twoSum_two_pointers([0,0,3,4], 0))