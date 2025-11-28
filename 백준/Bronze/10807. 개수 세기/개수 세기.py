A = int(input())
B = map(int, input().split( ))
C = int(input())

count = 0
for i in B:
    if i == C:
        count += 1
    else:
        continue

print(count)