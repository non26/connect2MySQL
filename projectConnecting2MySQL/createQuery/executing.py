from ..connecting import connect2MySQL
connect2MySql=connect2MySQL.connect2MySql
# from connect2MySql.connecting.connect2MySQL import connect2MySql
import xlsxwriter
import pandas as pd
import os

class createScript(connect2MySql):

    def __init__(self, script, conObj) :
        self.script=script
        self.conn=conObj
        self.conn.createCursor().execute(self.script)

    def showAll(self):
        xObj=connect2MySql.showCursor(self.conn).fetchall()
        return xObj

    def showMany(self, number):
        xObj=connect2MySql.showCursor(self.conn).fetchmany(number)
        return xObj

    def to_xlsx(self):
        xObj=connect2MySql.showCursor(self.conn).fetchall()
        column_name=connect2MySql.showCursor(self.conn).column_names
        count=connect2MySql.showCursor(self.conn).rowcount
        workbook=xlsxwriter.Workbook('result_query.xlsx', {'nan_inf_to_errors':True})
        worksheet=workbook.add_worksheet()
        amplitude=len(column_name)
        def header():
            #row=0
            for index, column in enumerate(column_name):
                worksheet.write(0, index, column)
        header()
        def write_data():
            #start at row=1
            row=1
            for item in xObj:
                for index, element in enumerate(item):
                    worksheet.write(row, index, element)
                row+=1
            workbook.close()
        write_data()



