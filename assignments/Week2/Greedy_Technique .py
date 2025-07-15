#Greedy Technique 
def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin 
            count += 1     
    return count if amount == 0 else -1

if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20]
    amount = 49
    result = min_coins(coins, amount)
    print(f"Minimum coins needed: {result}")  
    print(f"The coins used are: ", end="")
    for coin in coins:
        while amount >= coin:
            amount -= coin
            print(coin, end=" ")