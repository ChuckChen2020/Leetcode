# 2021 April 25, 22:09-22:48
def searchRange(nums , target: int):
        if len(nums) == 0:
            return [-1,-1]

        l = 0
        r = len(nums) - 1
        mid = 0
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                break

        if nums[mid] != target:
            return [-1,-1]
        
        lr = rl = mid

        while l <= lr:
            m = int((l+lr)/2)
            if nums[m] == target:
                lr = m - 1
            else:
                l = m + 1
                if nums[l] == target:
                    break

        while rl <= r:
            m = int((rl+r)/2)
            if nums[m] == target:
                rl = m + 1
            else:
                r = m - 1
                if nums[r] == target:
                    break
        
        return [l,r]

if __name__ == "__main__":
    print(searchRange([], 6))