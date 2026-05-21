class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True



class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, objeto_livro):
        self.acervo.append(objeto_livro)
        print(f"O livro {objeto_livro.titulo} foi adicionado ao acervo")
    

    def pegar







livroteste = Livro("O livro", "Dev",)

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livroteste)

