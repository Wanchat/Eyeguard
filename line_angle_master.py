from table import table_1, table_2
from other import loop_array
import numpy as np

from line_angle_top import top_point_1,top_point_2,top_point_3,top_point_4
from line_angle_top import top_point_5,top_point_6,top_point_7,top_point_8
from line_angle_top import top_point_9,top_point_10,top_point_11,top_point_12
from line_angle_top import top_point_13,top_point_14,top_point_15,top_point_16

from line_angle_under import under_point_1,under_point_2,under_point_3,under_point_4
from line_angle_under import under_point_5,under_point_6,under_point_7,under_point_8
from line_angle_under import under_point_9,under_point_10,under_point_11,under_point_12
from line_angle_under import under_point_13,under_point_14,under_point_15,under_point_16

table_1_master = table_1()
table_2_master  = table_2()

def line_angle_master(point):

    if point <= 220:
        if table_1_master[0] <= point < table_1_master[10]:
            top_point_1(point)
        elif table_1_master[10] <= point < table_1_master[20]:
            top_point_2(point)
        elif table_1_master[20] <= point < table_1_master[30]:
            top_point_3(point)
        elif table_1_master[30] <= point < table_1_master[40]:
            top_point_4(point)
        elif table_1_master[40] <= point < table_1_master[50]:
            top_point_5(point)
        elif table_1_master[50] <= point < table_1_master[60]:
            top_point_6(point)
        elif table_1_master[60] <= point < table_1_master[70]:
            top_point_7(point)
        elif table_1_master[70] <= point < table_1_master[80]:
            top_point_8(point)
        elif table_1_master[80] <= point < table_1_master[90]:
            top_point_9(point)
        elif table_1_master[90] <= point < table_1_master[100]:
            top_point_10(point)
        elif table_1_master[100] <= point < table_1_master[110]:
            top_point_11(point):
        elif table_1_master[110] <= point < table_1_master[120]:
            top_point_12(point)
        elif table_1_master[120] <= point < table_1_master[130]:
            top_point_13(point)
        elif table_1_master[130] <= point <= table_1_master[139]:
            top_point_14(point)
        else:
            pass

    else:
        if table_2_master[0] <= point < table_2_master[10]:
            under_point_1(point)
        elif table_2_master[10] <= point < table_2_master[20]:
            under_point_2(point)
        elif table_2_master[20] <= point < table_2_master[30]:
            under_point_3(point)
        elif table_2_master[30] <= point < table_2_master[40]:
            under_point_4(point)
        elif table_2_master[40] <= point < table_2_master[50]:
            under_point_5(point)
        elif table_2_master[50] <= point < table_2_master[60]:
            under_point_6(point)
        elif table_2_master[60] <= point < table_2_master[70]:
            under_point_7(point)
        elif table_2_master[70] <= point < table_2_master[80]:
            under_point_8(point)
        elif table_2_master[80] <= point < table_2_master[90]:
            under_point_9(point)
        elif table_2_master[90] <= point < table_2_master[100]:
            under_point_10(point)
        elif table_2_master[100] <= point < table_2_master[110]:
            under_point_11(point)
        elif table_2_master[110] <= point < table_2_master[120]:
            under_point_12(point)
        elif table_2_master[120] <= point < table_2_master[130]:
            under_point_13(point)
        elif table_2_master[130] <= point <= table_2_master[139]:
            under_point_14(point)
        else:
            pass
       

    return angle

if __name__ == '__main__':

    print(table_1_master[2])