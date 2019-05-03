import sqlite3
import uuid
import random
import os

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

categoryList = []

def file2sqlite(filename, tablename, category):
    with open(filename, encoding='utf8') as f:
        count = 0
        for line in f:
            if count > 500:
                return
            count = count+1
            print ("INSERT INTO {tablename} (pk, category, value) VALUES (\"{pk}\", \"{category}\", \"{value}\")"\
                        .format(tablename=tablename, pk= str(uuid.uuid4()), category= category, value=line.rstrip()))
            cur.execute("INSERT INTO {tablename} (pk, category, value) VALUES (\"{pk}\", \"{category}\", \"{value}\")"\
                        .format(tablename=tablename, pk= str(uuid.uuid4()), category= category, value=line.rstrip().replace("'", "\'")))


for dir in os.listdir("."):
    parts = dir.split("_")
    tempCate = parts[-1]
    if tempCate in categoryList:
        tempCate = parts[-2]+"_"+parts[-1]
        if tempCate in categoryList:
            continue
    categoryList.append(tempCate)
    for r, d, f in os.walk(dir):
        for file in f:
            if '.txt' in file:
                file2sqlite(os.path.join(r, file), "pictures", tempCate)

# tsv2sqlite("D:\personal_git\wallpapers.tsv", "pictures")
# tsv2sqlite("D:\personal_git\memes.tsv", "pictures")
conn.commit()

cur.execute('select count(*) from pictures')
values=[x[0] for x in cur.fetchall()]

cur.execute('select value from {tablename} where category=\'{category}\''.format(tablename= "memes"
                                                                                      , category="sacred"))

conn.close()