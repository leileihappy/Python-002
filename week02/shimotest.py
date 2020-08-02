from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get(' https://shimo.im')
 
    btn1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]')
    btn1.click()

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('testpythonlei@163.com')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('anlei666')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    cookies = browser.get_cookies()
    print(cookies)

except Exception as e:
    print(e)

finally:

    browser.close()