croatia_dict = ['c=', 'c-', 'd-','lj', 
                   'nj', 's=']
                   
word = input()
count = sum([word.count(i) for i in croatia_dict])
count += 2*word.count('dz=')
count += (word.count('z=')-word.count('dz='))
print(len(word)-count)