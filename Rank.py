#!/usr/bin/env python
#coding=utf-8

import sqlite3
import xlrd

conn = sqlite3.connect('jingji.db')
c = conn.cursor()
c.execute('''create table if not exists student
         (sid text primary key NOT NULL, sname text, jqf1 real,credit1 real,jqf2 real,credit2 real)''')
#c.execute('drop table student')
class FileDispose(object):
    def __init__(self,file):
        super(FileDispose,self).__init__()
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()
        self.credit1 = 48
        self.credit2 = 39.5

    def ___del__(self):
        self.cursor.close()
        self.conn.close()

    def insert(self,sid,sname,jqf,credit):
        s = (sid,sname,jqf,self.credit1)
        sql = 'insert into student(sid,sname,jqf1,credit1)values(?,?,?,?) '
        self.cursor.execute(sql,s)
        self.conn.commit()

    def update(self,file):
        data = xlrd.open_workbook(file)
        table = data.sheets()[0]
        for rowid in range(5,55):
            row = table.row_values(rowid)
            sid = row[1]
            s = (row[25], self.credit2,sid)
            print(s)
            sql = 'update student set jqf2=?,credit2 = ? where sid == ?'
            self.cursor.execute(sql,s)
            self.conn.commit()

    def readFile(self,file):
        data = xlrd.open_workbook(file)
        table = data.sheets()[0]
        for rowid in range(1,158):
            row = table.row_values(rowid)
            if(row):
                print row
                self.insert(row[1],row[2],row[3],self.credit1)

fd = FileDispose('jingji.db')
fd.readFile('/home/dong/Desktop/jingji2.xlsx')
fd.update('/home/dong/Desktop/jingji1.xlsx')
c.execute('delete from student where credit2 is NULL')
table = c.execute('''
select sid,sname,jqf1,jqf2,(credit1*jqf1+credit2*jqf2)/(credit1+credit2) as jqf from student order by jqf desc;
''')
for row in table:
    print row
c.close()
