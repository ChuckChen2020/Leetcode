# 15:09 - 15:25
def canPlaceFlowers(flowerbed, n: int) -> bool:
        if len(flowerbed) == 0:
            return False
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return 1 >= n
            elif flowerbed[0] == 1:
                return 0 >= n 
        count = 0
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[0] == 0 and flowerbed[1] == 0:
                    count += 1
                    flowerbed[0] = 1
            elif i  == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    count += 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1]==0:
                    count += 1
                    flowerbed[i] = 1
        return count >= n

if __name__ == "__main__":
    print(canPlaceFlowers([1,0,0,0,1], 1))