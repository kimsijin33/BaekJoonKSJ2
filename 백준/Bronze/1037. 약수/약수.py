a = int(input())
b = map(int, input().split())
c = []

for i in b:
    c.append(i)
        
d = max(c)

#print(int(d)*2)
print(int(d)*int(min(c)))