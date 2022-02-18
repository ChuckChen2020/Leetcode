# The method below seems to yield correct result but will end in TLE for large cases.
# def candy(ratings) -> int:
#         n = len(ratings)
#         candies = [0]*n

#         while True:
#             changed = False
#             for i in range(1, n):
#                 if ratings[i-1] < ratings[i] and candies[i-1] >= candies[i]:
#                     candies[i] = candies[i-1] + 1
#                     changed = True
#                 elif ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
#                     candies[i-1] = candies[i] + 1
#                     changed = True
#             iterations += 1
#             if not changed: 
#                 break

#         return sum(candies) + n


# Operating on a full list could end up having too long a list to handle,
# 
def candy(ratings) -> int:
        n = len(ratings)
        last_one = 1
        num_candies = 1
        # last index i where a[i-1] <= a[i], such that plus 1 shouldn't propage through i.
        last_le = 0
        # last index where a[idx-1] > a[idx] and a[idx - 1] - a[idx] > 1
        # make it a list and append element like [diff, i]
        # because adding 1, especially multiple time might accumulate the diff and end up propagating through a big_diff point.
        last_big_diff = []
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                num_candies += (last_one + 1)
                last_one += 1
                last_le = i
            elif ratings[i] == ratings[i-1]:
                num_candies += 1
                last_one = 1
                last_le = i
            elif ratings[i] < ratings[i-1] and last_one == 1:
                index_big_diff = 0
                while len(last_big_diff) and last_big_diff[-1][0] == 1:
                    del last_big_diff[-1]
                if len(last_big_diff) != 0:
                    index_big_diff = last_big_diff[-1][1]
                    last_big_diff[-1][0] -= 1

                num_candies += (i - max(last_le, index_big_diff) + 1) 
                last_one = 1                
            else:
                num_candies += 1
                last_big_diff.append([last_one - 1,i])
                last_one = 1
        return num_candies


def candy_1(ratings) -> int:
        n = len(ratings)
        candies = [1]*n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in reversed(range(1,n)):
            if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                candies[i-1] = candies[i] + 1

        return sum(candies)        


if __name__ == "__main__":
    print(candy_1([1,6,10,8,7,3,2])) 