# Day9 字符串常用操作练习
s = "  Hello Python 123  "

# 1. 去除两边空格
s_strip = s.strip()
print("去空格：", s_strip)

# 2. 大小写转换
print("大写：", s_strip.upper())
print("小写：", s_strip.lower())

# 3. 替换
print("替换Python：", s_strip.replace("Python", "World"))

# 4. 分割字符串
words = s_strip.split()
print("分割后：", words)

# 5. 判断是否以某字符开头/结尾
print("以H开头：", s_strip.startswith("H"))
print("以3结尾：", s_strip.endswith("3"))

# 6. 判断是否是数字
test_str = "12345"
print("是否全是数字：", test_str.isdigit())

# 7. 索引与切片
print("第1个字符：", s_strip[0])
print("切片1-5：", s_strip[1:5])