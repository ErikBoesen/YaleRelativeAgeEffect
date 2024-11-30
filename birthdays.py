import yalies
import os

api = yalies.API(os.environ['YALIES_API_KEY'])

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
people = api.people(filters={'school_code': 'YC'})
birth_months = [0] * 12
for person in people:
    birth_month = person.birth_month
    if not birth_month:
        continue
    birth_months[birth_month - 1] += 1

for month, births in zip(months, birth_months):
    print(f'{month}: {births}')
