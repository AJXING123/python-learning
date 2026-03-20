# Day5 函数练习
# ========== 1. 定义无参数无返回值函数 ==========
def say_hello():
    """打印问候语（无参数、无返回值）"""
    print("你好！欢迎学习Python函数～")

# 调用函数
say_hello()

# ========== 2. 定义有参数有返回值函数 ==========
def calculate_sum(num1, num2=0):
    """计算两个数的和（有位置参数+默认参数，有返回值）"""
    total = num1 + num2
    return total

# 调用方式1：位置参数
result1 = calculate_sum(5, 3)
print(f"5+3={result1}")

# 调用方式2：关键字参数
result2 = calculate_sum(num1=10, num2=20)
print(f"10+20={result2}")

# 调用方式3：只传一个参数（用默认参数）
result3 = calculate_sum(8)
print(f"8+0={result3}")

# ========== 3. 函数嵌套调用 ==========
def print_result():
    """调用计算函数，并打印结果"""
    res = calculate_sum(100, 200)
    print(f"100+200的结果是：{res}")

print_result()