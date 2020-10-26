num1, num2, num3 = list(map(int, input().split()))
print(num3 if num3<(num1 if num1<num2 
else num2) else (num1 if num1<num2 else num2))