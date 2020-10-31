map_list = []
for i in range(10):
    map_list.append(list(map(int, input().split())))

stat = 0
pos = [1, 1]

while 1:
    if (map_list[pos[0]+1][pos[1]]==1 and map_list[pos[0]][pos[1]+1]==1) or map_list[pos[0]][pos[1]]==2:
        map_list[pos[0]][pos[1]]=9
        break

    map_list[pos[0]][pos[1]]=9
    if map_list[pos[0]][pos[1]+1]==1:
        pos[0] += 1
    else:
        pos[1] += 1

for i in range(10):
    print(*map_list[i])
