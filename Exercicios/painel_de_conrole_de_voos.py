class Avião:
    def __init__(self, codigo, destino, capacidade, passageiros_abordados):
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
                if 

