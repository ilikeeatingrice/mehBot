# move all db operation to this clas
import sqlite3
import random
import uuid


class DbManager(object):
    def __init__(self):
        self.conn = sqlite3.connect('./utils/botdb.sqlite')
        self.cur = self.conn.cursor()

    def get_value_from_db(self, tablename ,category):
        self.cur.execute('select value from {tablename} where category=\'{category}\''.format(tablename=tablename
                                                                                         , category=category))
        values = [x[0] for x in self.cur.fetchall()]
        if not values:
            return ""
        return random.choice(values)

    def insert_value(self, tablename, category, value):
        self.cur.execute('INSERT INTO {tablename} (pk, category, value) VALUES (\'{pk}\', \'{category}\', \'{value}\')'\
                         .format(tablename=tablename, pk= str(uuid.uuid4()), category=category, value=value.rstrip()));
        self.conn.commit()

    def retrieve_categories(self, tablename):
        self.cur.execute('select distinct category from {tablename}'.format(tablename=tablename))
        return [x[0] for x in self.cur.fetchall()]

    def __del__(self):
        self.conn.close()