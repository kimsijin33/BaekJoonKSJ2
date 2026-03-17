string = input()

for i in range(0, len(string), 10):
    result = string[i:i+10]
    print(result)