import sqlite3
import uuid
import random

conn = sqlite3.connect('botdb.sqlite')
cur = conn.cursor()
createTableStatementTemplate = 'CREATE TABLE {tablename} (pk {pk}, category {category},value {value})'
dropTableStatementTemplate = 'DROP TABLE {tablename}'
tablenames = ['pictures']

cur.execute(dropTableStatementTemplate.format(tablename='memes'))
cur.execute(createTableStatementTemplate.format(tablename="memes", pk='TEXT', category='TEXT', value='adLongVarWChar'))


for tablename in tablenames:
    print(dropTableStatementTemplate.format(tablename = tablename))
    cur.execute(dropTableStatementTemplate.format(tablename=tablename))

for tablename in tablenames:
    print(createTableStatementTemplate.format(tablename=tablename, pk='TEXT', category='TEXT', value='TEXT'))
    cur.execute(createTableStatementTemplate.format(tablename=tablename, pk='TEXT', category='TEXT', value='TEXT'))

def tsv2sqlite(filepath, tablename):
    with open(filepath, encoding='utf8') as f:
        for line in f:
            parts = line.split("\t")
            print('INSERT INTO {tablename} (pk, category, value) VALUES (\'{pk}\', \'{category}\', \'{value})\')'\
                        .format(tablename=tablename, pk="1", category=parts[0], value=parts[1]))
            cur.execute('INSERT INTO {tablename} (pk, category, value) VALUES (\'{pk}\', \'{category}\', \'{value}\')'\
                        .format(tablename=tablename, pk= str(uuid.uuid4()), category=parts[0], value=parts[1].rstrip()))



tsv2sqlite("D:\personal_git\wallpapers.tsv", "pictures")
tsv2sqlite("D:\personal_git\memes.tsv", "pictures")
conn.commit()

cur.execute('select value from memes where category=\'sacred\'')
values=[x[0] for x in cur.fetchall()]

cur.execute('select value from {tablename} where category=\'{category}\''.format(tablename= "memes"
                                                                                      , category="sacred"))
values = [x[0] for x in cur.fetchall()]
print (random.choice(values))


conn.close()