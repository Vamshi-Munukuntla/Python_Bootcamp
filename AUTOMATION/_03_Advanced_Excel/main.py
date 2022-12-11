from openpyxl import Workbook
import random
import names

workbook = Workbook()
sheet = workbook.active

sheet['A1'] = 'Full Name'
sheet['B1'] = 'Score'

for row in range(2, 101):
    sheet['A'+str(row)] = names.get_full_name()
    sheet['B'+str(row)] = random.randint(60, 100)

workbook.save('sample_data.xlsx')
