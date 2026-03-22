# Day7 Python异常处理学习
## 一、什么是异常？
- 代码运行时出错（比如除以0、打开不存在的文件、输入非数字），程序崩溃
- 常见异常：ZeroDivisionError（除0）、FileNotFoundError（文件不存在）、ValueError（值错误）

## 二、核心语法：try-except
- 格式：
  try:
      可能出错的代码
  except 异常类型:
      出错后执行的代码
  else:
      没出错时执行的代码（可选）
  finally:
      无论是否出错都执行的代码（可选）

## 三、作用
- 避免程序崩溃，给用户友好提示
- 增强代码的容错性（求职高频考点）