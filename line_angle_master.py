from table import table_up, table_under

from line_angle_top import top_point_1,top_point_2,top_point_3,top_point_4
from line_angle_top import top_point_5,top_point_6,top_point_7,top_point_8
from line_angle_top import top_point_9,top_point_10,top_point_11,top_point_12
from line_angle_top import top_point_13,top_point_14

from line_angle_under import under_point_1,under_point_2,under_point_3,under_point_4
from line_angle_under import under_point_5,under_point_6,under_point_7,under_point_8
from line_angle_under import under_point_9,under_point_10,under_point_11,under_point_12
from line_angle_under import under_point_13,under_point_14

table_1_master = table_up()
table_2_master  = table_under()

class MasterAngle:
    def __init__(self):
        self.angle = 0
    def masterangle(self, point):
        if point <= 220:
            if table_1_master[0] <= point < table_1_master[10]:
                self.angle = top_point_1(point)
            elif table_1_master[10] <= point < table_1_master[20]:
                self.angle = top_point_2(point)
            elif table_1_master[20] <= point < table_1_master[30]:
                self.angle = top_point_3(point)
            elif table_1_master[30] <= point < table_1_master[40]:
                self.angle = top_point_4(point)
            elif table_1_master[40] <= point < table_1_master[50]:
                self.angle = top_point_5(point)
            elif table_1_master[50] <= point < table_1_master[60]:
                self.angle = top_point_6(point)
            elif table_1_master[60] <= point < table_1_master[70]:
                self.angle = top_point_7(point)
            elif table_1_master[70] <= point < table_1_master[80]:
                self.angle = top_point_8(point)
            elif table_1_master[80] <= point < table_1_master[90]:
                self.angle = top_point_9(point)
            elif table_1_master[90] <= point < table_1_master[100]:
                self.angle = top_point_10(point)
            elif table_1_master[100] <= point < table_1_master[110]:
                self.angle = top_point_11(point)
            elif table_1_master[110] <= point < table_1_master[120]:
                top_point_12(point)
            elif table_1_master[120] <= point < table_1_master[130]:
                self.angle = top_point_13(point)
            elif table_1_master[130] <= point <= table_1_master[139]:
                self.angle = top_point_14(point)
            else:
                pass

        else:
            if table_2_master[0] <= point < table_2_master[10]:
                self.angle = under_point_1(point)
            elif table_2_master[10] <= point < table_2_master[20]:
                self.angle = under_point_2(point)
            elif table_2_master[20] <= point < table_2_master[30]:
                self.angle = under_point_3(point)
            elif table_2_master[30] <= point < table_2_master[40]:
                self.angle = under_point_4(point)
            elif table_2_master[40] <= point < table_2_master[50]:
                self.angle = under_point_5(point)
            elif table_2_master[50] <= point < table_2_master[60]:
                self.angle = under_point_6(point)
            elif table_2_master[60] <= point < table_2_master[70]:
                self.angle = under_point_7(point)
            elif table_2_master[70] <= point < table_2_master[80]:
                self.angle = under_point_8(point)
            elif table_2_master[80] <= point < table_2_master[90]:
                self.angle = under_point_9(point)
            elif table_2_master[90] <= point < table_2_master[100]:
                self.angle = under_point_10(point)
            elif table_2_master[100] <= point < table_2_master[110]:
                self.angle = under_point_11(point)
            elif table_2_master[110] <= point < table_2_master[120]:
                self.angle = under_point_12(point)
            elif table_2_master[120] <= point < table_2_master[130]:
                self.angle = under_point_13(point)
            elif table_2_master[130] <= point <= table_2_master[139]:
                self.angle = under_point_14(point)
            else:
                pass
        return self.angle

if __name__ == '__main__':

    a = MasterAngle()
    print(a.masterangle(30))
