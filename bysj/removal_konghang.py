import  openpyxl
import pandas as pd


wb = openpyxl.load_workbook('data_final_clean.xlsx')
sheet = wb.worksheets[0]
maxrow_before = sheet.max_row
list1 = list()
count=0
for i in range(1,maxrow_before):
    print(count)
    count+=1
    list1.append(sheet[i][8].value)
#获得第一列每行的value，用于判断是否为none（是否需要删除）
delete_index = 1
for i in range(len(list1)):
    if list1[i] != None:
        delete_index += 1
        print(sheet[delete_index][4].value)
    else:
        print("删除了第" + str(sheet[delete_index][4].value))
        sheet.delete_rows(idx=delete_index)






# delete_index = 1
# for i in range(0,100):
#     if row_value_list[i] != '':
#         delete_index += 1
#         print("不等于None")
#     else:
#         sheet.delete_rows(idx=delete_index)
#         print("已删除第: " + str(delete_index) + "行")
#
#
wb.save("data_final_final_clean.xlsx")