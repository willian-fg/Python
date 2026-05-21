"""
Conjunto é uma coleção:
- Não ordenada,
- Sem Valores duplicados,
- Mutável

"""

numeros = {1, 2, 3, 3, 5,}
print(numeros) # {1, 2, 3, 4, 5}

#----- Criando conjuntos -----

conjunto = set()
conjunto.add(10)
conjunto.add(20)

#----- Operaçãoes com conjuntos-----

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)    #união
print(a & b)    #interseção
print(a - b)    #diferença

#----- Veificando a existencia-----

if 3 in a:
    print("Existe")

#----- Quando usar set -----

"""se set quando:

Precisa remover duplicatas

Precisa verificar existência rapidamente

Não importa a ordem
"""
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]
emails_unicos = set(emails)
#----- -----