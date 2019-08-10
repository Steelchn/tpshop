"""
封装浏览商品的表现层操作层
主页页面
"""
from common.base import Base, open_app
from time import sleep


class BrowserHomePage(Base):
    # 制作定位器
    cux_loc = ('xpath', '//*[@text="商品促销"]')#促销活动
    def click_cx_goods(self):
        # 点击促销商品
        self.click(self.cux_loc)

    # 定位
    search_loc = ("xpath", "//*[@text='请输入搜索关键词']")
    def click_search(self):
        # 点击主页搜索
        self.click(self.search_loc)
    # 积分商城
    interg_loc = ("xpath","//*[@text='积分商城']")
    def click_interg(self):
        # 点击积分商城
        self.click(self.interg_loc)

    # 团购
    tuan_loc = ("xpath","//*[@text='团购']")
    def click_tuan(self):
        # 点击团购
        self.click(self.tuan_loc)

    # 用户中心
    userinfo_loc = ("xpath","//*[@text='用户中心']")
    def  click_userinfo(self):
        # 点击用户中心
        self.click(self.userinfo_loc)

    # 分类
    classify_loc = ("xpath","//*[@text='分类']")
    def click_classify(self):
        # 点击分类
        self.click(self.classify_loc)
    # 品牌街
    brand_loc = ("xpath","//*[@text='品牌街']")
    def click_brand(self):
        # 点击品牌街
        self.click(self.brand_loc)
    # 我要拼团
    my_play_loc = ("xpath","//*[@text='我要拼团']")
    def click_myplay(self):
        # 点击分类
        self.click(self.my_play_loc)
    # 领券中心
    ticket_loc = ("xpath","//*[@text='领劵中心']")
    def click_ticket(self):
        # 点击分类
        self.click(self.ticket_loc)

    # 点击一般商品
    commonly_loc = ("xpath","//*[@text='航测试手机']")
    def click_commonly_goods(self):
        # 先滑动一下
        self.swipe_up()
        self.click(self.commonly_loc)


if __name__ == '__main__':
    driver = open_app()
    b = BrowserHomePage(driver)
    sleep(3)
    b.click_commonly_goods()
    sleep(4)
