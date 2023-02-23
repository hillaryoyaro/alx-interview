def makeChange(coins, total):
    # Sort the coins in descending order
    coins.sort(reverse=True)
    
    # Initialize a counter for the number of coins used
    num_coins = 0
    
    # Iterate over each coin denomination
    for coin in coins:
        # While the remaining total is greater than or equal to the current coin value
        while total >= coin:
            # Subtract the coin value from the total and increment the coin counter
            total -= coin
            num_coins += 1
    
    # If the total is not zero, then it cannot be reached with the given coins
    if total != 0:
        return -1
    
    # Otherwise, return the number of coins used
    return num_coins

