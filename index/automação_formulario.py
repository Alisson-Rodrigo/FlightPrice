from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


while True:
    try:
        navegador = webdriver.Chrome()
        actions = ActionChains(navegador)
        navegador.get("https://www.google.com/travel/flights?sca_esv=555979541&output=search&q=passagens+aereas&source=lnms&mode_promoted=true&impression_in_search=true&sa=X&sqi=2&ved=2ahUKEwjtxKnJm9WAAxXfLrkGHXdLBN4Q0pQJegQICRAB")

        origem = navegador.find_element('xpath','//*[@id="i21"]/div[1]/div/div/div[1]/div/div/input')
        actions.click(origem)
        actions.send_keys_to_element(origem, "\b")
        actions.send_keys('Rio de Janeiro')
        actions.send_keys(Keys.ENTER)
        actions.perform()
        WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath','//*[@id="i21"]/div[4]/div/div/div[1]/div/div/input')))
         
        destino = navegador.find_element('xpath','//*[@id="i21"]/div[4]/div/div/div[1]/div/div/input')
        actions.click(destino)
        actions.send_keys('Sao paulo')
        actions.send_keys(Keys.ENTER)
        actions.perform()
        WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input')))
    

        ida = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input')
        actions.click(ida)
        actions.send_keys('01/01/2024')
        actions.send_keys(Keys.ENTER)
        actions.perform()
        WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath','//*[@id="ow81"]/div[2]/div/div[3]/div[3]/div/button')))
  
        volta = navegador.find_element('xpath','//*[@id="ow81"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input')
        actions.click(volta)
        actions.send_keys('01/02/2024')
        actions.send_keys(Keys.ENTER)
        actions.perform()
        WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath','//*[@id="ow81"]/div[2]/div/div[3]/div[3]/div/button')))

        confirmar_data = navegador.find_element('xpath','//*[@id="ow81"]/div[2]/div/div[3]/div[3]/div/button')
        confirmar_data.click()

        confirmar = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button')
        confirmar.click()

        lista_preços = ['//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[4]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[5]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span']

        lista_companhias = ['//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[2]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[2]/div[2]/span[1]','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[4]/div/div[2]/div/div[2]/div[2]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[5]/div/div[2]/div/div[2]/div[2]/div[2]/span[1]']

        lista_paradas = ['//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[4]/div[1]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[4]/div[1]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[4]/div[1]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[4]/div/div[2]/div/div[2]/div[4]/div[1]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[5]/div/div[2]/div/div[2]/div[4]/div[1]/span']

        lista_horarios_partida = ['//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[4]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[5]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span']

        lista_horarios_chegada = ['//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[4]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[5]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span']

        count = 0
        for c in range(5):
            wait = WebDriverWait(navegador, 10)
            preco_element = wait.until(EC.visibility_of_element_located(('xpath', f'{lista_preços[count]}')))
            preço = navegador.find_element('xpath',f'{lista_preços[count]}')
            preço = preço.text
            print(preço)

            companhia = navegador.find_element('xpath',f'{lista_companhias[count]}')
            companhia = companhia.text
            print(companhia) 

            paradas = navegador.find_element('xpath',f'{lista_paradas[count]}')
            paradas = paradas.text
            print(paradas)

            horario_partida = navegador.find_element('xpath',f'{lista_horarios_partida[count]}')
            horario_partida = horario_partida.text
            print(horario_partida)

            horario_chegada = navegador.find_element('xpath',f'{lista_horarios_chegada[count]}')
            horario_chegada = horario_chegada.text
            print(horario_chegada)
            print('-------------------')
            print('')
            count += 1
        navegador.quit()
        break
    except:
        print('Erro ao carregar a página, tentando novamente...')
        continue
