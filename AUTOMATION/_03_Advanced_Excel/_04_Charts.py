from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

spreadsheet = Workbook()
sheet = spreadsheet.active
rows = [
    ['Book Name', 'Paperback', 'Ebook'],
    ['DSA Swift', 40, 50],
    ['DSA Java', 50, 45],
    ['DSA Python', 70, 150],
    ['DSA C++', 72, 90],
    ['Python for Kids', 240, 350],
    ['C#', 35, 30],
]

for row in rows:
    sheet.append(row)


chart = BarChart()
data = Reference(worksheet=sheet,
                 min_row=1, max_row=7,
                 min_col=2, max_col=3)

chart.add_data(data, titles_from_data=True)
sheet.add_chart(chart, "F2")

spreadsheet.save('books_data.xlsx')
