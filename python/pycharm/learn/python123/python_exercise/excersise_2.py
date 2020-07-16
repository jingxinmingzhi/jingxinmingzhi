import datetime
import sys


def next_day(date_str):
    flag = False
    if date_str.count("-") ==2:
        data = date_str.split("-")
        if data[0].isdigit() and data[1].isdigit() and data[2].isdigit():
            if int(data[2])<=31 and int(data[2])>=1 and int(data[1])<=12 and int(data[1])>=1:
                flag = True
    else:
        flag = False
    if(flag == True):
        data = date_str.split("-")
        if int(data[2]) ==28 or int(data[2]) ==29 or int(data[2]) ==30 or int(data[2]) ==31:
            if int(data[2])==28:
                if int(data[1]) == 2:
                    if int(data[0]) % 4 == 0:
                        data[2] = str(int(data[2]) + 1)
                    else:
                        data[2] = "01"
                        if int(data[1])==12:
                            data[1]="01"
                            data[0]=str(int(data[0])+1)
                        else:
                            data[1]=str(int(data[1])+1)
                else:
                    data[2] = str(int(data[2]) + 1)
            elif int(data[2])==29:
                if int(data[1]) == 2:
                    if int(data[0]) % 4 == 0:
                        data[2] = "01"
                        if int(data[1]) == 12:
                            data[1] = "01"
                            data[0] = str(int(data[0]) + 1)
                        else:
                            data[1] = str(int(data[1]) + 1)
                    else:
                        print("平年2月没有29日")
                        return
                else:
                    data[2] = str(int(data[2]) + 1)
            elif int(data[2]) == 30:
                if int(data[1]) == 1 or int(data[1]) == 3 or int(data[1]) == 5 or int(data[1]) == 7 or int(data[1]) == 8 or int(data[1]) == 10 or int(data[1]) == 12:
                    data[2] = str(int(data[2]) + 1)
                elif int(data[1]) == 2:
                    print("2月没有30号")
                    return
                else:
                    data[2] = "01"
                    if int(data[1]) == 12:
                        data[1] = "01"
                        data[0] = str(int(data[0]) + 1)
                    else:
                        data[1] = str(int(data[1]) + 1)
            elif int(data[2]) == 31:
                if int(data[1]) == 1 or int(data[1]) == 3 or int(data[1]) == 5 or int(data[1]) == 7 or int(data[1]) == 8 or int(data[1]) == 10 or int(data[1]) == 12:
                    data[2] = "01"
                    if int(data[1]) == 12:
                        data[1] = "01"
                        data[0] = str(int(data[0]) + 1)
                    else:
                        data[1] = str(int(data[1]) + 1)
                else:
                    print("除大月外的月份没有30号")
                    return
        else:
            data[2]=str(int(data[2])+1)
        if int(data[2])<10:
            if "0" not in data[2]:
                data[2]="0"+data[2]
        if int(data[1])<10:
            if "0" not in data[1]:
                data[1]="0"+data[1]
        return "-".join(data)
    else:
        print("请输入正确的日期")
def prev_day(date_str):
    flag = False
    if date_str.count("-") == 2:
        data = date_str.split("-")
        if data[0].isdigit() and data[1].isdigit() and data[2].isdigit():
            if int(data[2]) <= 31 and int(data[2]) >= 1 and int(data[1]) <= 12 and int(data[1]) >= 1:
                flag = True
    else:
        flag = False
    if (flag == True):
        data = date_str.split("-")
        if int(data[2])==1:
            if int(data[1])==1:
                data[0]=str(int(data[0])-1)
                data[1]="12"
                data[2]="31"
            elif int(data[1])==2 or int(data[1])==4 or int(data[1])==6 or int(data[1])==8 or int(data[1])==9 or int(data[1])==11:
                data[1]=str(int(data[1])-1)
                data[2] = "31"
            elif int(data[1]) == 3:
                if int(data[0]) % 4 == 0:
                    data[2] = "29"
                    data[1]="2"
                else:
                    data[2] = "28"
                    data[1] = "2"
            else:
                data[1] = str(data[1] - 1)
                data[2] = "30"
        else:
            data[2] = str(int(data[2]) - 1)
        if int(data[2])<10:
            if "0" not in data[2]:
                data[2]="0"+data[2]
        if int(data[1])<10:
            if "0" not in data[1]:
                data[1]="0"+data[1]
        return "-".join(data)
    else:
        print("请输入正确的日期")

while True:
    line = sys.stdin.readline()
    line = line.strip()
    if line == '':
        break
    print('前一天:', prev_day(line))
    print('后一天:', next_day(line))