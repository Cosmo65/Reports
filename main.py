#!/usr/bin/env python

from storm.locals import *

import data_def


if __name__ == "__main__":
    #database = create_database("sqlite:test.db")
    database = create_database("sqlite:")
    store = Store(database)

    data_def.create_db(store)

    store.commit()



