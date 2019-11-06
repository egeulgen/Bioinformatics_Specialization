def DPChange(money, coins):
    MinNumCoins = [0]
    for m in range(1, money + 1):
        MinNumCoins.append(money + 1)
        for coin in coins:
            if m >= coin:
                current = MinNumCoins[m - coin] + 1
                if current < MinNumCoins[m]:
                    MinNumCoins[m] = current
    return MinNumCoins[money]

if __name__ == "__main__":
    money = int(input().rstrip())
    coins = input().rstrip().split(',')
    for i in range(len(coins)):
        coins[i] = int(coins[i])
    print(DPChange(money, coins))