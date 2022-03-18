import xlrd
from xlwt import Workbook
import json

excel_path = r"D:\\ivy_person\\study_test\\304多语言词条对齐0302 19_58.xls"
workbook = xlrd.open_workbook(excel_path)
worksheet = workbook.sheets()[0]
rows = worksheet.nrows
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
print(rows)
CN = 0
HK = 0
EN = 0
JP = 0
for i in range(0, rows):
    nrow = worksheet.row_values(i)
    # print(nrow[0])
    if "_CN" in nrow[0]:
        print(nrow[1])
        sheet1.write(HK, 0, nrow[0])
        sheet1.write(HK, 1, nrow[1])
        HK += 1
    elif "_HK" in nrow[0]:
        sheet1.write(CN, 2, nrow[0])
        sheet1.write(CN, 3, nrow[1])
        CN += 1
    elif "_EN" in nrow[0]:
        sheet1.write(EN, 5, nrow[0])
        sheet1.write(EN, 6, nrow[1])
        EN += 1
    elif "_JP" in nrow[0]:
        sheet1.write(JP, 7, nrow[0])
        sheet1.write(JP, 8, nrow[1])
        JP += 1

wb.save("304ook多语言数据处理.xls")
