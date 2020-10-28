alpha_num = ord(input())
a_num = ord('a')
output_list = 'a'
for i in range(a_num, alpha_num):
    alphabet = ' {}'.format(chr(i+1))
    output_list += alphabet
print(output_list)