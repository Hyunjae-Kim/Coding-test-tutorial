for i in range(int(input())):
    repeat, word = input().split()
    print(''.join([i*int(repeat) for i in word]))