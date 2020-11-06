case_n = int(input())
for i in range(case_n)
    num, *score, = map(int, input().split())
    mean_ = sum(score)/num

    ratio = sum(list(map(lambda i: i>mean_, score)))/num
    print('{:.3f}%'.format(ratio))