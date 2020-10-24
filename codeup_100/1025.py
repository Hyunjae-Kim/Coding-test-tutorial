num = input()
for i in range(len(num)):
    print(('[{0:0<%d}]'%(5-i)).format(num[i]))