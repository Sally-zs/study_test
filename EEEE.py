#新增EEE文件
#修改test2文件

#输入数字/字母  按倒序输出字母和数字

# szi = input(str())
# qucong = set(szi)
# szilist = []
# for i in qucong:
#     # a = szi.count(i)
#     # print(a)
#     szilist.append([szi.count(str(i)),i])

# for i,zf in enumerate(szilist):
#     if i == len(szilist)-1:
#         break
#     elif int(zf[0])>int(szilist[i+1][0]):
#         continue
#     else:
#         szilist[i],szilist[i+1]=szilist[i+1],szilist[i]
# print(szilist)
# a = ""
# for i in szilist:
#     a = a + i[1]
# print(a)


while True:
    try:
        a = input()
        s = sorted(a)
        # ss = sorted(s,key=lambda x:a.count(x),reverse=True)
        # print(''.join(ss))
        print(''.join(s))
    except:
        break

