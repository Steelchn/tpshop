

from common.base import open_app, login
from page.browser_home_page import BrowserHomePage
from page.firm_order_page import FirmOrderPage
from page.sales_goods_page import SalesGoodsPage
import time, pytest, allure


class TestNotPromotion:
    def setup(self):
        # 打开app
        self.driver = open_app()

    def teardown(self):
        # 关闭app
        self.driver.quit()

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="使用余额购买商品")
    def test_not_promotion(self):
        time.sleep(2)
        b = BrowserHomePage(self.driver)  # 实例化主页页面
        allure.attach("点击购买商品", "一般商品")
        b.click_commonly_goods()  # 点击一般的商品
        s = SalesGoodsPage(self.driver)  # 实例化商品页面
        time.sleep(3)
        allure.attach("点击购买", "确认购买")
        s.click_bay()  # 点击立即购买
        s.click_true()  # 点击确认购买
        # 跳转到确认订单页面
        time.sleep(3)
        f = FirmOrderPage(self.driver)  # 先实例化确认订单页面
        time.sleep(3)
        proice = float(f.get_proice())
        # 获取购物前余额
        allure.attach("获取购买前的余额", f"{proice}")
        # # 点击使用积分购买
        # f.click_integer()
        # 点击余额购买
        f.click_balance()
        # 获取购物商品的金额
        goodsproice = float(f.get_goods_proice())
        # 获取购物前余额
        allure.attach("获取商品的价格", f"{goodsproice}")
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
    pytest.main("-s test_not_promotion.py")
