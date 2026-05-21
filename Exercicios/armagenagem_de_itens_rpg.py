class Item:
    def __init__(self, nome, tipo, raridade):
        self.nome = nome
        self.tipo = tipo
        self.raridade = raridade

class Inventario:
    def __init__(self):
        self.itens = []
    
    def adicionar_item(self, novo_item):
        self.novo_item = novo_item
        self.itens.append(self.novo_item)
        print(f'Novo item "{self.novo_item.nome}" adicionado.')

    def listar_itens(self):
        if len(self.itens) == 0:
            print("O Inventario está vazio.")
            return
        
        for item in self.itens:
            print(f"Nome: {item.nome} | Tipo: {item.tipo} | Raridade: {item.raridade}")

    def buscar_por_raridade(self, raridade_procurada):
        for item in self.itens:
            if item.raridade == raridade_procurada:
                print(f"Item: {item.nome} ({item.tipo})")

item1 = Item("Espada de Fogo", "Arma", "Lendario")
item2 = Item("Poção de Vida", "Poção", "Comun")
item3 = Item("Escudo de Ferro", "Armadura", "Comum") #4040104
item4 = Item("Cajado Arcano", "Arma", "Raro")

meu_inventario = Inventario()

meu_inventario.listar_itens()

meu_inventario.adicionar_item(item1)
meu_inventario.adicionar_item(item2)
meu_inventario.adicionar_item(item3)
meu_inventario.adicionar_item(item4)

print("\n ---- Meus Itens ---- ")
meu_inventario.listar_itens()

print("\n ---- Item Comuns ---- ")
meu_inventario.buscar_por_raridade("Comun")
