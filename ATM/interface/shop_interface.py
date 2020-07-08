from db import db_handle

# 购物接口
def get_shop_info():
    return db_handle.read_shop_info()

def add_shop_interface(user_name, shopping_car):
    user_dic = db_handle.select(user_name)
    shop_car = user_dic.get('shop_car')
    # 更新用户信息中的购物车
    # 判断当前用户选择的商品,是否已经存在
    for shop_name, price_num in shopping_car.items():
        # 商品存在,数量增加
        if shop_name in shop_car:
            shop_car[shop_name][1] += price_num[1]
        else:
            shop_car.update({shop_name:price_num})
    # 更新数据
    user_dic['shop_car'] = shop_car
    db_handle.save(user_dic)

    return True, '购物车添加成功'


def shopping_interface(user_name, shop_car):
    # 计算购物金额
    count = 0
    for shop, price_num in shop_car.items():
        price, num = price_num
        count += price * num

    from interface import bank_interface
    res = bank_interface.pay_interface(user_name, count)
    if res:
        return True, '支付成功'
    else:
        # 加进购物车
        add_shop_interface(user_name, shop_car)
        return False, '余额不足'
