# Day4 Python列表&字典学习
## 一、列表（List）
- 定义：有序、可修改的集合，用[]表示 → list1 = [1, 2, "张三", True]
- 常用操作：
  1. 取值：list1[0]（取第一个元素）
  2. 添加：list1.append(3)（末尾加元素）
  3. 删除：del list1[1]（删除指定位置元素）
  4. 长度：len(list1)（获取列表长度）

## 二、字典（Dict）
- 定义：键值对、无序、可修改，用{}表示 → dict1 = {"name":"张三", "age":20}
- 常用操作：
  1. 取值：dict1["name"] 或 dict1.get("age")
  2. 添加/修改：dict1["gender"] = "男"
  3. 删除：del dict1["age"]
  4. 取所有键：dict1.keys()，取所有值：dict1.values()