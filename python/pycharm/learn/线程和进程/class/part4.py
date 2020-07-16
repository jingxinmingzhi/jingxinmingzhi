#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from pandas import DataFrame, Series
import numpy as np

# 对默认值列数据进行处理，去除空格换行等，取出默认值，对于其他异常数据，导出为-1,这些异常处理后，才能保证数据导出无误
def deal_str(s):
    s = s.replace(' ','').replace('\n','').replace('\r','').replace('\xa0','')
    if '(' in s:
        index = s.find('(')
        s = s[:index]
    try:
        s = int(s, 16)
    except ValueError:
        # default_index = s.find('0x')
        # s = s[default_index:]
        # for_index = s.find('for')
        # if for_index != -1:
        #     s = s[:for_index]
        # if s == '0x':
        #     s = '0x0'
        # s = int(s, 16)
        s = -1
    return s

# 对Byte和 Bit列数据处理， mode是对带有 - 符的数据，保留左侧，还是保留右侧数据mode=1,取左侧
def get_single_value(s, mode):
    s = str(s)
    if s == '1 (MSB)':
        s = '1'

    if len(s) > 1 and '-' in s:
        s = s.replace(' ', '').replace('\n', '').replace('\r', '').replace('\xa0', '')
        index = s.find('-')
        if mode:
            s = s[:index]
        else:
            s = s[index + 1:]
    return int(s)
# 写hex数据到文本
def write_to_txt(DID, Byte, value_list, path):
    with open(path, 'a+') as f:
        f.write('\t/*' + DID + ',' + str(Byte+1) + '*/{')
        for v in value_list:
            f.write(v)
            f.write(', ')
        f.write('0x0}')
        f.write('\n')
        f.close()


# 写十六进制结果到txt中
# 每个DID对应字典result的一个键值对 DID:[... 18-16 15-8 7-0]类似格式 ；列表中每4个字节为一个值，可能出现MSB的地方有不到4个字节

def write_result_to_txt(result, path):
    with open(path, 'w+') as f:
        f.write('{\n')
        for DID, value in result.items():
            # DID对应有多少byte，也就是size
            byte_cnt = value[0]
            # MSB不到4字节的数量
            first_byte = int(byte_cnt) % 4
            hex_value = value[1:]# 16进制结果
            f.write('\t/*' + DID + ',' + str(int(byte_cnt)+1) + '*/{')
            for i in range(len(hex_value)):
                if hex_value[i] == '-0x1':
                    f.write('error****')#异常处理
                else:
                    hex_str = hex_value[i][2:]#去除开始的0x
                    if len(hex_str) < 8:#补足数据，比如4字节可能因为数据小，不满8位16进制数
                        hex_str = '0'* (8-len(hex_str))+ hex_str
                    if i == 0 and first_byte != 0:# MSB特殊处理，保证最终写入文件的字节数和MSB的字节数一致
                        hex_str = hex_str[-first_byte*2:]
                    for j in range(len(hex_str)//2):# 循环写每一个字节
                        byte_hex_value = hex_str[j * 2:(j + 1) * 2].upper()
                        f.write('0x' + byte_hex_value + ', ')
            f.write('0x00},\n')# 写校验值

        f.write('}')
        f.close()



names = ['DID', 'Name', '22', '2E', '2F', 'Size', 'Byte', 'Bit', 'ShortName', 'Range', 'Default']
df = pd.read_excel('Prt4整理.xls', sheet_name='Sheet1',skiprows=4, names=names)


# 对缺失值和数据类型进行处理
df['ShortName'] = df['ShortName'].fillna('Reserved')
df['Range'] = df['Range'].fillna('0')
df['Default'] = df['Default'].fillna('0x0')
df = df.fillna(method='ffill')
df['Size'] = df['Size'].astype('int64')
#df.info()

# 提取默认值，bit和byte值信息，便于后续计算
df['Default Value'] = df['Default'].apply(deal_str)
df['Bit Value'] = df['Bit'].apply(get_single_value, args=(False,))
df['Byte Value'] = df['Byte'].apply(get_single_value, args=(False,))
df['Byte Value']= df['Size'] - df['Byte Value']

df_error = df.loc[df['Default Value'] == -1, ['DID','Default']]

if df_error.shape[0] != 0:
    print("处理上述默认值异常后才能生成数据！")
    print(df_error)
else:
    print("默认值无异常数据，预处理结果为preprocess.xls")
    df.to_excel('preprocess.xls')


result = {}
key = df['DID'].unique()
#key = ['C130']
for i in key:
    df2 = df.loc[df['DID'] == i]
    #print(df2)
    # 一共字节数
    byte_cnt = df2.loc[df2.index[0], 'Size']
    #print(df2)
    # 4的整数倍，将byte_cnt按4分隔的份数，不用8的原因是会出现数据溢出的情况，用无符号数是不是会好一些？
    cal_len = byte_cnt // 4 + int(byte_cnt % 4 != 0)
    hex_value = []

    for idx in range(1, cal_len+1):
        # 逐次筛选，每4个字节提取一个值
        s1 = df2['Byte Value']<(4*idx)
        s2 = df2['Byte Value']>=(4*(idx-1))
        df3 = df2[s1 & s2]
        #print(8*(df3['Byte Value']-4*(idx-1)) + df3['Bit Value'])
        #计算对应整数值
        df3 = df3['Default Value'] * pow(2, 8*(df3['Byte Value']-4*(idx-1)) + df3['Bit Value'])
        value = df3.sum()
        # 转16进制
        hex_value.append(hex(value))
    hex_value.append(str(byte_cnt))
    # 按由高字节到低字节排序
    hex_value=hex_value[::-1]

    result[i] = hex_value

write_result_to_txt(result, '解析结果.txt')
print('配置字默认值导出成功，见 解析结果.txt')