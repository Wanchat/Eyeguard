from table import table_under_fit
from calc_plus import calc_under

table = table_under_fit()

def table_line(table):

    line =[]
    for i in table:
        for j in i:
            line.append(j)
    return line

table1 = table[0:1]
table2 = table[1:2]
table3 = table[2:3]
table4 = table[3:4]
table5 = table[4:5]
table6 = table[5:6]
table7 = table[6:7]
table8 = table[7:8]
table9 = table[8:9]
table10 = table[9:10]
table11 = table[10:11]
table12 = table[11:12]
table13 = table[12:13]
table14 = table[13:14]

line_1 = table_line(table1)
line_2 = table_line(table2)
line_3 = table_line(table3)
line_4 = table_line(table4)
line_5 = table_line(table5)
line_6 = table_line(table6)
line_7 = table_line(table7)
line_8 = table_line(table8)
line_9 = table_line(table9)
line_10 = table_line(table10)
line_11 = table_line(table11)
line_12 = table_line(table12)
line_13 = table_line(table13)
line_14 = table_line(table14)

def under_point_1(point):
    return calc_under(line_1, 0, point)
def under_point_2(point):
    return calc_under(line_2, 1, point)
def under_point_3(point):
    return calc_under(line_3, 2, point)
def under_point_4(point):
    return calc_under(line_4, 3, point)
def under_point_5(point):
    return calc_under(line_5, 4, point)
def under_point_6(point):
    return calc_under(line_6, 5, point)
def under_point_7(point):
    return calc_under(line_7, 6, point)
def under_point_8(point):
    return calc_under(line_8, 7, point)
def under_point_9(point):
    return calc_under(line_9, 8, point)
def under_point_10(point):
    return calc_under(line_10, 9, point)
def under_point_11(point):
    return calc_under(line_11, 10, point)
def under_point_12(point):
    return calc_under(line_12, 11, point)
def under_point_13(point):
    return calc_under(line_13, 12, point)
def under_point_14(point):
    return calc_under(line_14, 13, point)

if __name__ == '__main__':
    print(line_14)
    print(under_point_14(477))