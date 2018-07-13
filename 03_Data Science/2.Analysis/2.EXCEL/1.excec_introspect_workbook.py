# 전체 워크시트 정보 확인하기
from xlrd import open_workbook

input_file = "input_files/sales_2013.xlsx"
workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
print(workbook)

for worksheet in workbook.sheets():
    print("Worksheet name : ", worksheet.name, "\tRows:",
          worksheet.nrows, "\tColumns: ", worksheet.ncols)
    print(worksheet)
