#program to find the max profits you can get from buying and selling stocks. Yoy are given an array with stocks price for seven days, and you can buy and sell any day

def calculateProfits(arr,arr_size):
    
    profit = 0
    for i in range(1, arr_size):
        
        # If the current element is greater than last element then we weill but the previous day and sell it the current day.
        profit += arr[i] - arr[i-1]
    
    return profit
prices = [635.864,247,325,257,745,245]
profit = calculateProfits(prices, len(prices))
print("Max profit : ",profit)