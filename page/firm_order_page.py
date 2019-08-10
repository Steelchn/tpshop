"""
确认订单页面
"""
from common.base import Base, open_app, login
from page.browser_home_page import BrowserHomePage
from page.sales_goods_page import SalesGoodsPage
from time import sleep


class FirmOrderPage(Base):
    # 点击使用余额
    yue_loc = ("id", "com.tpshop.malls:id/order_balance_sth")

    def click_balance(self):
        self.click(self.yue_loc)

    # 点击使用积分
    jifen_loc = ("id", "com.tpshop.malls:id/order_point_sth")

    def click_integer(self):
        self.click(self.jifen_loc)

    # 点击确认订单
    order_loc = ("id", "com.tpshop.malls:id/submit_tv")

    def click_order(self):
        self.click(self.order_loc)

    proice_loc = ("id", "com.tpshop.malls:id/order_balance_tv")

    def get_proice(self):
        # 获取余额文本
        element = self.find_element(self.proice_loc)
        text = element.text
        return text

    # 返回
    def back_page(self):
        self.back()

    # 点击选择收货地址
    address_loc = ("id", "com.tpshop.malls:id/consignee_address_tv")

    def click_address(self):
        self.click(self.address_loc)

    # 输入密码输入框
    password_loc = ("id", "com.tpshop.malls:id/pwd_et")

    def send_passwd(self, value):
        self.send_keys(self.password_loc, value)

    # 确认
    qtrue_loc = ("id", "com.tpshop.malls:id/sure_tv")

    def click_qtrue(self):
        self.click(self.qtrue_loc)

    def click_back(self):
        # 点击返回
        self.back_page()

    my_loc = ("xpath", "//*[@text='我的']")

    def click_my(self):
        # 点击我的
        self.click(self.my_loc)

    # 获取我的余e
    my_yue_loc = ("id", "com.tpshop.malls:id/balance_tv")

    def get_new_proice(self):
        # 获取购买后的余额
        element = self.find_element(self.my_yue_loc)
        text = element.text
        return text

    # 获取商品的金额
    goods_proice_loc = ("id", "com.tpshop.malls:id/balance_fee_tv")

    def get_goods_proice(self):
        element = self.find_element(self.goods_proice_loc)
        text = element.text
        return text.strip("¥")


if __name__ == '__main__':
    driver = open_app()
    # login(driver)
    B = BrowserHomePage(driver)
    B.click_commonly_goods()  # 点击一般商品
    sleep(3)
    sales = SalesGoodsPage(driver)
    sales.click_bay()  # 点击立即购买
    sales.click_true()  # 点击确认
    F = FirmOrderPage(driver)  # 进入订单页面
    # 获取余额
    price = F.get_proice()
    print(price)
    test = F.get_goods_proice()
    print(test)
    # F.click_balance()
    # F.click_integer()
    # F.click_order()
    # value = "123456"
    # F.send_passwd(value)
    # F.click_qtrue()
