# 品物の価値
value = [6,12,4,3,7,1,3,2,7,3,2,7,3,4,2,10,13,5,16,14,9]

# 品物の重さ
weight = [4,8,3,5,9,2,3,1,5,2,4,2,7,10,3,13,11,8]

# ナップサックの容量
capacity = 45

n = len(value)

best_value = 0          # 最大価値
best_weight = 0         # 最大価値のときの重さ
best_choice = []        # 選んだ品物

# 2^n通りをすべて調べる
for i in range(2 ** n):

    total_value = 0
    total_weight = 0
    choice = []

    # 各品物について選ぶか調べる
    for j in range(n):

        # j番目のビットが1なら選択
        if (i >> j) & 1:

            total_value += value[j]
            total_weight += weight[j]
            choice.append(j + 1)

    # 容量以内なら最大値を更新
    if total_weight <= capacity:

        if total_value > best_value:

            best_value = total_value
            best_weight = total_weight
            best_choice = choice

print("選んだ品物:", best_choice)
print("総価値:", best_value)
print("総重量:", best_weight)