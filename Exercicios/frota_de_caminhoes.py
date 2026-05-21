from time import sleep
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = 100

    def abastecer(self):
        self.combustivel = 100
        print("O Veiculo foi abastecido")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas 

    def abrir_porta_malas(self):
        print(f"Porta malas do carro de {self.portas} aberto!")


class Caminhao(Veiculo):
    def __init__(self, marca, modelo, eixos):
        super().__init__(marca, modelo)
        self.eixos = eixos

    def carregar_cacamba(self):
        print(f"Carregando a caçamba do caminhão de {self.eixos} com mercadorias")
        sleep(4)
        print("Carregado.")

# ----- Testando ------

# --- criando objetos
meu_carro = Carro("Toyota", "Corolla", 4)
meu_caminhao = Caminhao("Volvo", "FH 540", 6)

# --- Testando a Herança
print(f"Carro: {meu_carro.marca} {meu_carro.modelo} | Combustível: {meu_carro.combustivel}")
meu_carro.abastecer()

# --- Testando Métodos Exclusivos

meu_carro.abrir_porta_malas()
meu_caminhao.carregar_cacamba()

# --- teste de erro
#meu_carro.carregar_cacamba()
    
        
