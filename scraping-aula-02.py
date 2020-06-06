from selenium.webdriver import Firefox


def find_by_text(browser, tag, text):

    elementos = browser.find_elements_by_tag_name(tag)

    for elemento in elementos:
        if elemento.text == text:
            return elemento


browser = Firefox()
browser.get("https://selenium.dunossauro.live/aula_04_a.html")

elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')
print(elemento_ddg.text)