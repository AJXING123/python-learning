# Day6 文件操作练习
import os  # 导入os模块，用于确认文件路径

# ========== 1. 写文件（w模式，覆盖） ==========
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Python文件操作练习\n")  # 写单行
    f.writelines(["第一行内容\n", "第二行内容\n", "第三行内容\n"])  # 写多行
print("✅ 已生成test.txt文件（覆盖模式）")

# ========== 2. 追加文件（a模式） ==========
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("\n这是追加的内容～")
print("✅ 已往test.txt追加内容")

# ========== 3. 读文件（r模式） ==========
with open("test.txt", "r", encoding="utf-8") as f:
    all_content = f.read()  # 读取全部内容
    print("\n📄 test.txt文件全部内容：")
    print(all_content)

# ========== 4. 验证文件位置（可选） ==========
print(f"\n📌 文件路径：{os.path.abspath('test.txt')}")