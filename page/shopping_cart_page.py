"""
购物车页面
"""

from common.base import Base
import time

class ShoppingCartPage(Base):
    # 立即购买
    now_bay_loc = ("xpath", "//*[@text='立即购买']")
    def click_now_bay(self):
        # 点击立即购买
        self.click(self.now_bay_loc)

    # 全选
    all_chose_loc = ("id","com.tpshop.malls:id/check_all_btn")
    def click_all_chose(self):
        # 点击全选
        self.click(self.all_chose_loc)

    















