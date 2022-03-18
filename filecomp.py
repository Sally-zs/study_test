import xlrd
from xlwt import Workbook
import json

# excel_path  = r"D:\\ivy_person\\study_test\\jiantizw.xlsx"
# workbook=xlrd.open_workbook(excel_path)
# worksheet=workbook.sheets()[0]
# rows = worksheet.nrows
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
# print(rows)
# for i in range(0,rows):
#     values = worksheet.row_values(i)
#     print(values[0])
cout = 0
with open('4.fant.json', "rb") as f:
    date = json.load(f)
print(date)
print(type(date))

list = []
list1 = []
if isinstance(date, dict):
  for k in date.keys():
    # print(k)
    if isinstance(date[k], dict):
        for i in date[k]:
            print(date[k][i], type(date[k][i]))
            if isinstance(date[k][i], str):
                list.append(date[k][i])  # 第二层的值
                # print(list)
            if isinstance(date[k][i], dict):
                for m in date[k][i]:
                    if isinstance(date[k][i][m], str):
                        list.append(date[k][i][m])  # 第三层的值
                    if isinstance(date[k][i][m], dict):
                        for s in date[k][i][m]:
                            if isinstance(date[k][i][m][s], str):
                                list.append(date[k][i][m][s])
                            if isinstance(date[k][i][m][s], dict):
                                list.append(
                                    "ddddddddddddddddddddddddddd")

# list3 = list+list1
# print("list33333",list3)
for z in list:
    # print(z)
    sheet1.write(cout, 0, str(z))
    cout += 1
    wb.save('2前端繁体.xls')
