# from openpyxl.styles import Font, Color, Alignment, Border, Side
from openpyxl.styles import NamedStyle, Font, Border, Side, Alignment
from openpyxl import load_workbook


workbook = load_workbook('sample_data.xlsx')
sheet = workbook.active
# red_text = Font(color='00FF0000',
#                 size=32,
#                 bold=True,
#                 italic=True)
# center_aligned = Alignment(horizontal='center')
# border_side = Side(border_style='double')
# square_border = Border(top=border_side,
#                        left=border_side,
#                        right=border_side,
#                        bottom=border_side)
# sheet['A1'].font = red_text
# sheet['A3'].alignment = center_aligned
# sheet['C2'].border = square_border

# NAMED STYLES
header = NamedStyle(name='header')
header.font = Font(bold=True, size=17)
header.border = Border(bottom=Side(border_style='thick'))
header.alignment = Alignment(horizontal='center', vertical='center')

first_row = sheet[1]
for cell in first_row:
    cell.style = header

workbook.save('sample_data.xlsx')
