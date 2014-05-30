
from storm.locals import *

class Rennen(object):
    __storm_table__ = 'rennen'
    id = Int(primary=True)
    nr = Int()
    name = Unicode()
    
class Boot(object):
    __storm_table__ = 'boot'
    id = Int(primary=True)
    bnr = Int()
    team = Unicode()
    rennen_id = Int()
    rennen = Reference(rennen_id, Rennen.id)

# extend class Rennen with a property that requires Rennen and Boot classes to be defined
Rennen.boote = ReferenceSet(Rennen.id, Boot.rennen_id)

class Lauf(object):
    __storm_table__ = 'lauf'
    id = Int(primary=True)
    typ = Unicode()
    rennen_id = Int()
    rennen = Reference(rennen_id, Rennen.id)


class Start(object):
    __storm_table__ = 'start'
    id = Int(primary=True)
    lauf_id = Int()
    lauf = Reference(lauf_id, Lauf.id)
    boot_id = Int()
    boot = Reference(boot_id, Boot.id)
    startzeit = DateTime()


def create_db(store):
    store.execute("CREATE TABLE rennen (id INTEGER PRIMARY KEY, nr INTEGER, name VARCHAR);");
    store.execute("CREATE TABLE boot (id INTEGER PRIMARY KEY, bnr INTEGER, team VARCHAR, rennen_id INTEGER REFERENCES rennen(id));");
    store.execute("CREATE TABLE lauf (id INTEGER PRIMARY KEY, typ VARCHAR, rennen_id INTEGER REFERENCES rennen(id));");
    store.execute("CREATE TABLE start (id INTEGER PRIMARY KEY, lauf_id INTEGER REFERENCES lauf(id), boot_id INTEGER REFERENCES boot(id), startzeit DATETIME);");
    store.commit();


