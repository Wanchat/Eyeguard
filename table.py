import numpy as np

def table_1():
    table_1 = np.arange(0, 240, 1.8)
    add_0 = np.zeros(6)
    table_1 = np.append(add_0, table_1)
    table_1[139] = 240
    return table_1

def table_2():
    table_2 = np.arange(240, 480, 1.8)
    add_480 = np.array([480, 480, 480, 480, 480, 480])
    table_2 = np.append(add_480, table_2)
    # table_2.shape = (14, 10)
    return table_2

table_1t = table_1()
table_2t = table_2()

def table_top():
    table_1t.shape = (14, 10)
    return table_1t

def table_under():
    table_2t.shape = (14, 10)
    return table_2t


if __name__ == '__main__':
    print(table_top())

