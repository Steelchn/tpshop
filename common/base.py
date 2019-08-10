# 封装定位的方法

import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


def open_app():
    # 手机配置项
    desired_caps = {}
    # 手机系统
    desired_caps['platformName'] = "android"
    # 手机版本
    desired_caps['platformVesion'] = "5.1"
    # 设备名称
    desired_caps['deviceName'] = "127"
    # app启动名
    desired_caps['appActivity'] = ".SPMainActivity"
    # app包名
    desired_caps['appPackage'] = "com.tpshop.malls"
    # 配置键盘
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 不重置应用
    desired_caps["noReset"] = True
    # toast参数配置
    desired_caps["automationName"] = "Uiautomator2"
    # 打开APP
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver
# 登录
def login(driver):
    element_1 = driver.find_element_by_xpath("//*[@text='我的']")
    element_1.click()
    element_1_1 = driver.find_element_by_id("com.tpshop.malls:id/head_img")
    element_1_1.click()
    element_2 = driver.find_element_by_id("com.tpshop.malls:id/mobile_et") # 账号
    element_2.send_keys("18982954299")
    element_3 = driver.find_element_by_id("com.tpshop.malls:id/pwd_et")  # 密码
    element_3.send_keys("123456")
    element_4 = driver.find_element_by_id("com.tpshop.malls:id/login_tv")
    element_4.click() # 点击登录
    time.sleep(2)
    element_5 = driver.find_element_by_xpath("//*[@text='首页']")
    element_5.click()  # 点击返回首页



class Base:
    """
    封装打开手机app
    """

    def __init__(self, driver):
        self.driver = driver
        self.size = self.driver.get_window_size()  # 获取屏幕大小


    def swipe_up(self):
        # 向上滑动
        x1 = self.size['width'] * 0.5
        y1 = self.size['height'] * 0.75
        y2 = self.size['height'] * 0.25
        self.driver.swipe(x1, y1, x1, y2, duration=2000)

    def swipe_down(self):
        # 向下滑动
        x1 = self.size['width'] * 0.5
        y1 = self.size['height'] * 0.25
        y2 = self.size['height'] * 0.75
        self.driver.swipe(x1, y1, x1, y2, duration=2000)

    def swipe_light(self):
        # 向左滑动
        x1 = self.size['width'] * 0.75
        x2 = self.size['width'] * 0.25
        y1 = self.size['height'] * 0.5
        self.driver.swipe(x1, y1, x2, y1, duration=2000)

    def swipe_right(self):
        # 向右滑动
        x1 = self.size['width'] * 0.25
        x2 = self.size['width'] * 0.75
        y1 = self.size['height'] * 0.5
        self.driver.swipe(x1, y1, x2, y1, duration=2000)

    def find_element(self, selector):
        # 定位单个元素
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(selector))
        return element

    def find_elements(self, selector):
        # 定位多个个元素
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(selector))
        return elements

    def click(self, selector):
        # 做点击
        element = self.find_element(selector)
        element.click()

    def send_keys(self, selector, value):
        # 输入文本
        element = self.find_element(selector)
        element.clear()  # 清空
        element.send_keys(value)  # 输入

    def get_text(self,selector):
        # 获取文本
        element = self.find_element(selector)
        text = element.text
        return text

    # 使用坐标定位点击
    def coord_click(self, x, y):
        TouchAction(self.driver).tap(x=x, y=y).perform()

    # 获取toast值
    def get_toast(self,selector):
        toast = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(selector))
        return toast.text

    # 返回
    def back(self):
        self.driver.back()

    def close(self):
        # 关闭手机app
        self.driver.close()



if __name__ == '__main__':
    driver = open_app()
    login(driver)
    base = Base(driver)  # 先实例化
    selector = ('xpath', '//*[@text="商品促销"]')
    time.sleep(3)
    base.click(selector)
    time.sleep(6)
