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
