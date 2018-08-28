# 一级
## 二级

```
# coding:utf-8

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'e2939b32'
desired_caps['appPackage'] = 'com.android.quicksearchbox'
desired_caps['appActivity'] = '.SearchActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element_by_id("android:id/button1").click()
driver.find_element_by_class_name("android.widget.EditText").click()

print "done !"
# driver.quit()
```
