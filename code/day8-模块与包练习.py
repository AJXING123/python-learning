# Day8 模块与包练习
# ========== 1. 导入内置模块（math） ==========
print("===== 导入math模块 =====")
# 方式1：import 模块名
import math
print("√16 =", math.sqrt(16))  # 计算平方根
print("π =", math.pi)          # 调用模块中的变量

# 方式2：from 模块导入函数
from math import pow
print("2^3 =", pow(2, 3))      # 计算2的3次方

# 方式3：导入模块并取别名
import math as m
print("sin(90°) =", m.sin(m.pi/2))  # 计算正弦值（弧度制）

# ========== 2. 自定义模块（实战演示） ==========
print("\n===== 自定义模块 =====")
# 第一步：先在桌面新建一个my_module.py文件，内容如下：
# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b

# 第二步：导入自定义模块
import sys
# 添加桌面路径（让Python能找到自定义模块）
sys.path.append("C:/Users/你的用户名/Desktop")  # 替换成你的桌面路径！

try:
    import my_module
    print("5+3 =", my_module.add(5, 3))
    print("5-3 =", my_module.sub(5, 3))
except ImportError:
    print("❌ 请先在桌面创建my_module.py文件！")