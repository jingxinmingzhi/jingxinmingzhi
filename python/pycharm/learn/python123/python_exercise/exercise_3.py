import datetime
def date_delta(start, end):
    a=datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
    b=datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
    return float(((b-a).seconds)+(b-a).days*24*3600)
start = input()  # sys.stdin.readline()
end = input()  # sys.stdin.readline()

print(date_delta(start, end))