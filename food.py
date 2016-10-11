import sqlite3
from brownFood import *
import datetime

conn = sqlite3.connect('food.db')
c = conn.cursor()

def create_db():
    c.execute('CREATE TABLE IF NOT EXISTS FoodByDay(day TEXT PRIMARY KEY, eatery TEXT, meal TEXT, item TEXT)')

def drop_db():
    c.execute('DROP TABLE IF EXISTS FoodByDay')

def add_to_db():
    ratty = get_menu_items('sharpe-refectory')
    vdub = get_menu_items('verney-woolley')
    for meal in ratty:
        if ratty.index(meal) == 0:
            for item in meal:
                c.execute('INSERT INTO FoodByDay(day,eatery,meal,item) VALUES (?,?,?,?)', (str(datetime.datetime.now()), 'ratty', 'breakfast', item))
        elif ratty.index(meal) == 1:
            for item in meal:
                c.execute('INSERT INTO FoodByDay(day,eatery,meal,item) VALUES (?,?,?,?)', (str(datetime.datetime.now()), 'ratty', 'lunch', item))
        else:
            for item in meal:
                c.execute('INSERT INTO FoodByDay(day,eatery,meal,item) VALUES (?,?,?,?)', (str(datetime.datetime.now()), 'ratty', 'dinner', item))
    for meal in vdub:
        if vdub.index(meal) == 0:
            for item in meal:
                c.execute('INSERT INTO FoodByDay(day,eatery,meal,item) VALUES (?,?,?,?)', (str(datetime.datetime.now()), 'vdub', 'breakfast', item))
        elif vdub.index(meal) == 1:
            for item in meal:
                c.execute('INSERT INTO FoodByDay(day,eatery,meal,item) VALUES (?,?,?,?)', (str(datetime.datetime.now()), 'vdub', 'lunch', item))
        else:
            for item in meal:
                c.execute('INSERT INTO FoodByDay(day,eatery,meal,item) VALUES (?,?,?,?)', (str(datetime.datetime.now()), 'vdub', 'dinner', item))
    conn.commit()

create_db()
add_to_db()