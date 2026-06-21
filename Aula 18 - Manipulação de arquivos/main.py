from modelos import Carro, formatar_carro

# A nossa lista de carros na memória RAM
garagem = [
    Carro(marca="Chevrolet", modelo="Onix", ano=2022),
    Carro(marca="Toyota", modelo="Corolla", ano=2023),
    Carro(marca="Fiat", modelo="Uno", ano=2015)
]

print("--- A guardar os dados no arquivo ---")

# O COMANDO MÁGICO ENTRA AQUI:
# 'w' significa 'write' (escrever). Ele cria o arquivo ou limpa se já existir.
with open("garagem.txt", "w", encoding="utf-8") as arquivo:
    for carro in garagem:
        texto = formatar_carro(carro)
        
        # Escreve a linha no arquivo e adiciona o '\n' para pular de linha
        arquivo.write(texto + "\n")

print("Prontinho! Arquivo 'garagem.txt' gerado com sucesso.")
