"""
Normalmente quando de cria uma função normanlmente se usa a palavra-chave def, dá um nome,
define os parametros e coloca um return
"""
# --- Jeito padrão

def ao_quadrado(x):
    return x ** 2

print(ao_quadrado(4)) # 16

quadrado_lambda = lambda x: x ** 2

print(quadrado_lambda(4))

# formula = lambda parameter_list: expression


#Exemplo Pratico:

produtos = [{"nome": "Teclado", "preco": 150},
            {"nome": "Mouse", "preco": 80},
            {"nome": "Monitor", "preco": 900}]

produtos.sort(key=lambda item: item["preco"])

print(produtos)

