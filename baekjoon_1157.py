word = input().lower()
word_list = list(set(word))

cnt = []

for letter in word_list:
    cnt.append(word.count(letter))

if cnt.count(max(cnt)) > 1:
    print("?")

else:
    
    print(word_list[cnt.index(max(cnt))].upper())
    
 


