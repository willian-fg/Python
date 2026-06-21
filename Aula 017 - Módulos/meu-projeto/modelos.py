from collections import namedtuple

# Definimos a nossa "mini-classe" aqui dentro
Carro = namedtuple('Carro', ['marca', 'modelo', 'ano'])

# Podemos também criar uma função auxiliar para formatar o texto do carro
def formatar_carro(carro):
    return f"🚗 {carro.marca} {carro.modelo} ({carro.ano})"
