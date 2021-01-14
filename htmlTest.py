#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/6/10 17:25
# @Email   : 1370465454@qq.com
# @File    :
# @Description:
import xlrd
import xlwt
import os
import time
from openpyxl import load_workbook

strtime = time.strftime('%Y-%m-%d_%H_%M_%S')

# def readExcelDataByName(filename, sheetName):
#     '''读取Excel文件和表名'''
#     wb = xlrd.open_workbook(filename)
#     # sheet=data.sheet_by_index(0)#通过索引顺序获取，0表示第一张表
#     # sheets = data.sheet_names()#获取文件中的表名
#     sheet = wb.sheet_by_name(sheetName)
#     ncols = sheet.ncols
#     # 获取行数
#     nrows = sheet.nrows
#     print("nrows %d, ncols %d" % (nrows, ncols))
#     total_data=url_list=[]

#     #读取url
#     for m in range(0,nrows):
#         # print(sheet.cell_value(m,1))
#         # print(sheet.cell_value(m,2))
#         # print(sheet.cell_value(m,3))
#         # print(sheet.cell_value(m,5))
#         url_list.append(sheet.cell_value(m,1))
#         url_list.append(sheet.cell_value(m,3))
#         url_list.append(sheet.cell_value(m,2))
#         url_list.append(sheet.cell_value(m,5))
#         total_data.append(url_list)
#         # print(url_list)
#         url_list=[]

#     # print(total_data)
#     return total_data
import xlrd

import unittest

import ddt


class ExcelUtil(object):

    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)

        # get titles
        self.row = self.table.row_values(0)

        # get rows number
        self.rowNum = self.table.nrows
        print(self.rowNum)
        # get columns number
        self.colNum = self.table.ncols
        print(self.colNum)

        # the current column
        self.curRowNo = 1

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
        print(r)
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True
            # if __name__ == '__main__':
        # readExcelDataByName('TestCase.xlsx', 'TestCase')


# ExcelUtil=ExcelUtil("TestCase.xlsx", "TestCase")
# ExcelUtil.next()


excel = ExcelUtil("TestCase.xlsx", "TestCase")


# excel.next()

@ddt.ddt
class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start')

    @classmethod
    def tearDownClass(cls):
        print('stop')

    @ddt.data(*excel.next())
    def testLogin(self, data):
        print(data['Request URL'])
        print(data['Request Method'])
        print(data['Request Data'])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    unittest.TextTestRunner(verbosity=2).run(suite)