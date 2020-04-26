# สร้างฟังก์ชันแบบไม่มีการ return value
def hello(name):
    print(f"Hello {name}")


# สร้างฟังก์ชันแบบมีการ return value
def area(width, height):
    total = width * height
    return total


# เรียกใช้ hello()
hello("nee")

# เรียกใช้ area()
print(area(5, 8))


# ฟังก์ชันแบบมีค่าเริ่มต้น
def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"lang: {lang}")


show_info()
print()
show_info('Nee', 12000, 'PHP')
