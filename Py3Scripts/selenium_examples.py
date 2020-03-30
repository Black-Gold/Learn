from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions, expected_conditions, wait
from selenium.common.exceptions import (
    ElementNotSelectableException,
    ElementNotVisibleException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options


# selenium示例
# 选择器优先使用依次为id、css selector、xpath灵活但性能低复杂度高不好调试，基于link的只适合href链接且会在WebDriver中调用xpath选择器
# tag name可能会出现页面存在同一标记多个元素，调用返回元素集合的findElements by方法时很有用
#
"""
| 定位器/选择器 | 描述 |
| :------: | :------: |
| class name        | 查找类名称包含搜索值的元素（不允许复合类名称） |
| css selector      | 查找与 CSS 选择器匹配的元素 |
| id                | 查找其 ID 属性与搜索值匹配的元素 |
| name              | 查找 NAME 属性与搜索值匹配的元素 |
| link text         | 查找可见文本与搜索值匹配的锚点元素 |
| partial link text | 查找其可见文本包含搜索值的锚点元素。如果匹配多个元素，则只选择第一个元素 |
| tag name          | 查找其标记名称与搜索值匹配的元素 |
| xpath             | 查找与 XPath 表达式匹配的元素 |
"""

try:
    # service = Service('E:/chromedriver.exe')
    # service.start()
    # browser = webdriver.Remote(service.service_url)
    browser = webdriver.Chrome()
    browser.get("https://www.xxx.com/login.html")
    element = browser.find_element_by_name("p")
    # 使用sendKeys方法设置元素文本
    element.send_keys("vim" + Keys.RETURN)
    # 获取当前url
    browser.current_url
    # 浏览器的刷新、前进和后退按钮
    browser.refresh()
    browser.forward()
    browser.back()
finally:
    browser.quit()

# 处理js拖动一个元素到另一个元素，例如拖放功能
source = browser.find_element_by_id("source")
target = browser.find_element_by_id("target")
ActionChains(browser).drag_and_drop(source, target).perform()

# click方法单击一个元素
browser.find_element_by_css_selector("input[type='sumbit']").click()

# WebDriver无法区分浏览器窗口和标签页，但可以使用窗口句柄的唯一标识符来操作
# 获取当前窗口句柄
browser.current_window_handle

# selenium4之前需要遍历WebDriver，切换窗口，selenium4新的api接口NewWindow可以创建新的窗口并自动切换
# 上下文管理器启动驱动程序
with webdriver.Firefox() as browser:
    browser.get("https://www.xxx.com")
    # 设置等待时间
    wait_time = WebDriverWait(browser, 10)
    # 存储原始窗口id
    origin_window = browser.current_window_handle
    # 检查其他未打开的窗口
    assert len(browser.window_handles) == 1
    browser.find_element_by_link_text("new window").click()
    # 等待新窗口或标签页
    wait.until(EC.number_of_windows_to_be(2))
    # 循环找到新的窗口句柄
    for window_handle in browser.window_handles:
        if window_handle != origin_window:
            browser.switch_to.window(window_handle)
            break
    # 等待加载完成                                                                                        发
    wait.until(EC.title_is("xxx"))

# 创建新的标签页和窗口,此特性只适用于selenium4
browser.switch_to.new_window("tab")
browser.switch_to.new_window("window")

# 通过id切换frame或iframe
browser.switch_to.frame("buttonframe")
browser.find_element_by_tag_name("button").click()

# 若页面js中包括_window.frames，则可以使用frame的index查询
# 切换到第二个框架
browser.switch_to.frame(1)

# 切换到默认内容
browser.switch_to.default_content()

# 获取窗口大小
size = browser.get_window_size()  # 返回字典类型
width = browser.get_window_size().get("width")
height = browser.get_window_size().get("height")
browser.set_window_size(900, 900)

# 获取窗口左上角坐标
xy = browser.get_window_position()  # 返回字典类型
browser.set_window_position(0, 0)  # 移动窗口到左上角
browser.maximize_window()  # 最大化窗口

# 同一个等待条件不要混合使用显式等待和隐式等待
# 超时3秒但直到some_condition满足后(显式等待)
# WebDriverWait(browser, timeout=3).until(some_condition)


# 隐式等待是告诉WebDriver如果在查找一个或多个不是立即可用的元素时轮询DOM一段时间。默认设置为0，表示禁用
# 一旦设置好，隐式等待就被设置为会话的生命周期
browser.implicitly_wait(10)  # 等待10秒

# 流畅等待定义等待条件的最大时间量及检查条件的频率
# 例如设置等待来忽略NoSuchElementException异常
browser.get("xxx.com")
wait = WebDriverWait(
    browser,
    10,
    poll_frequency=1,
    ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException],
)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))


# js的alerts警告框
browser.find_element_by_link_text("xxx").click()
# 等待alert窗口显示后存储到变量中
alert = wait.until(expected_conditions.alert_is_present())
# 将警告中的文本存储到变量
alert_text = alert.text
# 模拟点击确定按钮
alert.accept()

# js的confirm确认框
browser.find_element_by_link_text("xxx").click()
wait.until(expected_conditions.alert_is_present())
alert = browser.switch_to.alert
alert_text = alert.text
alert.dismiss()

# js的prompt提示框
alert = Alert(browser)
alert.send_keys("xxx")
alert.accept()

# http代理设置
Proxy = "host:port"
webdriver.DesiredCapabilities.CHROME["proxy"] = {
    "httpProxy": Proxy,
    "ftpProxy": Proxy,
    "sslProxy": Proxy,
    "proxyType": "MANUAL",
}

with webdriver.Chrome() as driver:
    driver.get("xxx.com")


# 页面加载策略
"""
document.readyState 属性描述当前页面的加载状态. 默认情况下, 在页面就绪状态是 complete 之前,
WebDriver都将延迟 driver.get() 的响应或 driver.navigate().to() 的调用
"""

# normal默认加载策略
# WebDriver等待整个页面的加载，设置为normal时，WebDriver保持等待直到返回load事件
options = Options()
options.page_load_strategy = "normal"
browser = webdriver.Chrome(options=options)
browser.get("xxx.com")
browser.quit()

# eager加载策略
# WebDriver保持等待并直到完全加载并解析了html文件，忽略css样式表、图片和subframes的加载
# 设置为eager时，保持等待直到返回DOMContentLoaded事件
options.page_load_strategy = "eager"

# none加载策略
# WebDriver仅等待至初始页面下载完成

# find element用于查找网页元素
# 从网页元素q中查找searchbox元素
search_box = browser.find_element_by_name("q")
search_box.send_keys("searchconent")

# find elements返回的是匹配到的网页元素列表，需要遍历元素列表操作
elements_list = browser.find_element_by_tag_name("p")
for ele in elements_list:
    print(ele.text)

# 从父元素的上下文查找子元素
search_src = browser.find_element_by_tag_name("form")
search_box = search_src.find_element_by_name("q")
search_box.send_keys("searchconent")

# 从父元素的上下文查找匹配子webelement的列表
element = browser.find_element_by_tag_name("div")
sub_elements = element.find_element_by_tag_name("p")
for ele in sub_elements:
    print(ele.text)

# get active element
# 用于查找当前页面上下文具有焦点的DOM元素
browser.find_element_by_css_selector('[name="q"]').send_keys("webElement")
# 获取当前动态元素的属性
attr = browser.switch_to.active_element.get_attribute("title")
print(attr)

# 模拟按下或释放辅助按键的动作，keyDown、keyUp
webdriver.ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").perform()
webdriver.ActionChains(browser).key_up(Keys.CONTROL).send_keys("a").perform()

# clear清除可编辑的元素的内容，但仅适用于可编辑且可交互的元素，例如google的搜索输入元素
search_input = browser.find_element_by_name("q")
search_input.send_keys("searchcontent")
search_input.clear()

# 为firefox创建自定义配置
"""
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
options=Options()
firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", False)
options.profile = firefox_profile
"""

# 鼠标动作模拟
browser = webdriver.Chrome()
browser.get("http://www.google.com")

# 存储google search按钮元素
searchBtn = browser.find_element_by_link_text("Sign in")
# 点击元素不释放
webdriver.ActionChains(browser).click_and_hold(searchBtn).perform()
# 在元素上下文单击(鼠标右键)
webdriver.ActionChains(browser).context_click(searchBtn).perform()
# 给定元素双击
webdriver.ActionChains(browser).double_click(searchBtn).perform()

# 移动到元素
gmailLink = driver.find_element_by_link_text("Gmail")
webdriver.ActionChains(browser).move_to_element(gmailLink).perform()

# 设置元素x,y坐标
xOffset = 100
yOffset = 100
# 将鼠标移动到指定坐标位置，可移到窗口之外
webdriver.ActionChains(browser).move_by_offset(xOffset, yOffset).perform()

# 在一个元素点击并按住，然后移到另一个元素
sourceEle = driver.find_element_by_id("draggable")
targetEle = driver.find_element_by_id("droppable")
# 鼠标从sourceEle移动到targetEle元素
webdriver.ActionChains(browser).drag_and_drop(sourceEle, targetEle).perform()

# 在一个元素点击并按住，然后移动一定的偏移量
targetEleXOffset = targetEle.location.get("x")
targetEleYOffset = targetEle.location.get("y")
webdriver.ActionChains(browser).drag_and_drop_by_offset(
    sourceEle, targetEleXOffset, targetEleYOffset
).perform()

# 释放按下的鼠标左键，如果webelement移动了，将自动释放在给定webelement上按下的鼠标左键
webdriver.ActionChains(browser).release().perform()

# 添加cookies
# 常用于将cookie添加到当前访问的上下文中. 添加Cookie仅接受一组已定义的可序列化JSON对象
browser.get("xx.com")
browser.add_cookie({"name": "key", "value": "value"})

# 获取cookie
browser.get_cookie()
# 获取所有cookies
browser.get_cookies

# 删除cookie
browser.delete_cookie()
# 删除所有cookies
browser.delete_all_cookies()

# Lax,将Cookie sameSite属性设置为Lax时，该Cookie将与第三方网站发起的GET请求一起发送
# 目前此功能已嵌入chrome80+,适用于selenium4+
driver.add_cookie({"name": "foo", "value": "value", "sameSite": "Strict"})
driver.add_cookie({"name": "foo1", "value": "value", "sameSite": "Lax"})
cookie1 = driver.get_cookie("foo")
cookie2 = driver.get_cookie("foo1")
print(cookie1)
print(cookie2)
