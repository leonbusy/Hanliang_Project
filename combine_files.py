import os
import openpyxl

# 获取指定目录下的所有Excel文件
def dir_excel(dpath):
    excel_names = []
    for fname in os.listdir(dpath):
        # 判断是否为 Excel文件
        if fname.endswith('.xlsx') or fname.endswith('.xls'):
            excel_names.append(fname)

    return excel_names

# 拼接Excel
def concat_excel(excel_names, dpath):
    # 新建Excel
    new_wb = openpyxl.Workbook()
    new_sheet = new_wb.active
    new_sheet.title = '全部数据'

    for i, excel_name in enumerate(excel_names):
        excel_path = os.path.join(dpath, excel_name)
        wb = openpyxl.load_workbook(excel_path)
        sheet = wb.active
        if i == 0: # 只取第一个Excel的表头
            values = list(sheet.values)
        else:
            values = list(sheet.values)[1:]
        # 添加到新的表格里
        for value in values:
            new_sheet.append(value)
    # 保存
    new_wb.save(os.path.join(dpath, 'data_final.xlsx'))


if __name__ == '__main__':
    path = r'C:\Users\43108\Desktop\文昌帝君毕业项目必过\数据'
    excel_names = dir_excel(path)
    concat_excel(excel_names, path)