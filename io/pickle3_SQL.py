import numpy as np
import pickle as pk
import pandas as pd
import sqlite3 as sq3
import datetime as dt

path = '/test/python/'
con = sq3.connect(path + 'numbs.db')

# create = 'create table numbs (Date date, No1 real, No2 real)'
# con.execute(create)
# con.commit()

con.execute('insert into numbs values(?, ?, ?)', (dt.datetime.now(), 0.12, 7.3))
con.commit()

data = np.random.standard_normal((10000, 2)).round(5)
for r in data:
    con.execute('insert into numbs values(?,?,?)', (dt.datetime.now(), r[0], r[1]))
con.commit()

data = con.execute('select * from numbs').fetchmany(10)
con.close()
print(data)
