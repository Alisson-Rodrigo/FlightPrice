class Melhores_voos:
    def __init__(self, origem, destino, ida, volta):
        self.origem = origem
        self.destino = destino
        self.ida = ida
        self.volta = volta

    def __str__(self):
        return f"Rota: {self.origem} -> {self.destino}\nIda: {self.ida}\nVolta: {self.volta}"
