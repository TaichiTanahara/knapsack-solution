weights = [4,8,3,5,9,2,3,1,5,2,4,2,7,10,3,13,11,8]
values = [6,12,4,3,7,1,3,2,7,3,4,2,10,13,5,16,14,9]

capacity = 45

n = len(weights)

dp = [0] * (capacity + 1)

for i in range(n):
    for w in range(capacity, weights[i]-1, -1):
        dp[w] = max(dp[w],
                    dp[w-weights[i]] + values[i])

print("最大価値:", dp[capacity])