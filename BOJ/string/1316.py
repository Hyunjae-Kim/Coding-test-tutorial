num = int(input())
count = 0

for i in range(num):
    word = input()
    set_word = set(word)
    list_word = list(word)
    word_stat=0
    for j in set_word:
        bool_word = [int(j==i) for i in list_word]
        stat = 0
        for k in bool_word:
            if stat==0 and k==1:
                stat=1
            elif stat==0 and k==0:
                continue
            elif stat==1 and k==1:
                continue
            elif stat==1 and k==0:
                stat=2
            elif stat==2 and k==0:
                continue
            elif stat==2 and k==1:
                stat=3
        if stat==3:
            word_stat=1
            break
        else:
            continue   
    if word_stat==0:
        count += 1
print(count)