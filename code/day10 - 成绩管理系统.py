# Day10 综合项目：学生成绩管理系统
def show_menu():
    """显示菜单"""
    print("=" * 30)
    print("  学生成绩管理系统 v1.0")
    print("1. 添加学生成绩")
    print("2. 查询所有学生")
    print("3. 计算班级平均分")
    print("4. 保存数据到文件")
    print("0. 退出系统")
    print("=" * 30)


def add_student(students):
    """添加学生"""
    try:
        name = input("请输入学生姓名：")
        score = int(input("请输入学生成绩："))
        students.append({"name": name, "score": score})
        print("✅ 添加成功！")
    except ValueError:
        print("❌ 输入错误，请输入数字！")


def show_students(students):
    """显示所有学生"""
    print("\n📋 学生列表：")
    for idx, stu in enumerate(students, 1):
        print(f"{idx}. {stu['name']}：{stu['score']} 分")


def calc_avg(students):
    """计算平均分"""
    if not students:
        print("❌ 暂无学生数据")
        return
    total = sum(s["score"] for s in students)
    avg = total / len(students)
    print(f"\n📊 班级平均分：{avg:.1f} 分")


def save_to_file(students):
    """保存到文件"""
    with open("students.txt", "w", encoding="utf-8") as f:
        for stu in students:
            f.write(f"{stu['name']},{stu['score']}\n")
    print("✅ 数据已保存到 students.txt")


def main():
    students = []
    while True:
        show_menu()
        choice = input("请输入操作序号：")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            calc_avg(students)
        elif choice == "4":
            save_to_file(students)
        elif choice == "0":
            print("👋 退出系统，再见！")
            break
        else:
            print("❌ 输入错误，请重新输入！")


if __name__ == "__main__":
    main()