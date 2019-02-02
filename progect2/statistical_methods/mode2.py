# комментарии позже, если коротко - я тупой идиот
def mode2():
    mode = []  # 0 - число интервалов в промежутке, 1 - начение моды
    k = 0
    count = 0
    for i in points:
        if k * 0.05 < (i[0]*1000 - 50) / 1000:
            mode.append([k, count])
            count = 0
            while k * 0.05 < (i[0]*1000 - 50) / 1000:
                k += 1
            count += i[1]
        else:
            count += i[1]
    mode.append([k, count])
    just_variable = sorted(mode, key=lambda x: x[1], reverse=True)[0]
    mode = [round(just_variable[1]*1000/length)/10,
            round(((just_variable[0])*0.05 + 0.05*((just_variable[1] - mode[mode.index(just_variable)-1][1])
                                                   /((just_variable[1] - mode[mode.index(just_variable)-1][1])
                                                     +(just_variable[1] - mode[mode.index(just_variable)+1][1]))))*1000)
            / 1000]
    return mode
