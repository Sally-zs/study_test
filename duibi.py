from itertools import count
import xlrd
import xlwt
from xlwt import Workbook
from xlutils.copy import copy

excel_path1 = r"D:\\ivy_person\\study_test\\303产品整理.xlsx"  # 基础
excel_path2 = r"D:\\ivy_person\\study_test\\303前后端合并.xls"
# 被对比的文件
workbook1 = xlrd.open_workbook(excel_path1)
workbook2 = xlrd.open_workbook(excel_path2)
wb1 = copy(workbook1)
ws1 = wb1.get_sheet(0)
wb2 = copy(workbook2)
ws2 = wb2.get_sheet(0)

worksheet1 = workbook1.sheets()[0]
worksheet2 = workbook2.sheets()[0]
rows1 = worksheet1.nrows
rows2 = worksheet2.nrows
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 3  # 3为绿色
style = xlwt.XFStyle()
style.pattern = pattern
rows1 = worksheet1.nrows
rows2 = worksheet2.nrows
list = []
for i in range(0, rows1):
    nrow1 = worksheet1.row_values(i)
    # print(nrow1[1])
    list.append(nrow1)
    for j in range(0, rows2):
       nrow2 = worksheet2.row_values(j)
    #    print("nrow2",nrow2)
# print(list)
butong = []
count = 0
for j in list:
    for k in range(0, rows2):
        nrow2 = worksheet2.row_values(k)
        # print(nrow2[0],"nrow2",type(nrow2))
        # if str(j[1]) == str(nrow2[0]):
        if str(j[0]) == str(nrow2[0]):
            print(j[0], nrow2, "相同")
            ws1.write(count, 0, "{}".format(str(j[0])), style)
            # ws1.write(count, 1, "{}".format(str(j[1])), style)
            ws2.write(k, 0, "{}".format(str(nrow2)), style)
            count += 1
            # print("count", count)
            break
        # elif str(j[1]) != str(nrow2[0]) and k == rows2-1:
        elif str(j[0]) != str(nrow2[0]) and k == rows2-1:
            butong.append(j[0])
            count += 1
            # print("count", count)
    wb1.save("303产品日语.xls")
    # wb2.save("228产品日语.xlsx")
# print(butong)

# print(butong)

# file_handle = open('333.txt', mode='w')
# file_handle.write(str(butong))
#test
