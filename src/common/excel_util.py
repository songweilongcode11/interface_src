# coding=utf-8
import xlrd
import  xdrlib ,sys
import xlrd
class excel_util(object):
    def __init__(self, excelPath, sheetName):  
        self.data = xlrd.open_workbook(excelPath)  
        self.table = self.data.sheet_by_name(sheetName)  
        #get titles  
        self.row = self.table.row_values(0)  
        #get rows number  
        self.rowNum = self.table.nrows  
        #get columns number  
        self.colNum = self.table.ncols  
        #the current column  
        self.curRowNo = 1  
        
    #获取下一行
    def next(self):  
        r = []  
        while self.hasNext():  
            s = {}  
            col = self.table.row_values(self.curRowNo)  
            i = self.colNum  
            for x in range(i):  
                s[self.row[x]] = col[x]  
            r.append(s)  
            self.curRowNo += 1  
        return r      
    # 判断是否还有行数
    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo :
            return False
        else:
            return True


    def open_excel(self,file= 'file.xls'):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception as e:
            print (str(e))
    #根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
    def get_table_byindex(self,file= 'file.xls',colnameindex=0,by_index=0):
        data = self.open_excel(file)
        table = data.sheets()[by_index]
        nrows = table.nrows #行数
        ncols = table.ncols #列数
        colnames = table.row_values(colnameindex)#某一行数据
        if colnames is int:
            colnames = int(colnames)
        else:
            colnames =colnames
        list =[]
        for rownum in range(1,nrows):
             row = table.row_values(rownum)
             if row:
                 app = {}
                 for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                 list.append(app)
        return list

    #根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
    def get_table_byname(self,file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
        data = self.open_excel(file)
        table = data.sheet_by_name(by_name)
        nrows = table.nrows #行数
        colnames = table.row_values(colnameindex) #某一行数据
        list = []
        for rownum in range(1,nrows):
             row = table.row_values(rownum)
             if row:
                 app = {}
                 for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                 list.append(app)
        return list
    def get_rows_count_by_sheet_index(self,file= 'file.xls',sheetindex=0):
        data=self.open_excel(file)
        sheet = data.sheet_by_index(sheetindex)
        return sheet.nrows

    def get_cols_count_by_sheet_index(self,file= 'file.xls',sheetindex=0):
        data=self.open_excel(file)
        sheet = data.sheet_by_index(sheetindex)
        return sheet.ncols

    def get_cell_by_col_row(self,file= 'file.xls',colindex=0,rowsindex=0,sheetindex=0):
        data=self.open_excel(file)
        sheet = data.sheet_by_index(sheetindex)
        rows = sheet.row_values(rowsindex)
        cell_value=sheet.cell(rowsindex,colindex).value.encode('utf-8')
        print(cell_value.ctype)
        # if cell_value.ctype == 2 and cell_value.value % 1 == 0:
        #     cell_value = int(cell_value.value)
        return cell_value
