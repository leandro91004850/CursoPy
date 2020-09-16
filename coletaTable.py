from selenium import webdriver
from time import sleep


#acesso o site
url = "https://br.advfn.com/common/account/login"
driver = webdriver.Chrome()
driver.get(url)

#informacoes de acesso
email = ""
password = ""

# checar os campos
email_xpath = '//*[@id="login_username"]'
password_xpath = '//*[@id="login_password"]'
login_button_xpath = '//*[@id="login_submit"]'

# inserir informacoes nos campos
email_element = driver.find_element_by_xpath(email_xpath)
password_element = driver.find_element_by_xpath(password_xpath)
login_button_element = driver.find_element_by_xpath(login_button_xpath)

# realizar o acesso
email_element.send_keys(email)
password_element.send_keys(password)
login_button_element.click()



sleep(5)
table = driver.find_element_by_id('monitorApp_monGrid_grid_table')
coletaTR = table.find_elements_by_tag_name('tr')

resultado = coletaTR[3]
coletaTD = resultado.find_elements_by_tag_name('td')
print(coletaTD[0].text)
print(coletaTD[1].text)
print(coletaTD[2].text)
print(coletaTD[3].text)
print(coletaTD[4].text)