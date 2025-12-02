count = int(input())
#N, X = map(str, input().split( ))

#print(type(N))
#print(type(X))

for i in range(count):
    answer = ''
    N, X = map(str, input().split( ))
    j = len(X)
    for k in range(j):
        answer += X[k]*int(N)
    print(answer)