# FlightPrice Package
O pacote Flight Price é uma ferramenta que permite buscar os melhores preços de voos por meio de web scraping em diferentes sites de companhias aéreas e agências de viagens. Com este pacote, você pode automatizar a busca por preços competitivos para suas viagens.

Instalação
Para instalar o pacote Flight Price, você pode usar o pip. Abra um terminal e execute o seguinte comando: pip install flight-price

Uso
import FlightPrice as flp

#utilizando a biblioteca.
scraper = FlightScraper('São paulo','Rio de janeiro','17/01/2024','17/02/2024')
voos = scraper.buscar_voos()

#Exibindo informações dos voos.
for c,k in var.items():
    print(var[c])


Contribuição
Contribuições são bem-vindas! Se você quiser melhorar o pacote Flight Price, sinta-se à vontade para abrir uma pull request no repositório do GitHub.


Aviso Legal
O pacote Flight Price foi desenvolvido apenas para fins educacionais e de demonstração. O web scraping pode violar os termos de serviço de alguns sites. Certifique-se de estar em conformidade com as políticas de uso dos sites que você deseja fazer scraping.

Licença
Este projeto é licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter mais detalhes.