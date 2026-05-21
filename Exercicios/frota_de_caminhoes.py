class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = 100

    def abastecer(self):
        self.combustivel = 100
        print("O Veiculo foi abastecido")

class Carro(Veiculo):

    def abrir_porta_malas(self):
        print("Porta malas do carro aberto!")


class Caminhao(Veiculo):

    def carregar_cacamba()
        print("Carregando a caçamba com mercadorias")
        sleep(4)
        print("Carregado.")

# ----- Testando ------

# --- criando objetos
meu_carro = Carro("Toyota", "Corolla")
meu_caminhao = Caminhao("Volvo", "FH 540")

# --- Testando a Herança
print(f"Carro: {meu_carro.marca} {meu_carro.modelo} | Combustível: {meu_carro.combustivel}")
meu_carro.abastecer()

# --- Testando Métodos Exclusivos

meu_carro.abrir_porta_malas()
meu_caminhao.carregar_cacamba()

# --- teste de erro
#meu_carro.carregar_cacamba()
    
        
