"""
促销商品详情页面
"""

from common.base import Base, open_app
from page.browser_home_page import BrowserHomePage
import random
import time


class SalesGoodsPage(Base):
    # def __init__(self):
    #     sales = BrowserHomePage()
    #     sales.click_cx_goods()

    # 点击促销商品
    x = random.randint(1, 570)
    y = random.randint(100, 1000)

    def click_goods(self):
        # 先滑动
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.coord_click(x=self.x, y=self.y)

    # 点击立即购买
    bay_loc = ("xpath", "//*[@text='立即购买']")
    def click_bay(self):
        self.click(self.bay_loc)
    # 点击确认
    true_loc = ("xpath", "//*[@text='确定']")
    def click_true(self):
        self.click(self.true_loc)


if __name__ == '__main__':
    driver = open_app()
    B = BrowserHomePage(driver)
    B.click_cx_goods()
    time.sleep(3)
    sales = SalesGoodsPage(driver)
    time.sleep(3)
    sales.click_goods()
    time.sleep(3)
    sales.click_bay()
    sales.click_true()
