#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/1 18:56'

from sqlalchemy.orm import sessionmaker

from mysql import orm_many_fk

Session_class = sessionmaker(bind=orm_many_fk.engine)
session = Session_class()

# addr1 = orm_many_fk.Address(street="beiji",city="bj",state="bj")
# addr2 = orm_many_fk.Address(street="zhixing",city="nanz",state="ng")
# addr3 = orm_many_fk.Address(street="gz",city="zh",state="biaoan")
#
# session.add_all([addr1,addr2,addr3])
#
# c1 = orm_many_fk.Customer(name="jacky",billing_address=addr1,shipping_address=addr2)
# c2 = orm_many_fk.Customer(name="Tom",billing_address=addr3,shipping_address=addr3)
#
# session.add_all([c1,c2])

obj = session.query(orm_many_fk.Customer).filter(orm_many_fk.Customer.name=="jacky").first()
print(obj.name,obj.billing_address,obj.shipping_address)

session.commit()