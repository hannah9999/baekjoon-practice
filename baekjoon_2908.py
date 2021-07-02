a ,b = map(int, input().split())
s_a = int(str(a) [::-1])
s_b = int(str(b) [::-1])
lst = [s_a, s_b]
print(max(lst))