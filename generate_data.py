#!/usr/bin/env python

from storm.locals import *

from data_def import *

global database, store

import random

def generate_testdata(store):
    random.seed()
    for nr in range(1, random.randint(5,10)):
        r = Rennen()
        r.nr = nr
        r.name = u"Rennen {nr}".format(nr=nr)
        store.add(r)
        for bnr in range(1, random.randint(4,20)):
            b = Boot()
            b.bnr = bnr
            b.rennen = r
            b.team = u"Rennen {r} Boot {b}".format(r=nr, b=bnr)
            store.add(b)

if __name__ == '__main__':
    database = create_database("sqlite:test.db")
    #database = create_database("sqlite:")
    store = Store(database)

    data_def.create_db(store)
    generate_testdata(store)

    store.commit()



