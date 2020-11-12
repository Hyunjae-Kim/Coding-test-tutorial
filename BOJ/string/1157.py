import copy
word = input().lower()
count = list(map(word.count, set(word)))
count2 = copy.copy(count)
count2.remove(max(count2))

if len(count2)==0:
    print(list(set(word))[0].upper())
elif max(count)==max(count2):
    print('?')
else:
    print(list(set(word))[max(range(len(count)), 
        key = lambda i : count[i])].upper())


## short coding
## key를 잘 활용하자.
# word = input().upper()
# chr_set = sorted({'?', *word}, key=word.count)
# if word.count(chr_set[-1])==word.count(chr_set[-2]):
#     print('?')
# else:
#     print(chr_set[-1])