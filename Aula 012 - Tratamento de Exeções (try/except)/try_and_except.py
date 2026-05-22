            """  Tratamento de Exceções """

"""
É a técnica usada para impedir que seu programa (trave e feche na cara do usuário)
quando acontece um erro inesperado durante a execução. Em vez de derrubar o sistema nós 
capituramos o erro e decidimos o que deve ser feito.
"""

""" --- Erro de Sintaxe vs. Exceçõe """

"""
Erro de Sintaxe: Ocorre quando o código é escrito com a gramática errada
do Python(ex: esquecer os dois pontos(:). O programa nem chega a rodar.

Exceção: O código etá escrito certo, mas algo da errado enquanro ele roda 
(ex: Dividir um número por zero, ou tentar abrir um arquivo que não existe)
"""

# ------ Estrutura Básica ______
try:
   #O código que você quer rodar, mas pode dar erro
    numero = int(input("Digite um número:"))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")

except ZeroDivisionError:
    #O que fazer se o usuário digitar 0
                print("Erro: Não é possivel dividir um número por 0")
except ValueError:
    print("Erro: Por favor digite apenas números inteiros!")


# ------ Blocos complementares (else/finally)

try:
    arquivo = open("dados.txt", "r")

except FileNotFoundError:
    print("O arquivo não foi encontrado")

else:                                  # Executa se o try acontecer perfeitamente
    print("Arquivo lido com sucesso")

finally:                                         # Executa de qualquer jeito com ou sem erro!!
    print("Encerrando a conexão com o arquivo.")

