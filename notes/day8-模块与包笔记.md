# Day8 Python模块与包学习
## 一、什么是模块？
- 一个.py文件就是一个模块（比如math.py），包含函数/变量/类
- 作用：代码复用，不用重复写相同功能

## 二、导入模块的方式
1. import 模块名 → 比如 import math（使用：math.sqrt(4)）
2. from 模块名 import 函数/变量 → 比如 from math import sqrt（使用：sqrt(4)）
3. from 模块名 import * → 导入模块所有内容（不推荐，易冲突）
4. import 模块名 as 别名 → 比如 import math as m（使用：m.sqrt(4)）

## 三、什么是包？
- 包含__init__.py文件的文件夹就是包（用于组织多个模块）
- 新手先掌握模块即可，包是进阶用法