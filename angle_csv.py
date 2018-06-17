import numpy as np
import csv

def angle_csv():
    with open('angle_new.csv') as f:
        data = csv.reader(f)
        for raw_angle in data:
            return raw_angle

raw_angle = [float(i) for i in angle_csv()]

table = np.array(raw_angle)
table.shape = (14,10)

def table_top():
    table_top = np.roll(table,6)
    table_top[0,0:6] = 0
    return table_top

def table_under():
    table_under = table + 220
    return table_under

if __name__ == '__main__':
    print(table_top())
    print(table_under())