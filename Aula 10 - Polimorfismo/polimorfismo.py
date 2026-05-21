                     ''' ----- Polimorfismo -----'''

'''A palavra significa muitas formas. Na prática é quando duas classes filhas 
tem um método com o mesmo nome, mas cada um executa esse método de um jeito 
diferente( Específico para ela).'''

        ''' --- Sintax --- '''

class Animal:
    def __init__(self, nome):
        self.nome = nome


    def emitir_som():
        print("Esse animal emite um som genérico")




class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Au Au!")




class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Miau!")



# ----- Testando

dog = Cachorro("Rex")
cat = Gato("Mingau")

dog.emitir_som()
cat.emitir_som()
