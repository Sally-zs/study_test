# coding:utf-8
import xlrd 
from xlwt import Workbook
excel_path=r"D:\\ivy_person\\study_test\\translate.xlsx"
workbook=xlrd.open_workbook(excel_path)
worksheet=workbook.sheets()[0]
# col_list=worksheet.row_values(1,start_colx=0,end_colx=None)
# print("col_list",col_list)
rows=worksheet.nrows
cols=worksheet.ncols
print(rows,cols)
wb=Workbook()
sheet1=wb.add_sheet('Sheet 1')
cout=0
yuyan=""
for i in range(0,rows):
    # value=worksheet.col_values(i)
    # print(value)
    row_v= worksheet.row_values(i)
    #取出前置条件
    for q in row_v:
        qianzhi = row_v[0]
    #取出模块的文案
    for m in row_v:
        mokuai= row_v[1]
        leixing = row_v[2]
    #取出中文的文案
    for k in row_v:
        jianti= row_v[3]
    z=0
    for j in row_v:
        if z == int(0):
            yuyan ="繁体中文"
        elif z == int(1):
            yuyan ="英文"
        elif z == int(2): 
            yuyan ="日语"
        else:
            break
        sheet1.write(cout,1,"检查{},{}按钮悬停时{}提示语".format(mokuai,jianti,yuyan))#标题
        sheet1.write(cout,2,"p1")#用例等级
        sheet1.write(cout,3,"{}".format(qianzhi))#前置条件
        sheet1.write(cout,4,"文本")#类型
        # sheet1.write(cout,5,"1.\n2.检查{}为{}时悬停的提示语".format(mokuai,,yuyan))
        sheet1.write(cout,5,"1.{}{}\n2.检查{}为{}时悬停的提示语".format(mokuai,leixing,jianti,yuyan))#用例步骤
        sheet1.write(cout,6,"2.{}时悬停的提示语：{}".format(yuyan,row_v[z+4]))#预期结果
        z+=1
        cout+=1
        # print(cout)
    wb.save('test.xls')