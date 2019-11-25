#coding==utf--8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

caps = {}
caps["deviceName"] = "syam-test-iPad3"
caps["platformName"] = "iOS"
caps["platformVersion"] = "11.4.1"
caps["bundleId"] = "com.bindo.bindo-pos-dev"
caps["udid"] = "1d4e848c7ae0f061e1820baf5a60be6560ef3b26"
caps["no-reset"] = True
caps["useNewWDA"] = False

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

TouchAction(driver).tap(x=655, y=48).perform()
TouchAction(driver).tap(x=978, y=722).perform()
TouchAction(driver).tap(x=132, y=151).perform()
TouchAction(driver).tap(x=328, y=143).perform()
TouchAction(driver).tap(x=132, y=146).perform()
TouchAction(driver).tap(x=345, y=144).perform()

TouchAction(driver).tap(x=333, y=472).perform()
TouchAction(driver).tap(x=451, y=472).perform()
TouchAction(driver).tap(x=595, y=477).perform()
TouchAction(driver).tap(x=341, y=554).perform()
TouchAction(driver).tap(x=472, y=552).perform()
TouchAction(driver).tap(x=583, y=556).perform()

TouchAction(driver).tap(x=674, y=144).perform()
time.sleep(2)
driver.quit()
