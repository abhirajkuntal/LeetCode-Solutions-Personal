def max_69_num(num):

    str_num = str(num)

    for i in range(len(str_num)):
        if str_num[i] == "6":

            str_num = str_num[:i] + "9" + str_num[i+1:]
            break

    return int(str_num)

num = 9669

print(max_69_num(num))
