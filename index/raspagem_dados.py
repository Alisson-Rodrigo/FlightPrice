from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



#exibir preços
while True:
    navegador = webdriver.Chrome()
    navegador.get("https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDIzLTA4LTE2agwIAxIIL20vMDZnbXJyDQgDEgkvbS8wMmIwX18aKRIKMjAyMy0wOS0xNGoNCAMSCS9tLzAyYjBfX3IMCAMSCC9tLzA2Z21yQAFIAXABggELCP___________wGYAQE")
    preços = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span')
    texto = preços.text
    print(texto)
    sleep(1000)