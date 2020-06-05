from selenium import webdriver


#acesso o site
driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")

#informacoes de acesso
email = "seu-email"
password = "sua-senha"

# checar os campos
email_xpath = '//*[@id="email"]'
password_xpath = '//*[@id="pass"]'
login_button_xpath = '//*[@id="u_0_b"]'

# inserir informacoes nos campos
email_element = driver.find_element_by_xpath(email_xpath)
password_element = driver.find_element_by_xpath(password_xpath)
login_button_element = driver.find_element_by_xpath(login_button_xpath)

# realizar o acesso
email_element.send_keys(email)
password_element.send_keys(password)
login_button_element.click()