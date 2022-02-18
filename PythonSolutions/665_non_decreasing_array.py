#2021, April 23, 09:38 - 11:28
def checkPossibility(nums) -> bool:
        i = 0
        count = 1
        while (i != len(nums) - 1):
            if nums[i+1] < nums[i] and count == 1:
                if i == 0 or nums[i-1] <= nums[i+1]:
                    count -= 1
                elif i == len(nums) - 2 or nums[i+2] >= nums[i]:
                    count -= 1
                else:
                    return False
            elif nums[i+1] < nums[i] and count == 0:
                return False

            i += 1

        return True
        

if __name__ == "__main__":
    print(checkPossibility([4,2,3]))