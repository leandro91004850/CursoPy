from selenium import webdriver


#acesso o site
url = "http://gestao.obti.com.br:8080/mk/login/?sys=MK0"
driver = webdriver.Firefox()
driver.get(url)

#informacoes de acesso
email = "leandro"
password = "senha"

# checar os campos
email_xpath = '/html/body/div/div[2]/form/input[2]'
password_xpath = '/html/body/div/div[2]/form/input[3]'
login_button_xpath = '/html/body/div/div[2]/form/button'

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