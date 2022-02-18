
def numberOfSubarrays(nums, k: int):
    odd_indices = []
    for idx, x in enumerate(nums):
        if x % 2 == 1:
            odd_indices.append(idx)
    count_over_odds = 0
    for start in range(len(odd_indices) - k + 1):       
        valid_slice = odd_indices[start: start + k]

        count = 1
        head = 1
        tail = 1

        if start != 0:
            head = odd_indices[start] - odd_indices[start - 1]
        else:
            head += odd_indices[0]
        
        if start + k != len(odd_indices):
            tail = odd_indices[start + k] - odd_indices[start + k - 1]
        else:
            tail += (len(nums) - odd_indices[-1] - 1)

        count *= head
        count *= tail

        count_over_odds += count
    return count_over_odds




if __name__ == "__main__":
    print(numberOfSubarrays([45627,50891,94884,11286,35337,46414,62029,20247,72789,89158,54203,79628,25920,16832,47469,80909], 1))


