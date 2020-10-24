input_date = input()
year, month, dates = list(map(int, input_date.split('.')))
print('{:02d}-{:02d}-{:04d}'.format(dates, month, year))