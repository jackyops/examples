#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/1 19:37'

from sqlalchemy.orm import sessionmaker

from mysql import orm_mtom

Session_class = sessionmaker(bind=orm_mtom.engine)
session = Session_class()

# b1 = orm_mtom.Book(name="Jacky Python")
# b2 = orm_mtom.Book(name="jack Python")
# b3 = orm_mtom.Book(name="tom Python")
# b4 = orm_mtom.Book(name="Luct Python")
#
# a1 = orm_mtom.Author(name="Jacky")
# a2 = orm_mtom.Author(name="Lucy")
# a3 = orm_mtom.Author(name="Tom")
#
# b1.authors = [a1, a2]
# b2.authors = [a1, a2, a3]
#
# session.add_all([b1, b2, b3, b4, a1, a2, a3])

# author_obj = session.query(orm_mtom.Author).filter(orm_mtom.Author.name=="jacky").first()
# print(author_obj.books[1].pub_date)
#
# book_obj = session.query(orm_mtom.Book).filter(orm_mtom.Book.id==1).first()
# print(book_obj.authors)
#
#
# book_obj.authors.remove(author_obj) #从一本书里删除一个作者


# 插入中文
# engine = create_engine("mysql+pymysql://jacky:123456@192.168.5.100/quansw?charset=utf8",encoding='utf-8', echo=True)
b4 = orm_mtom.Book(name="跟jacky学Python",pub_date="2017-01-12")
session.add_all([b4,])
session.commit()