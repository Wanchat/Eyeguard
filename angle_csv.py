import numpy as np
import csv

def angle_csv():
    with open('angle_new.csv') as f:
        data = csv.reader(f)
        for raw_angle in data:
            return raw_angle

def raw_angle():
    return [float(i) for i in angle_csv()]

def newtable():
    table = np.array(raw_angle())
    table.shape = (14,10)
    return table

# def table2line(table_new):
#     lineangle =[]
#         for l in table_new:
#             for j in l:
#                 k.append(j)        
#         return lineangle

# k =[]
#     for i in table:
#         for j in i:
#             k.append(j)

if __name__ == '__main__':
    print(newtable())