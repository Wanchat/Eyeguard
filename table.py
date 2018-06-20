import numpy as np

def table_up():
    table_up = np.arange(0, 240, 1.8)
    add_0 = np.zeros(6)
    table_up = np.append(add_0, table_up)
    table_up[139] = 240
    return table_up

def table_under():
    table_under = np.arange(240, 480, 1.8)
    add_480 = np.array([480, 480, 480, 480, 480, 480])
    table_under = np.append(table_under, add_480)
    return table_under

def table_up_fit():
    table_up_fit = table_up()
    table_up_fit.shape = (14, 10)
    return table_up_fit

def table_under_fit():
    table_under_fit = table_under()
    table_under_fit.shape = (14, 10)
    return table_under_fit

class Table:

    def table_up(self):
        table_up = np.arange(0, 240, 1.8)
        add_0 = np.zeros(6)
        table_up_new = np.append(add_0, table_up)
        table_up_new[139] = 240
        return table_up_new

    def table_up_fit(self):
        table_up_fit = self.table_up()
        table_up_fit.shape = (14, 10)
        return table_up_fit

    def table_under(self):
        table_under = np.arange(240, 480, 1.8)
        add_480 = np.array([480, 480, 480, 480, 480, 480])
        table_under = np.append(table_under, add_480)
        return table_under

    def table_under_fit(self):
        table_under_fit = self.table_under()
        table_under_fit.shape = (14, 10)
        return table_under_fit

if __name__ == '__main__':
    print(table_under_fit())
