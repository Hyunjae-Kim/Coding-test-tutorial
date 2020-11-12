word= input()
print(*[word.find(chr(i)) 
      for i in range(ord('a'), ord('z')+1)])

##short coding
## list 안에서 for 돌릴때 map을 이용하면 short 코딩가능
## but, python-like coding 은 for 돌리는게 맞지 
# print(*map(input().find,
#     map(chr, range(ord('a'), ord('z')+1))))