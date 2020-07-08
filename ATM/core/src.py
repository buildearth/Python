# 存储用户视图层代码

from interface import user_interface
from interface import bank_interface
from interface import shop_interface
from lib import common
# 登录的用户
login_user = None
# 登录的管理员
login_admin = None
#用户视图层功能
#1.注册功能->register
def register():
    while True:
        # 接收用户输入信息
        user_name = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()
        re_password = input('请再次输入密码: ').strip()

        # 判断用户名为空
        if user_name == '':
            print('请输入正确的用户名格式')
            continue

        # 判断两次输入密码是否一致->小逻辑判断
        if password != re_password:
            print('两次输入密码不一致，请重新输入')
            continue

        # 调用用户接口层进行逻辑处理
        flag, msg = user_interface.register_interface(user_name, password)

        # 输出接口层返回的结果
        print(msg)
        if flag:
            # 注册成功
            break

#2.登录功能->login
def login():
    while True:
        # 接收用户输入信息
        user_name = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()

        # 调用逻辑处理层
        flag, msg = user_interface.login_interface(user_name, password)

        print(msg)
        if flag:
            # 登录成功
            global login_user
            login_user = user_name
            break

#3.查询功能->check_balance
@common.login_auth
def check_balance():
    balance = user_interface.check_bal_interface(login_user)
    print('余额为: %s'%balance)

#4.提现功能->withdrow
@common.login_auth
def withdrow():
    # 银行接口
    while True:
        money = input('请输入提现金额: ').strip()
        # 检测输入的正确性,必须是整数数字
        if not money.isdigit():
            print('请输入正确的金额')
            continue

        money = float(money)
        if money <= 0:
            print('请输入正确的金额')
            continue

        flag, msg = bank_interface.withdrow_interface(login_user, money)
        print(msg)
        if flag:
            break

#5.转账功能->tranfer
@common.login_auth
def tranfer():
    # 接收用户输入的金额,和目标用户
    while True:
        money = input('请输入转账金额:').strip()
        dst_user = input('请输入转账目标用户:').strip()

        # 检测money正确性
        if not money.isdigit():
            print('请输入正确的金额')
            continue
        money = float(money)
        if money <= 0:
            print('请输入正确的金额')
            continue

        # 调用银行接口层
        flag, msg = bank_interface.tranfer_interface(login_user, dst_user, money)
        print(msg)
        if flag:
            break

#6.还款功能->repay
@common.login_auth
def repay():
    while True:
        # 接收用户输入的金额
        money = input('请输入还款金额:').strip()
        #用户输入正确性校验
        if not money.isdigit():
                print('请输入正确的金额')
                continue
        money = float(money)
        if money <= 0:
            print('请输入正确的金额')
            continue
        # 调用银行接口
        flag, msg = bank_interface.repay_interface(login_user, money)
        print(msg)
        if flag:
            break

#7.购物功能->shopping
@common.login_auth
def shopping():
    '''
        思路
            1.商品信息存在于文件当中,显示商品信息时需要从文件中读取,调用shop_interface中的接口获取商品信息
            2.用户当前有个购物车,存储当前选择的商品,若支付成功不用加入购物车,若没有支付,加进用户的购物车
                购物车中没有的商品,进行添加,商品数量为1
                购物车中有的商品,商品数量加1

    '''
    shop_dic = shop_interface.get_shop_info()
    # print(shop_dic)
    print('精品商店'.center(20, '='))
    for index, shop in shop_dic.items():
        shop_name, price = shop
        print('   {}.{}:{}$'.format(index,shop_name, price))
    print('24h营业'.center(22, '='))

    shop_car = {}  # {'商品名字':[价格,数量]}
    while True:
        # 接手用户选择的商品
        choice = input('请输入商品的编号(y(支付) or n(不支付)):').strip()

        if choice == 'y':
            # 检测用户当前购物车中有无商品
            if shop_car == {}:
                print('当前没有选择商品,请选择:')
                continue

            # 调用购物接口
            flag, msg = shop_interface.shopping_interface(login_user, shop_car)
            print(msg)
            if flag:
                break
        elif choice == 'n':
            flag, msg = shop_interface.add_shop_interface(login_user, shop_car)
            print(msg)
            if flag:
                break

        if not choice in shop_dic:
            print('请输入正确的商品编号:')
            continue

        # 购物车更新
        shop_name, shop_price = shop_dic[choice]
        if shop_name in shop_car:
            shop_car[shop_name][1] += 1
        else:
            shop_car[shop_name] = [shop_price, 1]
        print('购物车:', shop_car)



#8.查询流水->check_flow
@common.login_auth
def check_flow():
    flow_list = bank_interface.check_flow_interface(login_user)
    for flow in flow_list:
        print(flow)

#9.查看购物车->check_shop_car
@common.login_auth
def check_shop_car():
    pass

#10.管理员功能->admin
@common.login_auth
def admin():
    # 调用管理员接口
    from core import admin
    admin.run()


# 功能字典
func_dic = {
    '0': exit,
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdrow,
    '5': tranfer,
    '6': repay,
    '7': shopping,
    '8': check_flow,
    '9': check_shop_car,
    '10': admin
}

show_info = '''
    ======  ATM + 购物车  ======
        0.退出
        1.注册功能
        2.登录功能
        3.查询功能
        4.提现功能
        5.转账功能
        6.还款功能
        7.购物功能
        8.查询流水
        9.查看购物车
        10.管理员功能
    ======     end       ======
'''

def run():
    while True:
        print(show_info)
        choice = input('请输入功能编号: ').strip()
        # 用户输入校验
        if not choice in func_dic:
            print('请输入正确的功能编号!')
            continue

        # 调用对应功能
        func_dic[choice]()  # 内存地址加()相当于调用函数
