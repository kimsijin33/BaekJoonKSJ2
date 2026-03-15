x, y = map(int, input().split( ))

def weekly (result):
    if result == 0:
        answer = "SUN"
    elif result == 1:
        answer = "MON"
    elif result == 2:
        answer = "TUE"        
    elif result == 3:
        answer = "WED"
    elif result == 4:
        answer = "THU"
    elif result == 5:
        answer = "FRI"
    elif result == 6:
        answer = "SAT"
    return answer
        
if x == 1:
    result = y % 7
elif x == 2:
    y = y + 31
    result = y % 7
elif x == 3:
    y = y + 59
    result = y % 7
elif x == 4:
    y = y + 90
    result = y % 7
elif x == 5:
    y = y + 120
    result = y % 7
elif x == 6:
    y = y + 151
    result = y % 7
elif x == 7:
    y = y + 181
    result = y % 7
elif x == 8:
    y = y + 212
    result = y % 7
elif x == 9:
    y = y + 243
    result = y % 7
elif x == 10:
    y = y + 273
    result = y % 7
elif x == 11:
    y = y + 304
    result = y % 7
elif x == 12:
    y = y + 334
    result = y % 7
    
answer = weekly(result)
print(answer)