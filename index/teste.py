from flightPrice_package import Scraping_voos


var = Scraping_voos('Rio de janeiro','Sao paulo','17/01/2024','17/01/2024')
var2 = var.buscar_voos()
print (var2)