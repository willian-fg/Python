class Avião:
    def __init__(self, codigo, destino, capacidade):
        self.codigo = codigo
        self.destino = destino
        self.capacidade = capacidade
        self.passageiros_abordados = 0

class PainelAeroporto:
    def __init__(self):
        self.voos_agendados = []

    def registrar_voo(self, objeto_aviao):
        self.voos_agendados.append(objeto_aviao)
        print(f" Voo [{objeto_aviao.codigo}] com destino a [{objeto_aviao.destino}] foi registrado no painel.")

    def embarcar_passageiros(self, codigo_de_voo, quantidade):
        for aviao in self.voos_agendados:
            if aviao.codigo == codigo_de_voo:
                if aviao.passageiros_abordados + quantidade > aviao.capacidade:
                    print(f"Erro: O voo {aviao.codigo} excedeu a capacidade")
                else:
                    aviao.passageiros_abordados += quantidade


    def exibir_painel_geral(self):
        print(" ----- Painel Geral -----")
        for aviao in self.voos_agendados:
            print( f"Voo: {aviao.codigo} | Destino: {aviao.destino} | Passageiros: {aviao.passageiros_abordados}")


# ----- voos ---------

aviao1 = Avião("AZU-4412", "Rio de Janeiro", 150)
aviao2 = Avião("TAM-3301", "Salvador", 200)

aeroporto = PainelAeroporto()

aeroporto.registrar_voo(aviao1)
aeroporto.registrar_voo(aviao2)

# ----- Embarques 

print(" ----- Iniciando Embarques -----")
aeroporto.embarcar_passageiros("AZU-4412", 120)
aeroporto.embarcar_passageiros("TAM-3301", 250)

# ----- Painel

print("\n === PAINEL DE EMBARQUE DE VOOS === ")
aeroporto.exibir_painel_geral()
