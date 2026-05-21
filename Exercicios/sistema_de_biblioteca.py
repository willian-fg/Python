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
        print(f"O Livro {objeto_livro.titulo} foi adicionado.")


    def pegar_emprestado(self, titulo_do_livro):
        livro_encontrado = False
        for livro in self.acervo:
            if livro.titulo == titulo_do_livro:
                if livro.disponivel == True:
                    livro.disponivel = False
                    livro_encontrado
                    print(f"Empréstimo do Livro {livro.titulo} realizado sucesso!")
                    break
            
            if livro.titulo == titulo_do_livro:
                if livro.disponivel == False:
                    print(f"O livro {livro.titulo} ja está emprestado!")
                    break



    def devolver_livro(self, titulo_do_livro):
        for livro in self.acervo:
            if livro.titulo == titulo_do_livro:
                livro.disponivel == True
                print(f"Livro {livro.titulo} devolvido com sucesso!")
                break
 








livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Hobbit", "J.R.R Tolkien")

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.pegar_emprestado("Dom Casmurro")
biblioteca.pegar_emprestado("Dom Casmurro")
biblioteca.devolver_livro("Dom Casmurro")
