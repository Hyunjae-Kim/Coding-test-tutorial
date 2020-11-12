def solve(a):
    count = 0
    for i in range(1, a+1):
        
        if i<10:
            count += 1
        else:
            list_set = {int(str(i)[j+1])-int(str(i)[j]) for j in range(len(str(i))-1)}
        
            if len(list_set)==1:
                count += 1
            
    return count
    
print(solve(int(input())))

##short coding
# num = int(input())
# print(sum( (i//100 + i%10)==(i//10%10 *2) or
#        i<100 for i in range(1,num+1)))