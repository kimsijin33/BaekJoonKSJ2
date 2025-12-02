A = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

#print(alphabet.find(A))

#size = len(A)
size = len(alphabet)

for i in range(size):
    #print(alphabet.find(A[i]))
    print(A.find(alphabet[i]))