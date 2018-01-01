#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/1 17:12'


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
engine = create_engine("mysql+pymysql://jacky:123456@192.168.5.100/quansw",encoding='utf-8', echo=True)

# 生成orm基类
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    reginter_date  = Column(DATE,nullable=False)

    def __repr__(self):
        return "<%s name: %s>" %(self.id,self.name)

class StudyRecord(Base):
    __tablename__ = 'study_record' #表名
    id = Column(Integer, primary_key=True)
    day  = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey('student.id'))

    student = relationship("Student",backref="my_student_record")


    def __repr__(self):
        return "<%s day: %s status: %s >" % (self.student.name, self.day,self.status)

#创建表结构
Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例
#
# s1 = Student(name="Jacky",reginter_date="2017-01-22")
# s2 = Student(name="Tom",reginter_date="2014-01-22")
# s3 = Student(name="Lucy",reginter_date="2015-01-02")
# s4 = Student(name="Stuent",reginter_date="2016-01-22")
#
# study_ojb1 = StudyRecord(day=1,status="YES",stu_id=1)
# study_ojb2 = StudyRecord(day=2,status="No",stu_id=1)
# study_ojb3 = StudyRecord(day=3,status="YES",stu_id=1)
# study_ojb4 = StudyRecord(day=3,status="YES",stu_id=2)
#
# session.add_all([s1,s2,s3,s4,study_ojb1,study_ojb2,study_ojb3,study_ojb4])

# stu_obj = session.query(Student).filter(Student.name=="jacky").first()
stu_obj = session.query(Student).filter(Student.name=="jacky").first()
print(stu_obj.my_student_record)


session.commit()