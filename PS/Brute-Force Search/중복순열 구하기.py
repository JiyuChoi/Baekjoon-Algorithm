def dfs(l):
    if l == m:
        for x in ch:
            print(x, end=" ")
        print()
    else:
        for i in range(1, n+1):
            ch[l] = i
            dfs(l+1)

n, m = map(int, input().split())
ch = [0]*m
dfs(0)