# -- Herança 
#É a capacidade de uma classe (chamada filha) herdar automaticamente,
#todos os atributos de outra classe.
# Evita repetição de código(DRY - Don't Repeat Yourself)


''' Sintaxe Básica'''
class veiculo: #Classe Mãe(Geral)
    def __init__(self, marca):
        self.marca = marca

class Carro(Veiculo):
    def __init__(self, marca, portas):
        super().__init__(marca) # Envia 'marca' para a (Classe Mãe) guardar
        self.portas = portas # Guarda o atributo exclusivo do filho
