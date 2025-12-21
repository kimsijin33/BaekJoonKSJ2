#mat = map(int, input().split( ))
arr = [list(map(int, input().split())) for _ in range(9)]

#print(type(mat))
#print(len(mat))
max_value = []
max_list = []
for i in arr:
    #print(i)
    max_value.append(max(i))
    #print(max_value)
    max_list.append(i.index(max(i)))

#print(max_value)
#print(max_list)

print(max(max_value))
print(max_value.index(max(max_value))+1, max_list[max_value.index(max(max_value))]+1)
#print(max_list[max_value.index(max(max_value))]+1)