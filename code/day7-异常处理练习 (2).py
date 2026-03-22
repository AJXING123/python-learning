# Day7 异常处理练习
# ========== 1. 处理除0异常 ==========
print("===== 处理除0异常 =====")
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except ZeroDivisionError:
    print("❌ 错误：不能除以0！")
else:
    print(f"✅ 计算结果：{result}")
finally:
    print("👉 除0判断完成\n")

# ========== 2. 处理文件不存在异常 ==========
print("===== 处理文件不存在异常 =====")
try:
    with open("不存在的文件.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("❌ 错误：文件不存在！")
finally:
    print("👉 文件读取判断完成\n")

# ========== 3. 处理输入值错误（实战场景） ==========
print("===== 处理输入值错误 =====")
while True:
    try:
        age = int(input("请输入你的年龄："))
        if age < 0 or age > 120:
            print("❌ 年龄必须在0-120之间！")
        else:
            print(f"✅ 你的年龄是：{age}岁")
            break  # 输入正确则退出循环
    except ValueError:
        print("❌ 错误：请输入数字！")