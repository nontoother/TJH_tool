# 给定长度为 n 的数组arr，这个数组中，每个元素代表一个木头的长度
# 木头可以随意的截断，从木头中找出k 个相同的长度为 m 的木块
# 求m的最大值
#
# 例如
# n = 5
# k = 5
# arr=[4,7,2,10,5]
#
# 应返回 m = 4

# n = 5
# k = 5
#
# arr = [5, 7, 5, 21, 7]
#
# sum = 0
# max_arr = max(arr)
#
# for i in arr:
#     sum += i
#
# avg = sum // n
#
# for i in range(max_arr):
#     count = 0
#     max = avg - i
#     if max < 1:
#         break
#     for j in arr:
#         num = j // max
#         count += num
#     if count == k:
#         break
#
# if max >= 1:
#     print('max:', max)
# else:
#     print('no such value')

# flowerbed = [1, 0, 0, 0, 0, 1]
# n = 2
# flowerbed = [1, 0]
# n = 1
# flowerbed = [0]
# n = 1


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13, 14, 15, 16]]
result = []

m, n = len(matrix), len(matrix[0])
i, j = 0, 0
visited = [[1] * n for _ in range(m)]
sum_all = sum(map(sum,visited))
direction = 'right'
while sum_all > 0:
    result.append(matrix[i][j])
    sum_all -= 1
    visited[i][j] = 0

    if direction == 'right':
        if j+1 < n and visited[i][j+1] == 1:
            j += 1
        else:
            direction = 'down'
            i += 1
    elif direction == 'down':
        if i+1 < m and visited[i+1][j] == 1:
            i += 1
        else:
            direction = 'left'
            j -= 1
    elif direction == 'left':
        if j > 0 and visited[i][j-1] == 1:
            j -= 1
        else:
            direction = 'up'
            i -= 1
    else:
        if i > 0 and visited[i-1][j] == 1:
            i -= 1
        else:
            direction = 'right'
            j += 1

print(result)