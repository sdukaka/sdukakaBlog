# -*- coding: utf-8 -*-
__author__ = 'sdukaka'
# 测试数据库是否正常
#之前测试的时候  由于orm的地方插入语句那里没有写对 所以出了问题

import asyncio, orm
from models import User, Blog, Comment


def test(loop):
    yield from orm.create_pool(loop, user='root', password='123456', db='awesome')
    u = User(name='吴炜', email='walterwuwei@163.com', passwd='ww1925268604', image='about:blank')
    yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()