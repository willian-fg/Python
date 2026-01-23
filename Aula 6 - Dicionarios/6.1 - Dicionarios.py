# Um dicionário é uma estrutura de dados que armazena no formato
chave - valor

usuario = {
    'nome': 'Willian',
    'idade': 34,
    'altura': 1000,

}

print(usuario)

# Acessando os valores 
print(usuario['nome'])

#Chaves inesistentes geram erro -- KeyError --- a foma mais segura de acessar é:

print(usuario.get("peso", "Não Informado"))

# Adicionando dados

usuario["pesso"] = 80 #Chave inesistentes são adicionandas
usuario["idade"] = 43 #chaves exitentes são alteradas

# Deletando dados
del usuario["peso"]
#ou
usuario.pop("peso")


# Percorrendo um dicionário

# Apenas chaves
for chave in usuario:
    print(chave)

# Chaves e valores
for chave, valor in usuario.itens():
    print(chave, ":", valor)

# Métodos importantes
usuario.Keys() # Todas as Chaves
usuario.values() #Todos os Valores
usuario.itens() pares (chave, valor)

# ------ Exemplo pratico -------

cadastro = {}

cadastro["nome"] = input("Nome: ")
cadastro["idade"] = input("Idade: ")

# -- Lista de dicionários

usuarios = [
    {"nome": "Ana"},
    {"nome": "Carlos"}
 
]

