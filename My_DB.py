from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.Qt import QMessageBox


class MyDb(object):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('zhgl.db')
    query = QSqlQuery()

    def loaddb(self, sql):
        if not self.db.open():
            return False
        if self.query.exec_(sql):
            return self.query
            self.db.close()
        else:
            return 0  #当SQl语句执行失败返回一个标识0，让后后续代码捕获并作出相应的处理。


    def columnRow(self):
        datacolumn = self.query.record().count()
        datarow = 0
        if self.query.last():
            datarow = self.query.at() + 1
        # 把索引指向回第一条的上一条。这样next() 第一次才能指向第一条。
        self.query.first()
        self.query.previous()
        return (datacolumn, datarow)


'''测试代码'''
# MyDb().loaddb('SELECT * FROM "Test"')
# print(MyDb.columnRow())
# my_db = MyDb()
# data = my_db.loaddb('SELECT * FROM "Test"')
# print(my_db.columnRow())
#
# my_db1 = MyDb()
# data = my_db1.loaddb('SELECT * FROM "Paypal信息"')
# print(my_db1.columnRow())
# # 表的列数
# print(type(data.record().count()))
# print(data.record().count())
# # 表的行数
# i = 0
# while data.next():
#     i += 1
# print(i)
# print(data.size())
# 通过索引名称找到对应的值
# id_index = data.record().indexOf('Id')
# # name_index = data.record().indexOf('Name')
# # age_index = data.record().indexOf('Age')
# # while data.next():
# #     id = data.value(id_index)
# #     name = data.value(name_index)
# #     age = data.value(age_index)
# #     print(id, name, age)
# 通过
# id_index = data.record().indexOf('Id')
# name_index = data.record().indexOf('Name')
# age_index = data.record().indexOf('Age')
# while data.next():
#     id = data.value(0)
#     name = data.value(1)
#     age = data.value(2)
#     print(id, name, age)
