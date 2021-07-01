#백준 10809 (알파벳 찾기)
import string

a_z = list(string.ascii_lowercase)
s = list(input())
for alphabet in (a_z):
    if alphabet in s:
        print(s.index(alphabet), end=" ")
    else:
        print("-1", end= " ")