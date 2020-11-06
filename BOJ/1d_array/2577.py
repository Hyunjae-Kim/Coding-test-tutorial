num1, num2, num3 = map(int, [input() for i in range(3)])
*num, = str(num1*num2*num3)

for i in range(10):
    print(sum(map(lambda j:int(j)==i,num)))


## short coding
## count 함수가 있음...
## eval 혹은 exec을 써서 인풋받는거 구현가능
# num = str(eval('1'+'*int(input())'*3))

# for i in range(10):
#     print(num.count(str(i)))
