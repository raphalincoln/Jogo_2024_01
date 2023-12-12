import random


class Jogador:
    j_nome = None
    j_energia = None
    j_energia_inicial = None
    j_habilidade = None
    j_habilidade_inicial = None
    j_sorte = None
    j_sorte_inicial = None
    j_status = None
    j_ouro = None
    j_provisao = None
    j_pocao = None
    def __init__(self,
                 j_nome="TestJão",
                 j_energia=12 + random.randint(1, 6) + random.randint(1, 6),
                 j_habilidade=6 + random.randint(1, 6),
                 j_sorte=6 + random.randint(1, 6),
                 j_status="Vivo",
                 j_provisao=10,
                 j_ouro=600,
                 j_pocao="Sorte",
                 j_energia_inicial=0,
                 j_habilidade_inicial=0,
                 j_sorte_inicial=0):
        self.j_nome = j_nome
        self.j_vida = j_energia
        self.j_habilidade = j_habilidade
        self.j_sorte = j_sorte
        self.j_status = j_status
        self.j_provisao = j_provisao
        self.j_ouro = j_ouro
        self.j_pocao = j_pocao
        self.j_energia = j_energia_inicial
        self.j_habilidade = j_habilidade_inicial
        self.j_sorte = j_sorte_inicial

        print("Criando Personagem")