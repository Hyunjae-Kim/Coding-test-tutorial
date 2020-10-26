month = int(input())
if month<3 or month==12:
    print('winter')
elif month<6:
    print('spring')
elif month<9:
    print('summer')
else:
    print('fall')