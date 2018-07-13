# 목적 : 패턴, 정규식을 활용한 필터링
import re
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/6e.output.xls"

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet("jan_2013_output")

pattern = re.compile(r'(?P<my_pattern>^J.*)')
# pattern = re.compile('^J.*)

customer_name_column_index = 1
with open_workbook(input_file) as workbook_content:
    worksheet = workbook_content.sheet_by_name("january_2013")
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1, worksheet.nrows):
        row_list = []
        if pattern.search(worksheet.cell_value(row_index, customer_name_column_index)):
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook_content.datemode)
                    date_cell = date(*date_cell[0:3]).strftime("%m/%d/%Y")
                    # yyyy-mm-dd 형식을 mm-dd-yyyy형식으로 전환
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)

    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
            # output_workbook.write(행 인덱스, 열 인덱스, 데이터)
output_workbook.save(output_file)
