from interface import admin_interface

# 管理员功能
# 1.添加用户
def add_user():
    # 调用src的register
    from core import src
    src.register()

# 2.用户额度修改
def change_balance():
    while True:
        # 输入额度和用户
        user_name = input('请输入用户名:').strip()
        money = input('请输入额度:').strip()

        # 输入金额正确性判断
        if not money.isdigit():
            print('请输入正确的金额:')
            continue

        money = float(money)
        # 调用管理员接口
        flag, msg = admin_interface.change_bal_interface(user_name, money)
        print(msg)
        if flag:
            break
# 3.冻结账户
def lock_user():
    while True:
        user_name = input('请输入用户名:').strip()

        flag, msg = admin_interface.lock_user_interface(user_name)
        print(msg)
        if flag:
            break


# 4.添加管理员用户
# def add_admin():

admin_fuc = {
    '1': add_user,
    '2': change_balance,
    '3': lock_user
}

def run():
    while True:
        print('''
            ======  admin  ======
                1.添加用户
                2.用户额度修改
                3.冻结账户
            ======   end   ======
            ''')
        choice = input('请输入管理员功能编号')

        # 检测用户输入正确性
        if not choice in admin_fuc:
            print('请输入正确的功能编号')
            continue

        admin_fuc[choice]()
