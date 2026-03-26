# Day11 第一个Python爬虫：爬取网页标题
# 需要先安装库：pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# 1. 目标网址（我们爬一个简单的测试网页）
url = "https://www.baidu.com"

try:
    # 2. 发送请求，获取网页内容
    response = requests.get(url)
    response.encoding = "utf-8"  # 设置编码

    # 3. 解析网页
    soup = BeautifulSoup(response.text, "html.parser")

    # 4. 提取标题
    title = soup.find("title").text
    print("✅ 爬取成功！")
    print("网页标题：", title)

    # 5. 保存到文件
    with open("爬虫结果.txt", "w", encoding="utf-8") as f:
        f.write(f"爬取网址：{url}\n")
        f.write(f"网页标题：{title}\n")
    print("📄 结果已保存到 爬虫结果.txt")

except Exception as e:
    print("❌ 爬取出错：", e)