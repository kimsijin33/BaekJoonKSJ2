a = int(input())
b = int(input())
c = int(input())

result = a*b*c
#print(result)
result_list = str(result).split()
#print(type(result_list))
#print(result_list[0][0])
#print(len(result_list[0]))

result0,result1,result2,result3,result4,result5,result6,result7,result8,result9 = 0,0,0,0,0,0,0,0,0,0

for i in range(len(result_list[0])):
    #print(result_list[0][i])
    compare_num = int(result_list[0][i])
    #print(type(compare_num))
    if compare_num == 0:
        result0 += 1
    elif compare_num == 1:
        result1 +=1
    elif compare_num == 2:
        result2 +=1
    elif compare_num == 3:
        result3 +=1
    elif compare_num == 4:
        result4 +=1
    elif compare_num == 5:
        result5 +=1
    elif compare_num == 6:
        result6 +=1
    elif compare_num == 7:
        result7 +=1
    elif compare_num == 8:
        result8 +=1
    elif compare_num == 9:
        result9 +=1
    
#print(result0,'\n',result1,'\n',result2,'\n',result3,'\n',result4,'\n',result5,'\n',result6,'\n',result7,'\n',result8,'\n',result9)
print(result0)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)