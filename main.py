# coding=utf-8
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
print("on start")
# 打开网址登陆

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://healthreport.zju.edu.cn/ncov/wap/default/index")
driver.find_element_by_id("username").send_keys("您的学号")
driver.find_element_by_id("password").send_keys("您的密码")
driver.find_element_by_id("dl").click()


# print("打不开网站！")

# 是否有意向接种
driver.find_element_by_xpath(
    "//div[@name='sfyxjzxgym']/div[1]/div[1]").click()  # 是

# 是否不宜接种
driver.find_element_by_xpath(
    "//div[@name='sfbyjzrq']/div[1]/div[5]").click()  # 否

# 接种情况
driver.find_element_by_xpath(
    "//div[@name='jzxgymqk']/div[1]/div[2]").click()  # 已完成接种
# time.sleep(3)

# 今日是否因为发热
driver.find_element_by_xpath(
    "//div[@name='sffrqjwdg']/div[1]/div[2]").click()  # 否
# 今日是否因为其他原因
driver.find_element_by_xpath(
    "//div[@name='sfqtyyqjwdg']/div[1]/div[2]").click()  # 否

# 填写信息
# 今日是否在校
driver.find_element_by_xpath(
    "//div[@name='sfzx']/div[1]/div[1]").click()  # 是
# driver.find_element_by_xpath("//div[@name='sfzx']/div[1]/div[2]").click()  # 否
# 点击获得地理信息
driver.find_element_by_xpath("//div[@name='area']/input[1]").click()
# # 是否从以下地区返回
# driver.find_element_by_xpath("//div[@name='area']/input[1]").click()

# 是否已申领健康码
driver.find_element_by_xpath("//div[@name='sfsqhzjkk']/div[1]/div[1]").click()

# 健康码颜色
driver.find_element_by_xpath("//div[@name='sqhzjkkys']/div[1]/div[1]").click()

# driver.find_element_by_xpath(
#     "//div[@name='jrdqtlqk']/div[1]/div[3]").click()  # 否


# 本人家庭成员是否有近14日入境的情况
element = driver.find_element_by_xpath(
    "//div[@name='sfymqjczrj']/div[1]/div[2]")  # 否
webdriver.ActionChains(driver).move_to_element(
    element).click(element).perform()
# 本人承诺
driver.find_element_by_xpath("//div[@name='sfqrxxss']").click()
# 提交信息
driver.find_element_by_xpath("//div[@class='footers']").click()
# 确定提交
try:
    driver.find_element_by_xpath(
        "//div[@class='wapcf-btn wapcf-btn-ok']").click()
except:
    print("已经提交过啦")
# 退出
driver.close()
print("work done")
