# Day3 条件判断练习：成绩等级判断
score = 85  # 可以自己改分数测试

# 单if判断
if score >= 60:
    print("恭喜，成绩及格！")

# if-else判断
if score >= 90:
    grade = "优秀"
else:
    grade = "未达优秀"
print(f"成绩等级：{grade}")

# if-elif-else多条件判断
if score >= 90:
    final_grade = "优秀"
elif score >= 80:
    final_grade = "良好"
elif score >= 60:
    final_grade = "及格"
else:
    final_grade = "不及格"
print(f"最终评级：{final_grade}")