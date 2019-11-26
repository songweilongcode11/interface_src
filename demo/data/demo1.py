import xlrd
data = xlrd.open_workbook("./login.xls") #打开excel
table = data.sheet_by_name("Sheet1") #读sheet
nrows = table.nrows
cols = table.ncols
nos = []
for i in range(1,nrows):  #指定从1开始，到最后一列，跳过表头
    for j in range(cols):
        ctype = table.cell(i , j).ctype #判断python读取的返回类型  0 --empty,1 --string, 2 --number(都是浮点), 3 --date, 4 --boolean, 5 --error
        no = table.cell(i, j).value #获取单元格的值
        if ctype == 2 :
            no = str(int(no)) #将浮点转换成整数再转换成字符串
        nos.append(no)
print(nos)

