a, b = map(int, input().split())

if a <= 0 and b <= 0:
    answer = abs(a - b)
elif a <= 0 and b >= 0:
    answer = abs(a) + b
elif a >= 0 and b >= 0:
    answer = abs(a - b)
elif a >= 0 and b <= 0:
    answer = a + abs(b)
print(answer)