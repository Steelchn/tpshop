"""
评价
"""
import time
import pytest,allure
from common.base import open_app, login
from page.comment_page import CommentPage,to_be_com



class TestComment:
    def setup(self):
        # 打开APP
        self.driver = open_app()

    def teardown(self):
        # 关闭app
        self.driver.quit()

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="评价商品")
    def test_comment(self):

        allure.attach("进入app", "进入我的")
        to_be_com(self.driver)  # 进入待评价页面
        c = CommentPage(self.driver)  # 实例化待评价商品页面
        time.sleep(2)

        allure.attach("点击待评价", "点击评价晒单")

        c.click_comment_sai()  # 点击评价晒单
        time.sleep(2)
        allure.attach("进入评价页面", "排输入评价内容")
        text = "还不错,用的挺好"   # 输入评价内容
        c.send_comment(text)
        time.sleep(3)
        allure.attach("评价商品", "点击星级")
        c.click_star_5()  # 点击星级
        c.click_refer()  # 点击提交
        # 获取toast值
        text = c.get_page_toast()
        allure.attach("点击提交", f"得到{text}")
        if text == "评论成功":
            assert 1
        else:
            assert 0



if __name__ == '__main__':
    pytest.main("-s test_comment.py")