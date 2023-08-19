from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from time import sleep

class Buscador_voos:
    """
    Classe para obter o menor preço de passagens aéreas atraves da biblioteca selenium, utilizando o navegador Google Chrome,para fazer a raspagem de dados do site Google Flights.

    Parameters
    ----------
    origem : str
        Local de origem da viagem.
    destino : str
        Local de destino da viagem.
    ida : str
        Data de ida da viagem.
    volta : str
        Data de volta da viagem.

    Methods
    -------
    melhores_precos()
        Retorna um dicionário com os 5 melhores preços de passagens aéreas, com as seguintes informações: preço, companhia, paradas, horario de partida e horario de chegada.

    Returns
    -------
    dict
        Dicionário com os 5 melhores preços de passagens aéreas, com as seguintes informações: preço, companhia, paradas, horario de partida e horario de chegada.

    
    """
    
    
    def __init__(self,origem,destino,ida,volta):
        self.origem_campo = origem
        self.destino_campo = destino
        self.ida_campo = ida
        self.volta_campo = volta
        self.dicionario_voos = {}


        self.lista_preços = ['//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[4]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[5]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span']

        self.lista_companhias = ['//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[2]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[2]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[4]/div/div[2]/div/div[2]/div[2]/div[2]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[5]/div/div[2]/div/div[2]/div[2]/div[2]/span']

        self.lista_paradas = ['//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[4]/div[1]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[4]/div[1]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[4]/div[1]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[4]/div/div[2]/div/div[2]/div[4]/div[1]/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[5]/div/div[2]/div/div[2]/div[4]/div[1]/span']

        self.lista_horarios_partida = ['//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[4]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[5]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span']

        self.lista_horarios_chegada = ['//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[4]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[5]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span']
              

    def melhores_precos(self):
        """
        Retorna um dicionário com os 5 melhores preços de passagens aéreas, com as seguintes informações: preço, companhia, paradas, horario de partida e horario de chegada.

        Parameters
        ---------- 
        none

        Returns
        -------
        dict
            Dicionário com os 5 melhores preços de passagens aéreas, com as seguintes informações: preço, companhia, paradas, horario de partida e horario de chegada.

        """
        try:


            chrome_options = Options()
            chrome_options.add_argument('--headless')  
            chrome_options.add_argument('--disable-gpu')  
            chrome_options.add_argument('--window-size=1920x1080')


            navegador = webdriver.Chrome()

            actions = ActionChains(navegador)
            navegador.get("https://www.google.com/travel/flights?sca_esv=555979541&output=search&q=passagens+aereas&source=lnms&mode_promoted=true&impression_in_search=true&sa=X&sqi=2&ved=2ahUKEwjtxKnJm9WAAxXfLrkGHXdLBN4Q0pQJegQICRAB")
            sleep(2)

            origem = navegador.find_element('xpath','//*[@id="i21"]/div[1]/div/div/div[1]/div/div/input')
            actions.click(origem)
            actions.send_keys_to_element(origem, "\b")
            actions.send_keys(self.origem_campo)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath','//*[@id="i21"]/div[4]/div/div/div[1]/div/div/input')))
            sleep(2)
            
            
            destino = navegador.find_element('xpath','//*[@id="i21"]/div[4]/div/div/div[1]/div/div/input')
            actions.click(destino)
            actions.send_keys(self.destino_campo)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input')))
            sleep(2)
        

            ida = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input')
            actions.click(ida)
            actions.send_keys(self.ida_campo)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath','//*[@id="ow81"]/div[2]/div/div[3]/div[3]/div/button')))
            sleep(2)
    
            volta = navegador.find_element('xpath','//*[@id="ow81"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input')
            actions.click(volta)
            actions.send_keys(self.volta_campo)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            WebDriverWait(navegador, 10).until(EC.presence_of_element_located(('xpath','//*[@id="ow81"]/div[2]/div/div[3]/div[3]/div/button')))
            sleep(2)

            confirmar_data = navegador.find_element('xpath','//*[@id="ow81"]/div[2]/div/div[3]/div[3]/div/button')
            confirmar_data.click()

            confirmar = navegador.find_element('xpath','//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button')
            confirmar.click()
            sleep(2)

            count = 0
            while navegador.find_elements('xpath',f'{self.lista_preços[count]}') != []:
                wait = WebDriverWait(navegador, 10)
                wait.until(EC.visibility_of_element_located(('xpath', f'{self.lista_preços[count]}')))
            

                preço = navegador.find_element('xpath',f'{self.lista_preços[count]}') 
                preço = preço.text

                companhia = navegador.find_element('xpath',f'{self.lista_companhias[count]}')
                companhia = companhia.text

                paradas = navegador.find_element('xpath',f'{self.lista_paradas[count]}')
                paradas = paradas.text

                horario_partida = navegador.find_element('xpath',f'{self.lista_horarios_partida[count]}')
                horario_partida = horario_partida.text

                horario_chegada = navegador.find_element('xpath',f'{self.lista_horarios_chegada[count]}')
                horario_chegada = horario_chegada.text

                info_voo = {
                    'preço': preço,
                    'companhia': companhia,
                    'paradas': paradas,
                    'horario_partida': horario_partida.replace('\u202f', '') + '',
                    'horario_chegada': horario_chegada.replace('\u202f', '') + ''
                }
                chave = f'voo{count + 1}'  
                self.dicionario_voos[chave] = info_voo 
                count += 1
            for c in self.dicionario_voos:
                print(self.dicionario_voos[c])
            sleep(2)
            return self.dicionario_voos  
        except:
            print('Erro ao carregar a página, tentando novamente...')

if __name__ == '__main__':
    var = Buscador_voos('São Paulo','Rio de Janeiro','10/10/2023','20/10/2023')
    var2 = var.melhores_precos()
    print(var2)
       

