import sys
def convert_to_seconds(time_str):
    # write code here
    flag = False
    if time_str[-1] in "DdSsMmHh":
        if time_str[0:-1].isdigit():
            flag = True
        else:
            if time_str[0:-1].count(".") == 1:
                str = time_str[0:-1].split(".")
                if str[0].isdigit() or str[1].isdigit():
                    flag = True
    if (flag == True):
        if ("d" in time_str) or ("D" in time_str):
            return (float(time_str[0:-1]))*24*3600
        elif ("s" in time_str) or ("S" in time_str):
            return (float(time_str[0:-1]))
        elif ("M" in time_str) or ("m" in time_str):
            return (float(time_str[0:-1]))*60
        elif ("H" in time_str) or ("h" in time_str):
            return (float(time_str[0:-1]))*3600
    else:
        print("请以数字开头以D或d或S或s或M或m或H或h结尾")

while True:
    line = sys.stdin.readline()
    line = line.strip()
    if line == '':
        break
    print(convert_to_seconds(line))