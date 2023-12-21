import os
from random import randint


class Luta:
    def __init__(self,
                 j_nome,
                 j_vida,
                 j_habilidade,
                 j_sorte,
                 j_status,
                 m_nome,
                 m_vida,
                 m_habilidade,
                 m_status='Vivo'):
        self.dado1 = None
        self.j_nome = j_nome
        self.j_vida = j_vida
        self.j_habilidade = j_habilidade
        self.j_sorte = j_sorte
        self.j_status = j_status
        self.m_nome = m_nome
        self.m_vida = m_vida
        self.m_habilidade = m_habilidade
        self.m_status = m_status


    def dado(self):
        self.dado1 = randint(1, 6)
        return self.dado1

    def combate(self):
        # Luta por Round jogador.
        rodada = 0
        while self.m_vida > 0:
            rodada = 1 + rodada
            # print(f'Round: {rodada}')
            m_ataque = self.m_habilidade + randint(1, 6)
            j_ataque = self.j_habilidade + randint(1, 6)
            # print(f'O Ataque do {self.m_nome} é {m_ataque} ')
            # print(f'O Ataque do {self.j_nome} é {j_ataque}')
            # print('')
            if m_ataque == j_ataque:
                pass  # print('Roud Empatado')
            elif m_ataque > j_ataque:
                # print(f'Vitória do {self.m_nome}')
                self.j_vida = self.j_vida - 2
                if self.j_vida <= 0:
                    # print(f'{self.j_nome} Morreu! \nGame Over!!!')
                    self.j_status = 'Morto'
                    # os.system("pause")
                    # sys.exit()
                else:
                    pass  # print(f'{self.m_nome} tem {self.m_vida} de vida')
                    # print(f'{self.j_nome} tem {self.j_vida} de vida')
            elif m_ataque < j_ataque:
                # print(f'Vitória do {self.j_nome}')
                self.m_vida = self.m_vida - 2
                if self.m_vida <= 0:
                    # print(f'{self.m_nome} Morreu! \nVitoria!!!')
                    self.m_status = 'Morto'
                else:
                    pass  # print(f'{self.m_nome} tem {self.m_vida} de vida')
                    # print(f'{self.j_nome} tem {self.j_vida} de vida')
            os.system("pause")


def dado():
    dado1 = randint(1, 6)
    return dado1


print(dado())
