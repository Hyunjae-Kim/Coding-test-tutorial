from sys import stdin

while 1:
    try:
        A, B = map(int, stdin.readline().split())
        print(A+B)
    except:
        break


##stdin으로 전체 입력을 한번에 받고 
##readline으로 불러오는식이므로 다음과 같이 구현가능
##
## from sys import stdin
##
## for line in stdin:
##     A, B = map(int, line.split())
##     print(A+B)

