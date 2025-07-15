n, x, y = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
group1 = arr[:x]
group2 = arr[x:]

min_x = min(group1)
max_y = max(group2)

result = max(0, min_x - max_y - 1)
print(result)
