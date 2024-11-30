import csv


months = [0] * 12
with open('US_births_2000-2014_SSA.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        month = int(row['month'])
        births = int(row['births'])
        months[month - 1] += births

for births in months:
    print(births)
