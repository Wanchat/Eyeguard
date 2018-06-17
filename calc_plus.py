def calc_top(line, angle, point):

    if line[0] < point <= line[1]:
        angle += 1.0
    elif line[1] < point <= line[2]:
        angle += 0.9
    elif line[2] < point <= line[3]:
        angle += 0.8
    elif line[3] < point <= line[4]:
        angle += 0.7
    elif line[4] < point <= line[5]:
        angle += 0.6
    elif line[5] < point <= line[6]:
        angle += 0.5
    elif line[6] < point <= line[7]:
        angle += 0.4
    elif line[7] < point <= line[8]:
        angle += 0.3
    elif line[8] < point <= line[9]:
        angle += 0.2
    elif line[9] < point <= line[10]:
        angle += 0.1 
    else:
        pass
    return angle

def calc_under(line, angle, point):

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
