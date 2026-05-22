'''
                        List Comprehension

A list Comprehension faz tudo que uma lista normal faz, (só que tudo em uma linha!)
é mais rapido para o computador processar.
'''

# ------ Jeito tradicional (Com 3 linhas) -----

numeros = [1, 2, 3, 4, 5]
dobros = []

for n in numeros:
    dobros.append(n * 2)

print(dobros)

# ------ Novo Jeito (Com 1 linha) ------

numeros2 = [1, 2, 3, 4, 5]

dobros2 = [n * 2 for n in numeros2] 

# -- formula = [(o que eu quero fazer) for item in lista_original]


