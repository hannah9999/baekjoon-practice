dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = str(input())
ret = 0

for j in range(len(word)):
    for i in dial:
        if word[j] in i:
            ret += dial.index(i) + 3

print(ret)
