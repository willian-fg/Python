# Named tuple pode ser chamada de "mini-classe" para variaveis.
# você cria uma vorma e depois pode fazer várias variaveis iguais

# ----- Jeito simples de fazer tupla -----
ponto = (4, -2)

# Para acessar, você precisa lembrar o que o índice significa:
print(ponto[0]) # É o X? É o Y? Código confuso.

# ----- Namedtuple -----

from collections import namedtuple

# 1. Você define o "Molde" (Nome da tupla e os campos que ela vai ter)
Ponto = namedtuple('Ponto', ['x', 'y'])

# 2. Você cria o objeto passando os valores por nome
meu_ponto = Ponto(x=4, y=-2)

# 3. Você acessa os dados usando um ponto (igual em uma classe!)
print(meu_ponto.x)  # Resultado: 4
print(meu_ponto.y)  # Resultado: -2
