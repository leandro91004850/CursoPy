from selenium import webdriver


#acesso o site
url = "https://www.facebook.com/"
driver = webdriver.Firefox()
driver.get(url)

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


#variavel da url
usuario = driver.find_element_by_class_name('_1vp5')

#obtendo o nome do usuario logado
print(f'o usuario logado é o {usuario.text}')