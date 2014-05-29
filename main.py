#!/usr/bin/env python

from storm.locals import *


class Person(object):
    __storm_table__ = 'person'
    id = Int(primary=True)
    name = Unicode()


database = create_database("sqlite:test.db")
store = Store(database)


