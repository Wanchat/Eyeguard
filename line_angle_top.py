from table import table_up_fit
from calc_plus import calc_top
from other import loop_array

table = table_up_fit()
#
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

line_1 = loop_array(table1)
line_2 = loop_array(table2)
line_3 = loop_array(table3)
line_4 = loop_array(table4)
line_5 = loop_array(table5)
line_6 = loop_array(table6)
line_7 = loop_array(table7)
line_8 = loop_array(table8)
line_9 = loop_array(table9)
line_10 = loop_array(table10)
line_11 = loop_array(table11)
line_12 = loop_array(table12)
line_13 = loop_array(table13)
line_14 = loop_array(table14)

def top_point_1(point):
    return calc_top(line_1, 13, point)
def top_point_2(point):
    return calc_top(line_2, 12, point)
def top_point_3(point):
    return calc_top(line_3, 11, point)
def top_point_4(point):
    return calc_top(line_4, 10, point)
def top_point_5(point):
    return calc_top(line_5, 9, point)
def top_point_6(point):
    return calc_top(line_6, 8, point)
def top_point_7(point):
    return calc_top(line_7, 7, point)
def top_point_8(point):
    return calc_top(line_8, 6, point)
def top_point_9(point):
    return calc_top(line_9, 5, point)
def top_point_10(point):
    return calc_top(line_10, 4, point)
def top_point_11(point):
    return calc_top(line_11, 3, point)
def top_point_12(point):
    return calc_top(line_12, 2, point)
def top_point_13(point):
    return calc_top(line_13, 1, point)
def top_point_14(point):
    return calc_top(line_14, 0, point)

if __name__ == '__main__':
    print(line_14)
    print(top_point_14(225))