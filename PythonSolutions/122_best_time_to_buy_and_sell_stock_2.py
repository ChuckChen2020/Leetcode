#17:17 - 17:25
def maxProfit(prices) -> int:
        diff = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
        profit = 0
        for x in diff:
            if x > 0:
                profit += x
        return profit

if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))