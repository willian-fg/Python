# ==============================================================================
# APRENDA CLASSES E OBJETOS EM PYTHON (MOLDE VS OBJETO REAL)
# ==============================================================================

# 1. DEFINIÇÃO DA CLASSE (O MOLDE)
# Usamos a palavra-chave 'class' com a primeira letra Maiúscula.
class Carro:
    
    # 2. O MÉTODO CONSTRUTOR (__init__)
    # Ele define quais características (atributos) todo carro DEVE ter ao nascer.
    # O 'self' representa o carro específico que está sendo criado no momento.
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca       # Atributo
        self.modelo = modelo     # Atributo
        self.ano = ano           # Atributo
        self.cor = cor           # Atributo
        self.ligado = False      # Atributo com valor padrão (todo carro nasce desligado)

    # 3. MÉTODOS (AS AÇÕES QUE O CARRO PODE FAZER)
    # Importante: Todo método dentro da classe precisa receber o 'self' primeiro!
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} deu a partida: Vrum vrum!")
        else:
            print(f"O {self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O {self.modelo} foi desligado.")
        else:
            print(f"O {self.modelo} já está desligado.")

    def acelerar(self, velocidade):
        if self.ligado:
            print(f"O {self.modelo} acelerou para {velocidade} km/h!")
        else:
            print(f"Erro: Você não pode acelerar um carro desligado!")


# ==============================================================================
# 4. INSTANCIAÇÃO (CRIANDO OBJETOS REAIS A PARTIR DO MOLDE)
# ==============================================================================

print("--- Criando e usando o Carro 1 ---")
# Criamos o primeiro objeto (carro_do_joao) passando os dados que o __init__ pede:
carro_do_joao = Carro("Chevrolet", "Onix", 2022, "Preto")

# Acessando características (Atributos) usando o ponto '.'
print(f"Carro do João: {carro_do_joao.marca} {carro_do_joao.modelo} {carro_do_joao.cor}")

# Executando ações (Métodos) no carro do João:
carro_do_joao.acelerar(60)  # Vai dar erro porque está desligado
carro_do_joao.ligar()       # Liga o carro
carro_do_joao.acelerar(60)  # Agora funciona!
carro_do_joao.desligar()    # Desliga o carro

print("\n--- Criando e usando o Carro 2 ---")
# Criamos um objeto completamente independente a partir do mesmo molde:
carro_da_maria = Carro("Fiat", "Pulse", 2024, "Cinza")

print(f"Carro da Maria: {carro_da_maria.marca} {carro_da_maria.modelo}")
# Note que as ações da Maria não afetam o carro do João:
carro_da_maria.ligar()
print(f"O carro do João está ligado? {carro_do_joao.ligado}")
print(f"O carro da Maria está ligado? {carro_da_maria.ligado}")