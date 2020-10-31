num = input()
num_deci = int(num, 16)
for i in range(1,16):
    result = num_deci*i
    print('{}*{}={}'.format(num, 
    hex(i).upper()[2:], hex(result).upper()[2:]))
