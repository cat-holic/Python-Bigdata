# xlwt 모듈 설치
# py -m pip install xlwt

from xlrd import open_workbook
from xlwt import Workbook

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/2e.output.xls"

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            output_worksheet.write(row_index, column_index,
                                   worksheet.cell_value(row_index,
                                                        column_index))
output_workbook.save(output_file)
