input()
score_list = list(map(int, input().split()))

max_score = max(score_list)
for i in range(len(score_list)):
    score_list[i] = score_list[i]/max_score*100
print(round(sum(score_list)/len(score_list), 2))

## short coding
# input()
# score_list = list(map(int, input().split()))
# print(sum(score_list)/max(score_list)/len(score_list)*100)
