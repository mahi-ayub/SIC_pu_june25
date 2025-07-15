def is_valid(arrangement):
    for i in range(1, len(arrangement)):
        if arrangement[i] < arrangement[i-1]:
            return False
    return True

def solve(n, boys, girls):
    boys.sort()
    girls.sort()
    
    # Try boy-girl-boy-girl...
    pattern1 = []
    for i in range(n):
        pattern1.append(boys[i])
        pattern1.append(girls[i])
    
    # Try girl-boy-girl-boy...
    pattern2 = []
    for i in range(n):
        pattern2.append(girls[i])
        pattern2.append(boys[i])

    if is_valid(pattern1) or is_valid(pattern2):
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))
    print(solve(n, boys, girls))
