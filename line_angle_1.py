from line_angle_master import line_angle
from angle_csv import raw_angle, newtable

def table_line(table):

    line =[]
    for i in table:
        for j in i:
            line.append(j)
    return line

table = newtable()

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

angle_1 = 0
angle_2 = 1
angle_3 = 2
angle_4 = 3
angle_5 = 4
angle_6 = 5
angle_7 = 6
angle_8 = 7
angle_9 = 8
angle_10 = 9
angle_11 = 10
angle_12 = 11
angle_13 = 12
angle_14 = 13

def point_1(point):
    return line_angle(line_1, angle_1, point)
def point_2(point):
    return line_angle(line_2, angle_2, point)
def point_3(point):
    return line_angle(line_3, angle_3, point)
def point_4(point):
    return line_angle(line_4, angle_4, point)
def point_5(point):
    return line_angle(line_5, angle_5, point)
def point_6(point):
    return line_angle(line_6, angle_6, point)
def point_7(point):
    return line_angle(line_7, angle_7, point)
def point_8(point):
    return line_angle(line_8, angle_8, point)
def point_9(point):
    return line_angle(line_9, angle_9, point)
def point_10(point):
    return line_angle(line_10, angle_10, point)
def point_11(point):
    return line_angle(line_11, angle_11, point)
def point_12(point):
    return line_angle(line_12, angle_12, point)
def point_13(point):
    return line_angle(line_13, angle_13, point)
def point_14(point):
    return line_angle(line_14, angle_14, point)


if __name__ == '__main__':

    print(point_1(2))