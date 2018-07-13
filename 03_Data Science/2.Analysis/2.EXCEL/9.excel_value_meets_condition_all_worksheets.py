# 목적 : 모든 워크시트에서 특정 행 필터링 하기

from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/9e.output.xls"

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet("filtered_rows_all_worksheets")

sales_column_index = 3
threshold = 2000.0

first_worksheet = True
with open_workbook(input_file) as workbook_content:
    data = []
    for worksheet in workbook_content.sheets():
        if first_worksheet:
            header_row = worksheet.row_values(0)
            data.append(header_row)
            first_worksheet = False
        for row_index in range(1, worksheet.nrows):
            row_list = []
            sale_amout = worksheet.cell_value(row_index, sales_column_index)
            sale_amout = float(str(sale_amout).replace('$', '').replace(',', ''))
            if sale_amout > threshold:
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)
                    if cell_type ==3:
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

