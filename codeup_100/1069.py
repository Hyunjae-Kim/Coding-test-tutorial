grade = str(input())
grade_dict = {'A':'best!!!', 'B':'good!!',
              'C':'run!', 'D':'slowly~'}

print(grade_dict.get(grade,'what?'))