"""
购买促销商品
"""
from common.base import open_app
from page.browser_home_page import BrowserHomePage
from page.firm_order_page import FirmOrderPage
from page.sales_goods_page import SalesGoodsPage
import time,pytest,allure


class TestPromotion:
    def setup(self):
        self.driver = open_app()

    def teardown(self):
        self.driver.quit()

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="使用余额购买商品")
    def test_promotion(self):
        allure.attach("点击购买商品", "促销商品")
        b = BrowserHomePage(self.driver) # 实例化主页页面
        b.click_cx_goods()  # 点击促销
        s = SalesGoodsPage(self.driver)  # 实例化促销商品页面
        time.sleep(3)
        allure.attach("点击商品", "立即购买")
        s.click_goods() # 点击商品
        s.click_bay()   # 点击立即购买
        s.click_true()  # 点击确认购买
        # 跳转到确认订单页面
        time.sleep(3)
        f = FirmOrderPage(self.driver) # 先实例化确认订单页面
        time.sleep(3)
        # 获取当前余额
        proice = float(f.get_proice())
        allure.attach("获取购买前的余额", f"{proice}")
        # # 点击使用积分购买
        # f.click_integer()
        # 点击余额购买
        f.click_balance()
        # 获取商品价格
        goodsproice = float(f.get_goods_proice())
        allure.attach("获取需要购买商品的价格", f"{goodsproice}")
        # 点击立即购买
        f.click_order()
        # 输入密码
        f.send_passwd("123456")
        # 点击确定
        allure.attach("点击确认订单", "确认")
        f.click_qtrue()
        time.sleep(3)
        # 返回 获取余额
        f.click_back()
        time.sleep(3)
        f.click_back()
        time.sleep(3)
        f.click_back()
        f.click_my()
        # 获取新的余额
        newproice = float(f.get_new_proice())
        # 获取购物前余额
        allure.attach("获取购买后的余额", f"{newproice}")
        if proice - goodsproice == newproice:
            assert 1
        else:
            assert 0


if __name__ == '__main__':
    pytest.main("-s test_promotion.py")