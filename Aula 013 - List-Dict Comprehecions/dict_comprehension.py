"""
A lógica é a mensma do "List Comprehensions" só muda a chaves
no dicionario precisamos definir (chave: valor)

"""

produtos = ["Teclado", "Mouse", "Monitor"]
precos = [150, 80, 900]

dicionario_precos = {prod: preco for prod, preco in zip(produtos, precos)}

print(dicionario_precos)

