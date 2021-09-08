from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\willian.lima\Documents\Amazon Web Automation/chromedriver.exe")

driver.get("https://www.google.com.br/")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("www.amazon.com.br", Keys.ENTER)

driver.find_element_by_css_selector("#tads>div>div>div>div.d5oMvf>a>div.cfxYMc.JfZTW.c4Djg.MUxGbd.v0nnCb>span").click()

driver.find_element_by_css_selector("#nav-link-accountList").click()
sleep(3)

driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys("zup_teste@outlook.com")
sleep(3)
driver.find_element_by_xpath('//*[@id="continue"]').click()

driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys("Zup@1234")
sleep(3)
driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()

sleep(3)
driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys("sansumg s20", Keys.ENTER)

sleep(3)
driver.find_element_by_xpath(
    '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/span/a/div/img').click()

sleep(3)
driver.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()

sleep(3)
driver.find_element_by_xpath('//*[@id="attachSiNoCoverage"]').click()

sleep(3)
driver.find_element_by_xpath('//*[@id="nav-cart"]').click()

sleep(3)
driver.find_element_by_xpath('//*[@id="sc-buy-box-ptc-button"]').click()

sleep(3)
driver.find_element_by_xpath('//*[@id="spc-orders"]/div/div/div[3]/div/div/div[2]/div[1]/div/div[2]/div[3]/div/a').click()

sleep(3)
driver.find_element_by_xpath('//*[@id="spc-orders"]/div/div/div[3]/div/div/div[2]/div[1]/div/div[2]/div[3]/div/span[2]/a[2]').click()

driver.close()
