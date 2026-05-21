"""3. Operadores Lógicos

Operadores lógicos permitem combinar condições.

3.1 and (E lógico)

Retorna True se todas as condições forem verdadeiras.
"""

idade = 20
tem_carteira = True

print(idade >= 18 and tem_carteira)


"""
Tabela verdade simplificada:

True and True → True

True and False → False

3.2 or (OU lógico)

Retorna True se pelo menos uma condição for verdadeira.
"""

print(idade < 18 or tem_carteira)

"""
3.3 not (NÃO lógico)

Inverte o valor booleano.
"""
ativo = False
print(not ativo)  # True
