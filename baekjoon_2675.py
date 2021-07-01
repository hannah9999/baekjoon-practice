#백준 2675번(문자열 반복)
n = int(input())

for _ in range(n):
    r, s = list(input().split()) 
    for letter in s:
        print(int(r)*letter, end= "")
    print()
