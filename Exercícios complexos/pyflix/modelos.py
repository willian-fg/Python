from collections import namedtuple


Filme = namedtuple('filme', ['titulo', 'genero', 'nota'])

class Catalogo:
    def __init__(self):
        self.filmes = []


    def adicionar_filmes(self, filme):
        self.filmes.append(filme)

    def buscar_por_genero(self, genero):
        return [f for f in self.filmes if f.genero.lower() == genero.lower()]

    def __str__(self):
        quantidade = len(self.filmes)
        return f'Catalogo Pyflix com {quantidade} filme(s) cadastrados(s)'
    
    def obter_todos(self):
        return self.filmes
