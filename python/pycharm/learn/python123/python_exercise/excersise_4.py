import sys
def parse_http_datetime(s):
    datetime=""
    month=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    if "GMT" in s and "-" not in s:
        a=s.split(" ")
        y= a[3]
        if (month.index(a[2])+1)<10:
            m= str("0"+str(month.index(a[2])+1))
        else:
            m=str(month.index(a[2])+1)
        d=a[1]
        t=a[4]
        datetime=y+"-"+m+"-"+d+" "+t
    elif "GMT" in s and "-"  in s:
        a=s.split(" ")
        y= "19"+a[1].split("-")[2]
        if (month.index(a[1].split("-")[1])+1)<10:
            m= str("0"+str(month.index(a[1].split("-")[1])+1))
        else:
            m=str(month.index(a[1].split("-")[1])+1)
        d=a[1].split("-")[0]
        t=a[2]
        datetime=y+"-"+m+"-"+d+" "+t
    elif "GMT" not in s and "-" not in s:
        a=s.split(" ")
        y= a[5]
        if (month.index(a[1])+1)<10:
            m= str("0"+str(month.index(a[1])+1))
        else:
            m=str(month.index(a[1])+1)
        if  int(a[3])<10:
            d="0"+a[3]
        else:
            d=a[3]
        t=a[4]
        datetime=y+"-"+m+"-"+d+" "+t
    return datetime

while True:
    line = sys.stdin.readline()
    line = line.strip()
    if line == '':
        break
    print(parse_http_datetime(line))

