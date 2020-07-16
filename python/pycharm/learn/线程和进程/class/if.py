score=input("请输入分数： ")
grade=""
if 0>int(score)or int(score)>100:
    print("请输入正确分数")
    grade = "分数错误"
elif int(score)<60:
    grade = "不及格"
elif int(score)<80:
    grade = "一般"
else:
    grade = "优秀"
print('分数是{0}，等级是{1}'.format(score,grade))