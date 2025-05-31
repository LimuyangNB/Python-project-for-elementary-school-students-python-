print("欢迎使用注册登录系统")

# 加载文件内容到内存
try:
    with open("zhanghao.txt", "r", encoding="utf-8") as f:
        zhaohao = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    zhaohao = []

try:
    with open("mima.txt", "r", encoding="utf-8") as f:
        mima = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    mima = []

sz = 0

# 账号密码存放
zhaohao = []
mima = []


def 注册():
    print('开始注册！！！')
    print('请输入用户名和密码')
    a = input("请输入用户名：")
    zhaohao.append(a)
    with open("zhanghao.txt", "w", encoding="utf-8") as f:
        f.writelines(zhaohao)
    b = input("请输入密码：")
    mima.append(b)                 
    with open("mima.txt", "a", encoding="utf-8") as f:
        f.writelines(mima)
        print("注册成功")
        print('请登陆')
            
            
def 获取密码():
    global sz
    a = input("请输入密码：")
    for i in mima:
        if a in i:
            print("密码正确")
            sz = 1
            break
            
    else:
        print("密码错误")
        获取密码()
def 获取用户名():
    b = input("请输入用户名：")
    for i in zhaohao:
        if b in i:
            print("用户名正确")
            break
        print("用户名正确")
        获取密码()
    else:
        print("用户不存在，输入空格注册")
        if b == " ":
            注册()
            
        获取用户名()
def 使用内容():
    global sz
    global a
    print("你已经登录成功")
    print('输入0退出账号，输入1使用计算器，输入q退出该程序')
    a = input()
    if a not in ['0', '1', 'q']:
        print("输入错误，请重新输入")
        使用内容()
    if a == '0':
        print("已退出账号")
        sz = 0
        开头语()
    elif a == 'q':
        print("已退出程序")
        exit()

    elif a == '1':
        print("欢迎使用计算器")
        print("输入两个数字")
        a = float(input("请输入第一个数字："))
        b = float(input("请输入第二个数字："))
        print("输入你要进行的操作")
        print("1.加法 2.减法 3.乘法 4.除法")
            
        c = input()
        if c == '1':
            print(a + b)
        elif c == '2':
                print(a - b)
        elif c == '3':
                print(a * b)
        elif c == '4':
                print(a / b)
    
def 开头语():
    global sz
    global a
    if sz == 0:
        print("欢迎使用本系统,请输入注册还是登录")
        print("1.注册 2.登录")
        a = input()
    else:
        使用内容()
        
    if a == '2':
        print("请输入用户名和密码")
        获取用户名()
        获取密码()
        sz = 1
        使用内容()


while True:
    开头语()

        



