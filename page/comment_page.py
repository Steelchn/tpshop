"""
评价页面
"""
import time

from common.base import Base, open_app, login


# 进入待评价
def to_be_com(driver):
    driver.find_element_by_xpath("//*[@text='我的']").click()  # 进入我的
    driver.find_element_by_xpath("//*[@text='待评价']").click()  # 进入评价


class CommentPage(Base):
    # 评价晒
    comment_sai_loc = ("xpath", "//*[@text='评价晒单']")

    def click_comment_sai(self):
        # 点击评价晒
        elements = self.find_elements(self.comment_sai_loc)
        elements[0].click()

    # 点击已评价
    evaluate_x = 500
    evaluate_y = 100

    def click_evaluate(self):
        self.coord_click(x=self.evaluate_x, y=self.evaluate_y)

    # 获取商品数量
    goods_num_loc = ("xpath", "//*[contains(@text,'已评价')]")

    def get_comment_num(self):
        element = self.find_element(self.goods_num_loc)
        text = element.text
        return text

    # 输入评价com.tpshop.malls:id/comment_content_et
    comment_content_loc = ("id", "com.tpshop.malls:id/comment_content_et")

    def send_comment(self, text):
        # 输入评价
        self.send_keys(self.comment_content_loc, text)

    toast_loc = ("xpath","//*[contains(@text,'评论成功')]")
    def get_page_toast(self):
        toast_text = self.get_toast(self.toast_loc)
        return toast_text


    # 评价等级星星
    star1_loc = ("id", "com.tpshop.malls:id/star1_btn")
    star2_loc = ("id", "com.tpshop.malls:id/star2_btn")
    star3_loc = ("id", "com.tpshop.malls:id/star3_btn")
    star4_loc = ("id", "com.tpshop.malls:id/star4_btn")
    star5_loc = ("id", "com.tpshop.malls:id/star5_btn")

    def click_star_1(self):
        # 获取星星的元素
        elements = self.find_elements(self.star1_loc)
        # 遍历每一个做点击
        for element in elements:
            element.click()

    def click_star_2(self):
        elements_2 = self.find_elements(self.star2_loc)
        # 遍历每一个做点击
        for element in elements_2:
            element.click()

    def click_star_3(self):
        elements_3 = self.find_elements(self.star3_loc)
        # 遍历每一个做点击
        for element in elements_3:
            element.click()

    def click_star_4(self):
        elements_4 = self.find_elements(self.star4_loc)
        # 遍历每一个做点击
        for element in elements_4:
            element.click()

    def click_star_5(self):
        elements_5 = self.find_elements(self.star5_loc)
        # 遍历每一个做点击
        for element in elements_5:
            element.click()

    # 提交
    refer_loc = ("xpath", "//*[@text='提交']")

    def click_refer(self):
        # 点击提交
        self.click(self.refer_loc)


if __name__ == '__main__':
    driver = open_app()
    # login(driver)
    to_be_com(driver)
    c = CommentPage(driver)
    time.sleep(2)
    c.click_evaluate()  # 点击已评价
    num = c.get_comment_num()
    print(num)
