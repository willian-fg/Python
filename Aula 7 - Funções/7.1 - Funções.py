# ==============================================================================
# APRENDA FUNÇÕES EM PYTHON (RESUMO PRÁTICO)
# ==============================================================================

# 1. FUNÇÃO BÁSICA (Sem parâmetros e sem retorno)
# Usa-se 'def' para definir. O código interno precisa estar indentado.
def exibir_boas_vindas():
    print("Olá! Bem-vindo ao mundo das funções em Python.")

# Chamando a função básica:
exibir_boas_vindas()


# 2. FUNÇÃO COM PARÂMETROS (Recebendo dados)
# 'nome' e 'curso' são variáveis que vão receber os valores na hora da chamada.
def saudar_estudante(nome, curso):
    print(f"Sucesso nos seus estudos de {curso}, {nome}!")

# Chamando e passando os 'argumentos':
saudar_estudante("Carlos", "Python")


# 3. FUNÇÃO COM PARÂMETRO PADRÃO (Default)
# Se você não enviar o 'pais', ele assume automaticamente "Brasil".
def definir_nacionalidade(nome, pais="Brasil"):
    print(f"{nome} nasceu no(a) {pais}.")

definir_nacionalidade("Mariana")          # Usa o padrão (Brasil)
definir_nacionalidade("John", "Canadá")   # Substitui o padrão por Canadá


# 4. FUNÇÃO COM RETORNO (Retornando dados)
# O 'return' envia o resultado de volta e encerra a função imediatamente.
def calcular_desconto(preco_original, porcentagem):
    desconto = preco_original * (porcentagem / 100)
    preco_final = preco_original - desconto
    return preco_final  # Devolve o valor final para quem chamou

# Guardando o resultado do retorno dentro de uma variável:
valor_a_pagar = calcular_desconto(100, 15)
print(f"O preço com desconto é: R$ {valor_a_pagar}")


# 5. RETORNANDO MÚLTIPLOS VALORES
# O Python permite devolver mais de uma informação ao mesmo tempo.
def analisar_numero(numero):
    if numero % 2 == 0:
        tipo = "Par"
    else:
        tipo = "Ímpar"
    
    dobro = numero * 2
    return tipo, dobro  # Retorna duas coisas separadas por vírgula

# Capturando os dois retornos em duas variáveis diferentes:
resultado_tipo, resultado_dobro = analisar_numero(7)
print(f"O número 7 é {resultado_tipo} e o seu dobro é {resultado_dobro}.")