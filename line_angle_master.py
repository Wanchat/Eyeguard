from angle_csv import raw_angle, newtable
# from line_angle_1 import point_1
import line_angle_1


point = raw_angle()

def line_angle(line, angle, point):

    if line[0] < point <= line[1]:
        angle += 0.1
    elif line[1] < point <= line[2]:
        angle += 0.2
    elif line[2] < point <= line[3]:
        angle += 0.3
    elif line[3] < point <= line[4]:
        angle += 0.4
    elif line[4] < point <= line[5]:
        angle += 0.5
    elif line[5] < point <= line[6]:
        angle += 0.6
    elif line[6] < point <= line[7]:
        angle += 0.7
    elif line[7] < point <= line[8]:
        angle += 0.8
    elif line[8] < point <= line[9]:
        angle += 0.9
    elif line[9] < point <= line[10]:
        angle += 1.0 
    else:
        pass
    return angle

table = newtable()

def table_line():

    line =[]
    for i in table:
        for j in i:
            line.append(j)
    return line

line_table = table_line()


def line_angle_10(point):

    if line_table[0] < point <= line_table[10]:
        line_angle.point_1(point)
    elif line_table[10] < point <= line_table[20]:
        line_angle_1.point_2(point)
    elif line_table[20] < point <= line_table[30]:
        line_angle_3():
    elif line_table[30] < point <= line_table[40]:
        line_angle_4():
    elif line_table[40] < point <= line_table[50]:
        line_angle_5():
    elif line_table[50] < point <= line_table[60]:
        line_angle_6():
    elif line_table[60] < point <= line_table[70]:
        line_angle_7():
    elif line_table[70] < point <= line_table[80]:
        line_angle_8():
    elif line_table[80] < point <= line_table[90]:
        line_angle_9():
    elif line_table[90] < point <= line_table[100]:
        line_angle_10():
    elif line_table[100] < point <= line_table[110]:
        line_angle_11():
    elif line_table[110] < point <= line_table[120]:
        line_angle_12():
    elif line_table[120] < point <= line_table[130]:
        line_angle_13():
    elif line_table[130] < point <= line_table[133]:

        if 213.5 < point <= 215.0:
            angle = 0.4
        elif 215.0 < point <= 216.5:
            angle = 0.3
        elif 216.5 < point <= 218.5:
            angle = 0.2
        elif 218.5 < point <= 220.0:
            angle = 0.1
    else:
        pass

    return angle


def main():
    pass

if __name__ == '__main__':
    table = newtable()
    # table = table[0:1]

    # line_1 = table_line()
    line = table_line()

    angle = 10

    point = 2

    print(line[130])