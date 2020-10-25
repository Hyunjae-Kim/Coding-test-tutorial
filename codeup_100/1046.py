num_list = list(map(int, input().split()))
num_sum = sum(num_list)
num_mean = num_sum/3
print('{}\n{:.1f}'.format(num_sum, num_mean))