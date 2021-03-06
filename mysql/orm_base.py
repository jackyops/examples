#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/1 16:06'

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://jacky:123456@192.168.5.100/quansw",encoding='utf-8', echo=True)

# 生成orm基类
Base = declarative_base()

class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
    gender = Column(String(32),nullable=False)

    def __repr__(self):
        return "<%s name: %s>" %(self.name,self.password)

#创建表结构
Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例
#
# user_obj = User(name="Lucy", password="luyc123")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
# Session.commit()  # 现此才统一提交，创建数据

# 查询
# my_user = Session.query(User).filter(User.id>1).filter(User.id<3).all()
# print(my_user[0].name,my_user[0].password)
# print(my_user)

# 修改
# my_user = Session.query(User).filter_by(name="Lucy").first()
# my_user.name = "Jacky zhou"
# my_user.password = "jacky123"
# Session.commit()

# 回滚
# my_user = Session.query(User).filter_by(id=1).first()
# my_user.name = "Jack"
#
# fake_user = User(name='Rain', password='12345')
# Session.add(fake_user)
#
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 这时看session里有你刚添加和修改的数据
#
# Session.rollback()  # 此时你rollback一下
#
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 再查就发现刚才添加的数据没有了。

# Session
# Session.commit()

# 统计
# print(Session.query(User).filter(User.name.like("T%")).count())

# 分组
# from sqlalchemy import func
# print(Session.query(func.count(User.name),User.name).group_by(User.name).all() )

# 外键关联
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
#
#
# class Address(Base):
#     __tablename__ = 'addresses'
#     id = Column(Integer, primary_key=True)
#     email_address = Column(String(32), nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'))
#
#     user = relationship("User", backref="addresses")  # 这个nb，允许你在user表里通过backref字段反向查出所有它在addresses表里的关联项
#
#     def __repr__(self):
#         return "<Address(email_address='%s')>" % self.email_address


# user_obj = User(name="jackyzhou", password="zhou123",gender='M')  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id,user_obj.gender)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id,user_obj.gender)  # 此时也依然还没创建
# Session.commit()  # 现此才统一提交，创建数
