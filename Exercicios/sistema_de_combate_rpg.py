class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome 
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar_oponente(self, oponente):
        dano = self.ataque - oponente.defesa
        if dano > 0:
            oponente.vida -= dano

guerreiro = Personagem("Aragorn", vida=100, ataque=25, defesa=12)
mago = Personagem("Grandalf", vida=80, ataque=30, defesa=5)

while (guerreiro.vida > 0) and (mago.vida > 0):
    # --- TURNO DO GUERREIRO ---
    guerreiro.atacar_oponente(mago)
    print(f"Mago( vida: {mago.vida} ) | Guerreiro(Vida: {guerreiro.vida})")
    
    if mago.vida <= 0:
        print("Guerreiro Venceu!!!")
        break  # Interrompe o loop na hora, o mago não contra-ataca!

    # --- TURNO DO MAGO ---
    mago.atacar_oponente(guerreiro)
    print(f"Mago( vida: {mago.vida} ) | Guerreiro(Vida: {guerreiro.vida})")
    
    if guerreiro.vida <= 0:
        print("Mago Venceu!!!")
        break  # Interrompe o loop na hora!

