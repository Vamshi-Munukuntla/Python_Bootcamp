from openpyxl.utils import FORMULAE
from openpyxl import load_workbook

spreadsheet = load_workbook('sample_data.xlsx')
sheet = spreadsheet.active

# TOTAL SCORE
sheet['C2'] = "Total"
sheet['D2'] = "=Sum(B2:B100)"

# AVERAGE SCORE
sheet['C3'] = 'Average'
sheet['D3'] = "=AVERAGE(B2:B100)"

# SCORE more than 80
sheet['C4'] = 'More than 80'
sheet['D4'] = '=COUNTIF(B2:B100,">80")'

# Activating filters to the spreadsheet
sheet.auto_filter.ref = sheet.dimensions
spreadsheet.save('sample_data.xlsx')

