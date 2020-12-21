from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://oto.repair/')

myMenuText = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/nav/ul/li[2]/a')
textTobeAsserted="Danh sách tiệm"
try:
    assert textTobeAsserted in myMenuText.text
    print("{} exists on the main menu".format(textTobeAsserted))
except AssertionError:
    print("{} doesn't exist".format(textTobeAsserted))

driver.close()
    