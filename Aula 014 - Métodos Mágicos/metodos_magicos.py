"""
Servem para explicar para o Python como ele deve se comportar ao interagir com recursos da linguagem,
como print(), len() ou os operadore (+, -, ==).
"""



# 1. __str__ (Apresentação amigável)
# evita - <__main__.CofreBancario object at 0x7f8b04gb90>

#2. __repr__ (A Representação do Programador)
# define como os objetos vão ser apresentados 

class CofreBancario:
    def __init__(self, dono, senha):
        self.dono = dono
        self.__senha = senha
        self.__bloqueio = True
        self.__saldo = 0


    # O método mágico
    def __str__(self):
        return f"Cofre Digital do(a) {self.dono} | Status: {self.__bloqueio}"
    
    # A representação
    def __repr__(self):
        return f"CofreBancario(dono='{self.dono}', senha='{self.__senha}')"

cofre1 = CofreBancario("Junior", 1234)
cofre2 = CofreBancario("laura", 4321)

sala_do_cofre = [cofre1, cofre2]
print(cofre1)
print(sala_do_cofre)



#3 ----- Usando a função nativa de representação repr()
print(repr(cofre2))
print(repr(sala_do_cofre))




