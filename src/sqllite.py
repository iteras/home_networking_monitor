#!/usr/bin/env python

import sqlite3

db = "SmartHome.db"


class Sqlite(object):

    class ds:
        def __init__(self):
            self.conn = sqlite3.connect(db)
            self.c = self.conn.cursor()

        def insert_into(self,table,**kwargs):
            self.c.execute('INSERT INTO sbc_temperature ("up_time","ts","temp") VALUES (1800,1530127445,18.6);')

        def commit(self):
            self.conn.commit()
            self.conn.close()

test = Sqlite.ds()
test.insert_into(table="sbc_temperature")
test.commit()