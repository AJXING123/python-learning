# Day4 列表&字典练习
# ========== 列表操作 ==========
print("===== 列表操作 =====")
# 定义列表
student_list = ["张三", "李四", "王五"]
print("原始列表：", student_list)

# 添加元素
student_list.append("赵六")
print("添加后：", student_list)

# 取值
print("第二个学生：", student_list[1])

# 删除元素
del student_list[2]
print("删除第三个元素后：", student_list)

# ========== 字典操作 ==========
print("\n===== 字典操作 =====")
# 定义字典
student_dict = {"name": "张三", "age": 20, "score": 88}
print("原始字典：", student_dict)

# 取值（两种方式）
print("姓名：", student_dict["name"])
print("年龄：", student_dict.get("age"))

# 添加/修改键值对
student_dict["gender"] = "男"  # 新增
student_dict["score"] = 90     # 修改
print("修改后字典：", student_dict)

# 取所有键和值
print("所有键：", list(student_dict.keys()))
print("所有值：", list(student_dict.values()))