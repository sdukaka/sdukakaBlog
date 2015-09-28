# -*- coding: utf-8 -*-

__author__ = 'sdukaka'

#基本的数据库配置 注意前面的关键字的值是db  不是databse  所以下面的key 就是需要改成db     不然是没法运行的

configs = {
    'debug': True,
    'db': {
          'host': '127.0.0.1',
          'port': 3306,
          'user': 'root',
          'password': '123456',
          'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }

}
