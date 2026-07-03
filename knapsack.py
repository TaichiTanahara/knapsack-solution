weight = [4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13, 11, 8]

value = [6, 12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2, 10, 13, 5, 16, 14, 9]

capacity = 45

n = len(weight)

best_value = 0
best_weight = 0
best_choice = []

# 全探索
for i in range(2 ** n):

    total_weight = 0
    total_value = 0
    choice = []

    for j in range(0,n):

        # j番目の品物を選ぶか判定
        if (i >> j) & 1:

            total_weight += weight[j]
            total_value += value[j]
            choice.append(j + 1)

    # もし容量以内なら最適解を更新
    if total_weight <= capacity and total_value > best_value:

        best_value = total_value
        best_weight = total_weight
        best_choice = choice

print("最適な品物の組み合わせ")
print(best_choice)

print("総重量 =", best_weight)
print("総価値 =", best_value)