import pandas as pd
path = 'C:/Users/13781/Desktop/学生信息表.xlsx'
c=pd.read_excel(path,sheet_name=1)
print(c)
print(pd.show_versions())

