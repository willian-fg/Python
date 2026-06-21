# Estamos a dizer: "Do arquivo modelos, importa o Carro e a função"
from modelos import Carro, formatar_carro


garagem = [
    Carro(marca="Chevrolet", modelo="Onix", ano=2022),
    Carro(marca="Toyota", modelo="Corolla", ano=2023)
]

print("--- Sistema de Gestão da Garagem ---")
for carro in garagem:
    # Usamos a função que veio lá do módulo 'modelos.py'
    texto_formatado = formatar_carro(carro)
    print(texto_formatado)
