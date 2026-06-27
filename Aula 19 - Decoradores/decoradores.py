# ==============================================================================
# AULA DE FUNÇÕES E DECORADORES EM PYTHON
# ==============================================================================

# 1. O que é uma Função?
# Uma função é um bloco de código isolado que só roda quando é chamado.
# Usamos a palavra-chave 'def', seguida do nome e parênteses. 
# IMPORTANTE: O código interno precisa de indentação (4 espaços).

def minha_funcao():
    print("Olá! Esta é uma função básica executada.")

# Chamando a função:
minha_funcao()


# 2. Parâmetros e Argumentos (Passando dados)
# Parâmetro: É a variável definida na assinatura da função (ex: nome).
# Argumento: É o valor real enviado ao chamar a função (ex: "Carlos").

def saudar_usuario(nome):
    print(f"Seja muito bem-vindo, {nome}!")

saudar_usuario("Carlos")


# 3. O Retorno de uma Função
# O 'return' serve para a função devolver um valor para quem a chamou.
# Depois que o 'return' é executado, a função é imediatamente encerrada.

def somar(a, b):
    return a + b

resultado = somar(5, 7)
print(f"Resultado da soma: {resultado}")


# 4. Funções como Cidadãs de Primeira Classe (First-Class Citizens)
# Isso significa que, em Python, funções podem ser salvas em variáveis,
# passadas como argumentos ou retornadas por outras funções.

# Passo 1: Funções Aninhadas (Uma função dentro da outra)
def pai():
    print("Estou na função pai.")
    
    def filho():
        print("Estou na função filho (aninhada).")
        
    filho()  # Executa internamente

pai()


# Passo 2 & 3: Decoradores (O Conceito do "Embrulho" e o Açúcar Sintático '@')
# Um decorador recebe uma função original, adiciona um comportamento antes/depois 
# e devolve esse "embrulho" modificado.

def meu_decorador(funcao_original):
    def embrulho():
        print("[Aviso]: A ação vai começar no terminal...")
        funcao_original()  # Executa a função original recebida como ingrediente
        print("[Aviso]: A ação terminou com sucesso.")
    return embrulho

# Utilizando a Sintaxe Mágica do @ (Açúcar Sintático / Syntactic Sugar)
# O Python automaticamente faz: salvar_dados = meu_decorador(salvar_dados)
@meu_decorador
def salvar_dados():
    print("-> Salvando dados no banco de dados...")

# Executando a função decorada:
salvar_dados()


# ==============================================================================
# 🦾 DESAFIO RÁPIDO RESOLVIDO: O Decorador @gritar
# Criar um decorador que transforma o retorno de uma função em maiúsculas (.upper())
# ==============================================================================

def gritar(funcao_original):
    def embrulho():
        # Recebe o texto retornado pela função original
        texto_original = funcao_original()
        # Modifica para letras maiúsculas
        return texto_original.upper()
    return embrulho

@gritar
def saudar_neovim():
    return "estou programando funções no meu neovim!"

# Testando o desafio:
print("\n--- Resultado do Desafio Rápido ---")
print(saudar_neovim())
