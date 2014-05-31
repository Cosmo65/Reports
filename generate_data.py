#!/usr/bin/env python

from storm.locals import *

from data_def import *
from datetime import datetime, timedelta
from math import ceil

global database, store

import random

def generate_testdata(store):
    random.seed()
    startzeit = datetime(2014, 5, 30, 9, 00)
    hstartzeit = datetime(2014, 5, 31, 9, 00)
    fstartzeit = datetime(2014, 5, 31, 12, 00)
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

        if random.randint(0,1):
            # only 'Abteilung'
            l = Lauf()
            l.rennen = r
            l.typ = u'A'
            l.seq = 0
            l.startzeit = startzeit
            store.add(l)
            for anr in range(1, 1+int(ceil(b.bnr/6.0))):
                a = Abteilung()
                a.lauf = l
                a.nr = anr
                a.startzeit = startzeit
                startzeit += timedelta(minutes=5)
                store.add(a)
        else:
            # Vorlauf, Hoffnungslauf, Finale
            l = Lauf()
            l.rennen = r
            l.typ = u'V'
            l.seq = 1
            l.startzeit = startzeit
            startzeit += timedelta(minutes=5*int(ceil(b.bnr/6.0)))
            store.add(l)

            l = Lauf()
            l.rennen = r
            l.typ = u'H'
            l.seq = 2
            l.startzeit = hstartzeit
            store.add(l)
            hstartzeit += timedelta(minutes=5*int(ceil(b.bnr/6.0)))

            l = Lauf()
            l.rennen = r
            l.typ = u'F'
            l.seq = 3
            l.startzeit = fstartzeit
            store.add(l)
            fstartzeit += timedelta(minutes=5*int(ceil(b.bnr/6.0)))


if __name__ == '__main__':
    database = create_database("sqlite:test.db")
    #database = create_database("sqlite:")
    store = Store(database)

    data_def.create_db(store)
    generate_testdata(store)

    store.commit()



