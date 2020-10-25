num1, num2 = list(map(int, input().split()))
print('{}\n{}\n{}\n{}\n{}\n{:.2f}'.format(
    num1+num2, num1-num2, num1*num2, 
    int(num1/num2), num1%num2, num1/num2))