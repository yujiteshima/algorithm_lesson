def g1(x):
    x=str(x)
    x=list(x)
    x.sort(reverse=True)
    x="".join(x)
    return int(x)

def g2(x):
    x=str(x)
    x=list(x)
    x.sort()
    x="".join(x)
    return int(x)

def f(x):
    return g1(x) - g2(x)

N, K = map(int, input().split())

for i in range(K):
     N = f(N)

print(N)
