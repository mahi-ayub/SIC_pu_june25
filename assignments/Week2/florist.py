def getMinimumCost(k, c):
    c.sort(reverse=True)  
    total_cost = 0

    for i in range(len(c)):
        multiplier = i // k  
        total_cost += (multiplier + 1) * c[i]
    return total_cost

n, k = map(int, input().split())
c = list(map(int, input().split()))
result = getMinimumCost(k, c)
print(result)