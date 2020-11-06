from sys import stdin

input()
def f(a):
    if type(a)==str:
        a=len(a)

    if a <=1:
        return a
    else:
        return a + f(a-1)

for line in stdin:
    line_ = list(map(f, line.rstrip().split('X')))
    print(sum(line_))


## short coding
## n 재귀함수 대신 n*-~n//2 로 1~n 까지의 합 계산가능