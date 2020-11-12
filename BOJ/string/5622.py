def check(a):
    if a<='R':
        dtime = (ord(a)-65)//3 + 3
    elif a>'R' and a<='V':
        dtime = (ord(a)-66)//3 + 3
    else:
        dtime = 10
    return dtime

time_list = map(check, input())
print(sum(time_list))

##short coding
##중간에 하나씩 예외있는걸 커버하기위해 * 하고 //
## & 최대값 제한하기위해 min
## example
# print(sum(min(ord(c)-64,25)*28//89+3for c in input()))
## or pythonic 하게
## 예외부분에대한 boolean 체크
#print(sum((ord(c)-56)//3-(c in"SVYZ")for c in input()))