from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

for c in range(1):
    try:
        navegador = webdriver.Chrome()
        actions = ActionChains(navegador)
        navegador.get("https://www.google.com/travel/flights?sca_esv=555979541&output=search&q=passagens+aereas&source=lnms&mode_promoted=true&impression_in_search=true&sa=X&sqi=2&ved=2ahUKEwjtxKnJm9WAAxXfLrkGHXdLBN4Q0pQJegQICRAB")
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu-shader-disk-cache')
        origem = navegador.find_element('xpath','//*[@id="i21"]/div[1]/div/div/div[1]/div/div/input')
        actions.click(origem)
        actions.send_keys_to_element(origem, "\b")
        actions.send_keys('São Paulo')
        actions.send_keys(Keys.ENTER)
        actions.perform()
        sleep(3)
         
        destino = navegador.find_element('xpath','//*[@id="i21"]/div[4]/div/div/div[1]/div/div/input')
        actions.click(destino)
        actions.send_keys('Teresina')
        actions.send_keys(Keys.ENTER)
        actions.perform()
        sleep(3)
        
        ida = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input')
        actions.click(ida)
        actions.send_keys('01/01/2024')
        actions.send_keys(Keys.ENTER)
        actions.perform()
        sleep(3)

        volta = navegador.find_element('xpath','//*[@id="ow81"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input')
        actions.click(volta)
        actions.send_keys('01/02/2024')
        actions.send_keys(Keys.ENTER)
        actions.perform()
        sleep(3)

        confirmar_data = navegador.find_element('xpath','//*[@id="ow81"]/div[2]/div/div[3]/div[3]/div/button')
        confirmar_data.click()

        confirmar = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button')
        confirmar.click()

        wait = WebDriverWait(navegador, 10)
        preco_element = wait.until(EC.visibility_of_element_located(('xpath', '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span')))

        preço = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span')
        preço = preço.text
        print(preço)

        horario_chegada = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[1]/span')
        horario_chegada = horario_chegada.text
        print(horario_chegada)

        companhia = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[2]/span')
        companhia = companhia.text
        print(companhia) 

        paradas = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[4]/div[1]/span')
        paradas = paradas.text
        print(paradas)

        embarque = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span')
        embarque = embarque.text
        print(embarque)

        desembarque = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span')
        desembarque = desembarque.text
        print(desembarque)

        sleep(1000)

    except:
        sleep(100)
        continue
