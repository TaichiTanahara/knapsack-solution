weights = [4,8,3,5,9,2,3,1,5,2,4,2,7,10,3,13,11,8]
values = [6,12,4,3,7,1,3,2,7,3,4,2,10,13,5,16,14,9]

capacity = 45
n = len(weights)

# DPテーブル
dp = [[0]*(capacity+1) for _ in range(n+1)]

# DPの計算
for i in range(n):
    for w in range(capacity+1):
        if weights[i] <= w:
            dp[i+1][w] = max(dp[i][w],
                             dp[i][w-weights[i]] + values[i])
        else:
            dp[i+1][w] = dp[i][w]

print("最大価値:", dp[n][capacity])

# -------- 組み合わせを復元 --------
w = capacity
selected = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        selected.append(i)
        w -= weights[i-1]

selected.reverse()

print("選んだ品物:", selected)

