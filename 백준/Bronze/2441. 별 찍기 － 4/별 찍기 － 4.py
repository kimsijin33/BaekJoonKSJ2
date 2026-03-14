a = int(input())
    
for i in range(a, 0, -1):
    #print("*"*i)
    stars = '*' * i
    print(stars.rjust(a))    