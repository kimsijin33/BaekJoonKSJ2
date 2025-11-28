N, X = map(int, input().split( ))
A = map(int, input().split( ))

small_list = []
for i in A:
    if i < X:
        small_list.append(i)
    else:
        continue
for i in small_list:
    print(i, end=" ")