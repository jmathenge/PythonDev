import sqlite3 as sq
import pandas as pd
import matplotlib.pyplot as plt
import time

connection = sq.connect("testSQLDB")
pos = connection.cursor()


def graph_data():
    pos.execute('SELECT id, price FROM equipment')
    data = pos.fetchall()

    ids = []
    prices = []
    
    for row in data:
        ids.append(row[0])
        prices.append(row[0])
    
    plt.plot(ids,prices)
    
    plt.show()

#graph_data()


ls = [5,4,7,8,2,6,10,9]
d = [x for x in ls if x%2 == 0]
print(d)

def add(a,b):
    print(a+b)
    
print("New statement")
