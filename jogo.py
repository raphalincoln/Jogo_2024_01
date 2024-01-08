import tkinter
import os
from random import randint
from tkinter import *
from tkinter import messagebox

from fase_montanha import Fase
from jogador_Montanha import Jogador

pastaApp = os.path.dirname(__file__)
root = Tk()


def dado():
    jogar_dado = randint(1, 6)
    return jogar_dado


class Application:

    def __init__(self):
        self.usou_pocao = None
        self.bt_usar_pocao = None
        self.trechos = None
        self.trecho = None
        self.jogo = None
        self.inventario = None
        self.frame_1 = None
        self.frame_2 = None
        self.frame_trechos = None
        self.duelo = None
        self.root = root
        self.tela()
        self.batalha = None
        self.frames_da_tela()
        self.criando_interface()
        self.lbfra_inventario = None
        self.bt_testar_sorte = None
        self.bt_pegar_item = None
        self.bt_pegar_ouro = None
        self.validar_trecho_a = None
        self.validar_trecho_b = None
        self.validar_trecho_c = None
        self.validar_trecho_d = None
        self.validar_trecho_e = None
        self.bt_j_validar_nome = None
        self.alterar_sorte = None
        self.alterar_valor = None

        # criando o Loop
        root.mainloop()

    def tela(self):
        self.root.title("O Feiticeiro da Montanha de Fogo")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x600+10+15")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=700)
        self.root.minsize(width=500, height=300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root,
                             bd=4,
                             background='#dfe3ee',
                             highlightbackground='#dfe3ee',
                             highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.026, relwidth=0.475, relheight=0.96)

        self.frame_2 = Frame(self.root,
                             bd=4,
                             background='#dfe3ee',
                             highlightbackground='#dfe3ee',
                             highlightthickness=6)
        self.frame_2.place(relx=0.51, rely=0.026, relwidth=0.475, relheight=0.96)

    def tela_regras_batal(self):
        self.batalha = tkinter.Toplevel()
        self.batalha.title("Regras de Batalhas")
        self.batalha.geometry("500x580+10+15")
        self.batalha.configure(background='white')
        self.batalha.resizable(False, False)
        # Titulo das Regras de batalha
        lb_regras_batalha_titulo = Label(self.batalha,
                                         text="Regras de Batalha",
                                         background="white")
        lb_regras_batalha_titulo.place(relx=0.25,
                                       rely=0.01,
                                       relwidth=0.5,
                                       relheight=0.045)

        # Texto da Ajuda de Batalha
        lb_regras_batalha_ajuda = Label(self.batalha,
                                        text="Quando for instruído a lutar com uma criatura, a batalha será descrita\n "
                                             "informando o nome da criatura. Primeiro, observe os valores de \n"
                                             "HABILIDADE e ENERGIA da criatura (como apresentados na página \n"
                                             "em que você estiver). A sequência do combate é:\n"
                                             "Serão rolados dois dados para a criatura e os resultados "
                                             "serão somados à\n"
                                             "HABILIDADE dela. Este total é a força de ataque da criatura.\n"
                                             "Serão rolados dois dados para você e os resultados serão somados a sua "
                                             "HABILIDADE.\n"
                                             "Este total é a tua força de ataque.\n"
                                             "Quem tem a força de ataque maior? Se for você, então feriu a criatura.\n"
                                             "Se for a criatura, então ela o feriu (se for um empate, ambos erraram\n"
                                             "recomece a próxima rodada de combate a partir do passo 1, acima).\n"
                                             "Se tiver ferido a criatura, será diminuído 2 pontos da ENERGIA dela.\n"
                                             "Você pode usar a SORTE para aumentar o dano \n"
                                             "(veja Usando a sorte em batalhas).\n"
                                             "Se a criatura tiver ferido você, será diminuído 2 pontos da sua "
                                             "ENERGIA.\n"
                                             "Você pode usar a SORTE para diminuir o dano (veja Usando a sorte "
                                             "em batalhas).\n"
                                             "As mudanças necessárias na ENERGIA da criatura ou na sua própria \n"
                                             "(e na sua SORTE, caso a tenha usado) serão feitas e começará a próxima\n"
                                             "rodada de combate.\n"
                                             "O combate continua até que o valor de ENERGIA de um de "
                                             "vocês seja reduzido\n"
                                             "a zero (morte).\n"
                                             "\n"
                                             "Escapando de uma batalha:\n"
                                             "\n"
                                             "Em algumas páginas você terá a opção de escapar da batalha. "
                                             "Você\n"
                                             "só pode fazer isso se lhe for oferecido na página. \n"
                                             "Se decidir escapar, a criatura que você estiver \n"
                                             "enfrentando acerta automaticamente um golpe (será diminuído \n"
                                             "2 pontos de ENERGIA) enquanto você foge tal. Este é o preço \n"
                                             "da covardia. Você pode usar a SORTE neste ferimento \n"
                                             "normalmente (veja Usando a sorte em batalhas).\n",
                                        background="white")
        lb_regras_batalha_ajuda.place(relx=0.005,
                                      rely=0.067,
                                      relwidth=1,
                                      relheight=0.83)

        # Botão de Cancelar
        self.bt_batalha = Button(self.batalha,
                                 text="Cancelar",
                                 command=self.batalha.destroy)
        self.bt_batalha.place(relx=0.35, rely=0.90, relwidth=0.25, relheight=0.065)

    def tela_regras_itens(self):
        self.itens = tkinter.Toplevel()
        self.itens.configure(background='white')
        self.itens.geometry("500x580+10+15")
        self.itens.title("Regras de Batalhas")
        self.itens.resizable(False, False)
        # Titulo das Regras de Itens
        lb_regras_itens_titulo = Label(self.itens,
                                       text="Regras de Itens",
                                       background="white")
        lb_regras_itens_titulo.place(relx=0.25,
                                     rely=0.01,
                                     relwidth=0.5,
                                     relheight=0.045)

        # Texto da Ajuda de Itens
        lb_regras_itens_ajuda = Label(self.itens,
                                      text="Você começa a aventura com uma espada, uma armadura de couro, um escudo,\n "
                                           "uma mochila com dez provisões para a viagem e um lampião para iluminar o\n"
                                           " caminho. \n"
                                           "Mas você vai encontrar muitos outros itens durante o desenrolar\n "
                                           "da aventura. Você também pode levar uma poção mágica para ajudá-lo \n"
                                           "em sua missão. \n"
                                           "\n"
                                           "Escolha uma dentre as seguintes opções:\n"
                                           "Poção de habilidade: restaura pontos de HABILI DADE.\n"
                                           "Poção do vigor: restaura pontos de ENERGIA.\n"
                                           "Poção da fortuna: restaura pontos de SORTE e adiciona 1 à\n"
                                           "sua SORTE inicial.\n"
                                           "Essas poções podem ser bebidas a qualquer momento durante a aventura\n"
                                           "(exceto no meio de uma batalha). Beber uma poção sempre vai restaurar\n"
                                           "a sua HABILIDADE, ENERGIA ou SORTE ao seus valores iniciais. A poção\n"
                                           "da fortuna vai aumentar o seu valor inicial de SORTE em 1 \n"
                                           "ponto e restaurar a SORTE ao seu novo nível inicial.\n"
                                           "Cada poção só pode ser usada uma vez durante uma aventura.\n"
                                           "Quando usar uma poção, isso será anotado em Cabeçalho.",
                                      background="white")
        lb_regras_itens_ajuda.place(relx=0.005,
                                    rely=0.067,
                                    relwidth=1,
                                    relheight=0.83)

        # Botão de Cancelar
        self.bt_itens = Button(self.itens,
                               text="Cancelar",
                               command=self.itens.destroy)
        self.bt_itens.place(relx=0.35, rely=0.90, relwidth=0.25, relheight=0.065)

    def tela_regras_atributos(self):
        self.atributos = tkinter.Toplevel()
        self.atributos.title("Regras de Atributos")
        self.atributos.geometry("500x580+10+15")
        self.atributos.configure(background='white')
        self.atributos.resizable(False, False)
        # Titulo das Regras de Itens
        lb_regras_atributos_titulo = Label(self.atributos,
                                           text="Regras de Atributos",
                                           background="white")
        lb_regras_atributos_titulo.place(relx=0.25,
                                         rely=0.01,
                                         relwidth=0.5,
                                         relheight=0.045)

        # Texto da Ajuda de Itens
        lb_regras_atributos_ajuda = Label(self.atributos,
                                          text="Habilidade\n"
                                               "Seu valor de Habilidade não mudará muito durante sua aventura.\n"
                                               "Ocasionalmente, uma página trará instruções para que você altere o "
                                               "seu valor de\n"
                                               "HABILIDADE. Uma arma mágica pode aumentar sua HABILIDADE, "
                                               "por exemplo, mas\n"
                                               "lembre-se de que apenas uma arma pode ser usada por vez! Assim, você\n"
                                               "não ganhará dois bônus de usar duas armas mágicas (pois só\n"
                                               "pode usar uma por vez). Não se esqueça de que a sua HABILIDADE\n"
                                               "nunca pode ultrapassar o valor inicial, a menos que\n"
                                               "especificamente instruído.\n"
                                               "Beber uma poção de habilidade (veja Equipamento e Poções) sempre\n"
                                               "vai restaurar a sua HABILIDADE ao valor inicial.\n"
                                               "Energia:\n"
                                               "O seu valor de ENERGIA vai mudar muito durante a aventura. Quando se\n"
                                               "aproximar do objetivo, o seu nível de ENERGIA pode estar perigosamente"
                                               " baixo, e\n"
                                               "as batalhas irão se tornar especialmente arriscadas por isso, tenha"
                                               " cuidado!\n"
                                               "Você começa o jogo com dez provisões; cada uma é suficiente para uma"
                                               " refeição.\n"
                                               "Você pode comer a qualquer momento, exceto durante as batalhas.\n"
                                               "Quando comer, será somado 4 pontos ao seu valor de ENERGIA e\n"
                                               "deduzirá uma das provisões. Acompanhe no Cabeçalho do Personagem\n"
                                               "as provisões restantes. Lembre-se de que você tem um longo\n"
                                               "caminho a percorrer-assim, use suas provisões com sabedoria!\n"
                                               "Não se esqueça de que a sua ENERGIA nunca pode ultrapassar o valor"
                                               " inicial,\n"
                                               "a menos que especificamente instruído. Beber uma poção do vigor\n"
                                               "(veja Equipamento e poções) sempre vai restaurar a sua ENERGIA ao"
                                               " valor inicial.\n"
                                               "Sorte\n"
                                               "Você vai receber bônus ao seu valor de SORTE quando for especialmente"
                                               " sortudo.\n"
                                               "Não se esqueça de que, da mesma forma que HABILIDADE e ENERGIA, a sua\n"
                                               "SORTE nunca pode ultrapassar o valor inicial, a menos que"
                                               " especificamente\n"
                                               "instruído. Beber uma poção da fortuna (veja Equipamento e poções)"
                                               " sempre vai \n"
                                               "restaurar a sua SORTE ao valor inicial, e aumentar o seu valor \n"
                                               "inicial de SORTE em 1 ponto.\n",

                                          background="white")
        lb_regras_atributos_ajuda.place(relx=0.005,
                                        rely=0.067,
                                        relwidth=1,
                                        relheight=0.83)

        # Botão de Cancelar
        self.bt_atributos = Button(self.atributos,
                                   text="Cancelar",
                                   command=self.atributos.destroy)
        self.bt_atributos.place(relx=0.35, rely=0.90, relwidth=0.25, relheight=0.065)

    def tela_regras_sorte(self):
        self.sorte = tkinter.Toplevel()
        self.sorte.title("Regras de Atributos")
        self.sorte.geometry("500x580+10+15")
        self.sorte.configure(background='white')
        self.sorte.resizable(False, False)
        # Titulo das Regras de Itens
        lb_regras_sorte_titulo = Label(self.sorte,
                                       text="Regras de Sorte",
                                       background="white")
        lb_regras_sorte_titulo.place(relx=0.25,
                                     rely=0.01,
                                     relwidth=0.5,
                                     relheight=0.045)

        # Texto da Ajuda de Sorte
        lb_regras_sorte_ajuda = Label(self.sorte,
                                      text="Sorte\n"
                                           "Algumas vezes você terá de testar a sorte. Como você vai descobrir,\n"
                                           "usar a sorte é um negócio arriscado.\n"
                                           "Para testar a sorte, siga as instruções abaixo:\n"
                                           "Serão rolados dois dados e se o resultado for igual ou menor que \n"
                                           "a sua SORTE atual, você foi sortudo. Se o resultado for maior que a \n"
                                           "sua SORTE atual, então você foi azarado. \n"
                                           "As consequências de ser sortudo ou azarado \n"
                                           "são descritas na página.\n"
                                           "Cada vez que testar a sorte, será diminuído um ponto do seu\n"
                                           "valor atual de SORTE. Assim, quanto mais você \n"
                                           "depender da sorte, mais irá se arriscar\n"
                                           "\n"
                                           "Usando a sorte em batalhas:\n"
                                           "\n"
                                           "Em batalhas, você sempre tem a opção de usar a sorte \n"
                                           "para acertar um golpe mais sério em uma criatura, ou \n"
                                           "para reduzir os efeitos de um ferimento que a criatura \n"
                                           "tenha lhe causado.\n"
                                           "Se você tiver acabado de ferir a criatura, \n"
                                           "você pode testar a sorte para aumentar o ferimento. \n"
                                           "Se for sortudo, você causa 2 pontos de dano extras \n"
                                           "(ou seja, em vez de causar 2 pontos de dano, você causa 4). \n"
                                           "Se for azarado, você causa 1 ponto de dano a menos \n"
                                           "(assim, em vez de causar 2 pontos de dano, você causa 1).\n"
                                           "Se a criatura tiver acabado de ferir você: \n"
                                           "você pode testar a sorte para diminuir o ferimento. Se for \n"
                                           "sortudo, você sofre 1 ponto de dano a menos (ou seja, em vez de \n"
                                           "sofrer 2 pontos de dano, você sofre 1). Se for azarado, "
                                           "você sofre 1 ponto \n"
                                           "de dano extra (assim, em vez de sofrer 2 pontos de dano, você sofre 3).\n"
                                           "Não esqueça, será diminuído 1 ponto do seu valor de \n"
                                           "SORTE cada vez que testar a sorte.",
                                      background="white")
        lb_regras_sorte_ajuda.place(relx=0.005,
                                    rely=0.067,
                                    relwidth=1,
                                    relheight=0.83)

        # Botão de Cancelar
        self.bt_sorte = Button(self.sorte,
                               text="Cancelar",
                               command=self.sorte.destroy)
        self.bt_sorte.place(relx=0.35, rely=0.90, relwidth=0.25, relheight=0.065)

    def abrir_regras(self):
        self.regra = tkinter.Toplevel()
        self.regra.title("Regras")
        self.regra.geometry("200x580+20+25")
        self.regra.configure(background='white')
        self.regra.resizable(True, True)
        self.regra.maxsize(width=800, height=700)
        self.regra.minsize(width=500, height=300)
        # Titulo das Regras
        lb_regras_titulo = Label(self.regra,
                                 text="Regras",
                                 background="white")
        lb_regras_titulo.place(relx=0.25,
                               rely=0.01,
                               relwidth=0.5,
                               relheight=0.035)
        # Apresentação das Regras
        lb_regras_apresentacao = Label(self.regra,
                                       text="O Feiticeiro da Montanha de Fogo é uma aventura de fantasia em que "
                                            "você é o herói.\n "
                                            "Mas antes de começar,você deve criar seu personagem, rolando dados para \n"
                                            "determinar seus valores de HABILIDADE, ENERGIA e SORTE.\n"
                                            "Esses valores mudarão a cada vez que você iniciar a aventura "
                                            "e você poderá \n"
                                            "acompanhar sua evolução na espaço Cabeçalho, mas, fique atento, "
                                            "a variação \n"
                                            "nunca será maior que o valor inicial de cada atributo, excetoem momento \n"
                                            "bem especial e estará claramente descrito na página. ",
                                       background="white")
        lb_regras_apresentacao.place(relx=0.05,
                                     rely=0.055,
                                     relwidth=0.90,
                                     relheight=0.20)

        # Titulo da criação de Personagem
        lb_regras_criacao = Label(self.regra,
                                  text="Criação de Personagem",
                                  background="white")
        lb_regras_criacao.place(relx=0.25,
                                rely=0.26,
                                relwidth=0.5,
                                relheight=0.035)

        # Apresentação da Criação do Personagem
        lb_regras_apresentacao2 = Label(self.regra,
                                        text="Determinando Habilidade, Energia e Sorte\n"
                                             "Para definir seus valores iniciais de HABILIDADE, ENERGIA e SORTE:\n"
                                             "Vamos rolar um dado e somar 6 ao resultado e esta será a sua Habilidade\n"
                                             "Vamos rolar dois dados e somar 12 ao resultado e  esta será"
                                             " a sua Energia\n"
                                             "Vamos rolar um dado e somar 6 ao resultado e esta será a sua Sorte.\n"
                                             "HABILIDADE mede a sua perícia em combate quanto mais alta, melhor.\n"
                                             "ENERGIA representa o seu vigor físico, a sua saúde; quanto mais \n"
                                             "alta a sua ENERGIA, mais tempo você sobreviverá.\n"
                                             "SORTE reflete o quão sortudo você é. Sorte e magia são forças"
                                             " reais no mundo\n"
                                             "de fantasia que você está prestes a explorar.\n"
                                             "Para criar o personagem, clique em “Criar” na tela inicial",
                                        background="white")
        lb_regras_apresentacao2.place(relx=0.05,
                                      rely=0.30,
                                      relwidth=0.9,
                                      relheight=0.30)

        # Botão de Batalhas
        bt_regras_batal = Button(self.regra,
                                 text="Batalhas",
                                 command=self.tela_regras_batal)
        bt_regras_batal.place(relx=0.17, rely=0.65, relwidth=0.2, relheight=0.035)

        # Botão de Sorte
        bt_regras_sorte = Button(self.regra,
                                 text="Sorte",
                                 command=self.tela_regras_sorte)
        bt_regras_sorte.place(relx=0.57, rely=0.85, relwidth=0.2, relheight=0.035)

        # Botão de Atributos
        bt_regras_atributos = Button(self.regra,
                                     text="Atributos",
                                     command=self.tela_regras_atributos)
        bt_regras_atributos.place(relx=0.17, rely=0.85, relwidth=0.2, relheight=0.035)

        # Botão de Itens
        bt_regras_itens = Button(self.regra,
                                 text="Itens",
                                 command=self.tela_regras_itens)
        bt_regras_itens.place(relx=0.57, rely=0.65, relwidth=0.2, relheight=0.035)

        # Botão de Cancelar
        self.bt_cancelar_Regra = Button(self.regra,
                                        text="Cancelar",
                                        command=self.regra.destroy)
        self.bt_cancelar_Regra.place(relx=0.35, rely=0.93, relwidth=0.2, relheight=0.035)

    def criar_personagem_tela(self):
        # Criar a tela de criação de personagem
        self.jogador01 = Jogador
        self.personagem = tkinter.Toplevel()
        self.personagem.title("Criação de Pesonagem")
        self.personagem.geometry("500x580+10+15")
        self.personagem.configure(background='#98d37e')
        self.personagem.resizable(False, False)

        # Titulo da Criação de Persongem
        lb_j_titulo_sorte = Label(self.personagem,
                                  text="Crie Seu Personagem",
                                  background="#98d37e",
                                  font="arial")
        lb_j_titulo_sorte.place(relx=0.25,
                                rely=0.01,
                                relwidth=0.5,
                                relheight=0.045)

        # Fundo do Cabeçalho
        cabecalho_imagem = PhotoImage(file=pastaApp + "\\FundoCabeçalhoPNG.png")
        lb_j_cabecalho_imagem = Label(self.personagem,
                                      image=cabecalho_imagem,
                                      background="#98d37e")
        lb_j_cabecalho_imagem.photo = cabecalho_imagem
        lb_j_cabecalho_imagem.place(relx=0.02,
                                    rely=0.1,
                                    relwidth=0.96,
                                    relheight=0.25)

        # Descrição do Nome
        lb_j_descricao_nome = Label(self.personagem,
                                    text='Qual será o nome do seu Guerreiro',
                                    background="#98d37e")
        lb_j_descricao_nome.place(relx=0.1,
                                  rely=0.37,
                                  relwidth=0.5,
                                  relheight=0.045)

        # Entrada do Nome
        self.ent_j_nome = Entry(self.personagem)
        self.ent_j_nome.place(relx=0.575,
                              rely=0.37,
                              relwidth=0.25,
                              relheight=0.045)

        # Botão de Validação do nome
        self.bt_j_validar_nome = Button(self.personagem,
                                        text="OK",
                                        command=self.p_nome)
        self.bt_j_validar_nome.place(relx=0.85,
                                     rely=0.37,
                                     relwidth=0.05,
                                     relheight=0.045)

        # Descrição de Energia
        lb_j_descricao_energia = Label(self.personagem,
                                       text='Para Definir sua Energia\n'
                                            'Vamos jogar 2 dados e somar 12 a eles',
                                       background="#98d37e")
        lb_j_descricao_energia.place(relx=0.1,
                                     rely=0.5,
                                     relwidth=0.4,
                                     relheight=0.06)

        # Descrição de Habilidade
        lb_j_descricao_habilidade = Label(self.personagem,
                                          text='Para Definir sua Habilidade\n'
                                               'Vamos jogar 1 dado e somar 6 a ele',
                                          background="#98d37e")
        lb_j_descricao_habilidade.place(relx=0.1,
                                        rely=0.6,
                                        relwidth=0.4,
                                        relheight=0.06)

        # Descrição de Sorte
        lb_j_descricao_sorte = Label(self.personagem,
                                     text='Para Definir sua Sorte\n'
                                          'Vamos jogar 1 dado e somar 6 a ele',
                                     background="#98d37e")
        lb_j_descricao_sorte.place(relx=0.1,
                                   rely=0.7,
                                   relwidth=0.4,
                                   relheight=0.06)

        # Botão de Jogar Dados de Energia
        self.bt_Calcular_energia = Button(self.personagem,
                                          text="Calcular Energia",
                                          command=self.calcular_energia)
        self.bt_Calcular_energia.place(relx=0.70,
                                       rely=0.5,
                                       relwidth=0.24,
                                       relheight=0.045)

        # Botão de Jogar Dado de Habilidade
        self.bt_Calcular_habilidade = Button(self.personagem,
                                             text="Calcular Habilidade",
                                             command=self.calcular_habilidade)
        self.bt_Calcular_habilidade.place(relx=0.70,
                                          rely=0.6,
                                          relwidth=0.24,
                                          relheight=0.045)

        # Botão de Jogar Dados de Sorte
        self.bt_Calcular_sorte = Button(self.personagem,
                                        text="Calcular Sorte",
                                        command=self.calcular_sorte)
        self.bt_Calcular_sorte.place(relx=0.70,
                                     rely=0.7,
                                     relwidth=0.24,
                                     relheight=0.045)

        # Apresentação Botão Radio de Poção
        lb_escolhapocao = Label(self.personagem,
                                text="Escolha uma Poção",
                                background="#98d37e")
        lb_escolhapocao.place(relx=0.3,
                              rely=0.80,
                              relwidth=0.25,
                              relheight=0.06)

        self.pocao = StringVar()

        # Radio - Energia
        rd_pocao_energia = Radiobutton(self.personagem,
                                       text="Poção de Energia",
                                       value="Energia",
                                       variable=self.pocao,
                                       background="#98d37e")
        rd_pocao_energia.place(relx=0.6,
                               rely=0.75,
                               relwidth=0.3,
                               relheight=0.07)

        # Radio - Habilidade
        rd_pocao_habilidade = Radiobutton(self.personagem,
                                          text="Poção de Habilidade",
                                          value="Habilidade",
                                          variable=self.pocao,
                                          background="#98d37e")
        rd_pocao_habilidade.place(relx=0.6,
                                  rely=0.80,
                                  relwidth=0.3,
                                  relheight=0.07)

        # Radio - Sorte
        rd_pocao_sorte = Radiobutton(self.personagem,
                                     text="Poção de Sorte",
                                     value="Sorte",
                                     variable=self.pocao,
                                     background="#98d37e")
        rd_pocao_sorte.place(relx=0.6,
                             rely=0.85,
                             relwidth=0.3,
                             relheight=0.07)

        rd_pocao_energia.select()

        # Botão de Criar Personagem
        bt_criar = Button(self.personagem,
                          text="Criar",
                          command=self.criar_personagem)
        bt_criar.place(relx=0.15, rely=0.95, relwidth=0.2, relheight=0.035)

        # Botão de Salvar Personagem
        bt_salvar = Button(self.personagem,
                           text="Salvar",
                           command=self.salvar_personagem)
        bt_salvar.place(relx=0.42, rely=0.95, relwidth=0.2, relheight=0.035)

        # Botão de sair da Criação de Personagem
        bt_cancelar = Button(self.personagem,
                             text="Cancelar",
                             command=self.personagem.destroy)
        bt_cancelar.place(relx=0.70, rely=0.95, relwidth=0.2, relheight=0.035)

    def criar_personagem(self):  # Com classe
        # Criando Personagem na Classe
        # Exibir Dados no cabeçalho
        # Exibir Nome
        self.jogador01.j_nome = (self.ent_j_nome.get())
        lb_j_nome = Label(self.personagem,
                          text=self.jogador01.j_nome,
                          background="#98d37e")  # 98d37e
        lb_j_nome.place(relx=0.31, rely=0.171, relwidth=0.17, relheight=0.032)
        lb_j_nome.place(relx=0.31, rely=0.171, relwidth=0.17, relheight=0.032)

        # Exibir dados de Energia
        lb_valor_energia = Label(self.personagem,
                                 text=self.jogador01.j_energia,
                                 background="#98d37e")
        lb_valor_energia.place(relx=0.31, rely=0.21, relwidth=0.17, relheight=0.029)

        # Exibir dados de Habilidade
        lb_valor_habilidade = Label(self.personagem,
                                    text=self.jogador01.j_habilidade,
                                    background="#98d37e")
        lb_valor_habilidade.place(relx=0.31, rely=0.25, relwidth=0.17, relheight=0.029)
        self.bt_criar.configure(state=DISABLED)

        # Exibir dados de Sorte
        lb_valor_sorte = Label(self.personagem,
                               text=self.jogador01.j_sorte,
                               background="#98d37e")
        lb_valor_sorte.place(relx=0.31, rely=0.29, relwidth=0.17, relheight=0.029)

        # Exibir Status
        self.jogador01.j_status = 'Vivo'
        lb_j_status = Label(self.personagem,
                            text=self.jogador01.j_status,
                            background="#98d37e")  # 98d37e
        lb_j_status.place(relx=0.66, rely=0.171, relwidth=0.20, relheight=0.032)

        # Exibir Ouro
        self.jogador01.j_ouro = int(600)
        lb_j_ouro = Label(self.personagem,
                          text=f'{self.jogador01.j_ouro} Peças',
                          background="#98d37e")  # 98d37e
        lb_j_ouro.place(relx=0.66, rely=0.21, relwidth=0.20, relheight=0.032)

        # Exibir Provisões
        self.jogador01.j_provisao = int(10)
        lb_j_provisoes = Label(self.personagem,
                               text=self.jogador01.j_provisao,
                               background="#98d37e")  # 98d37e
        lb_j_provisoes.place(relx=0.66, rely=0.25, relwidth=0.20, relheight=0.032)

        # Exibir Poção
        self.jogador01.j_pocao = self.pocao.get()
        lb_j_pocao = Label(self.personagem,
                           text=self.jogador01.j_pocao,
                           background="#98d37e")  # 98d37e
        lb_j_pocao.place(relx=0.66, rely=0.29, relwidth=0.20, relheight=0.032)

    def calcular_energia(self):
        # Dados de Energia
        self.j_dado_energia1 = int(randint(1, 6))
        self.j_dado_energia2 = int(randint(1, 6))
        self.jogador01.j_energia = self.j_dado_energia1 + self.j_dado_energia2 + 12
        print("Energia: ", self.jogador01.j_energia)
        self.jogador01.j_energia_inicial = self.jogador01.j_energia

        # Escrever no Label de Energia
        self.lb_valor_energia = Label(self.personagem,
                                      text=self.jogador01.j_energia,
                                      background="#98d37e")

        # Escrever dado
        self.lb_valor_energia = Label(self.personagem,
                                      text=f"1º dado: {self.j_dado_energia1}\n"
                                           f"2º dado: {self.j_dado_energia2}",
                                      background="#98d37e")
        self.lb_valor_energia.place(relx=0.55,
                                    rely=0.5,
                                    relwidth=0.12,
                                    relheight=0.06)

        self.bt_Calcular_energia.configure(state=DISABLED)

        return self.jogador01.j_energia

    def calcular_habilidade(self):
        # Calcular Habilidade
        self.j_dado_habilidade = int(randint(1, 6))
        self.jogador01.j_habilidade = self.j_dado_habilidade + 6
        print("Habilidade: ", self.jogador01.j_habilidade)

        # Escrever no Label de Habilidade
        self.lb_valor_habilidade = Label(self.personagem,
                                         text=self.jogador01.j_habilidade,
                                         background="#98d37e")
        # lb_valor_habilidade.place(relx=0.30, rely=0.25, relwidth=0.193, relheight=0.029)

        # Escrever dado
        self.lb_valor_habilidade = Label(self.personagem,
                                         text=f"Dado: {self.j_dado_habilidade}\n",
                                         background="#98d37e")  # 98d37e"
        self.lb_valor_habilidade.place(relx=0.55,
                                       rely=0.6,
                                       relwidth=0.12,
                                       relheight=0.06)
        self.bt_Calcular_habilidade.configure(state=DISABLED)
        self.jogador01.j_habilidade_inicial = self.jogador01.j_habilidade

        return self.jogador01.j_habilidade

    def calcular_sorte(self):
        # Calcular Sorte
        self.j_dado_sorte = int(randint(1, 6))
        self.jogador01.j_sorte = self.j_dado_sorte + 6
        print("Sorte: ", self.jogador01.j_sorte)
        self.jogador01.j_sorte_inicial = self.jogador01.j_sorte

        # Escrever no Label de Sorte
        self.lb_valor_sorte = Label(self.personagem,
                                    text=self.jogador01.j_sorte,
                                    background="#98d37e")
        # lb_valor_sorte.place(relx=0.30, rely=0.29, relwidth=0.193, relheight=0.029)

        # Escrever dado
        self.lb_valor_sorte = Label(self.personagem,
                                    text=f"Dado: {self.j_dado_sorte}\n",
                                    background="#98d37e",  # 98d37e"
                                    anchor="center")
        self.lb_valor_sorte.place(relx=0.55,
                                  rely=0.7,
                                  relwidth=0.12,
                                  relheight=0.06)
        self.bt_Calcular_sorte.configure(state=DISABLED)

        return

    def p_nome(self):
        # Capturar Nome do personagem
        self.jogador01.j_nome = (self.ent_j_nome.get())
        self.lb_j_nome = Label(self.personagem,
                               text=self.jogador01.j_nome,
                               background="#98d37e")  # 98d37e
        # lb_j_nome.place(relx=0.297, rely=0.171, relwidth=0.20, relheight=0.032)
        print(self.jogador01.j_nome)
        self.bt_j_validar_nome.configure(state=DISABLED)

    def salvar_personagem(self):
        # SalvarPersonagem
        print("Salvando Personagem")
        self.personagem.destroy()
        self.bt_criar.configure(state=DISABLED)

    def usar_pocao(self):
        if self.usou_pocao != True:
            self.usou_pocao = True
            # Consumindo de Energia

            if self.jogador01.j_pocao == "Energia":
                print("Tomando poção de energia")
                self.jogador01.j_energia = self.jogador01.j_energia_inicial

            # Consumindo de Habilidade
            if self.jogador01.j_pocao == "Habilidade":
                print("Tomando poção de Habilidade")
                self.jogador01.j_habilidade = self.jogador01.j_habilidade_inicial

            # Consumindo de Sorte
            if self.jogador01.j_pocao == "Sorte":
                print("Tomando poção de Sorte")
                self.jogador01.j_sorte = self.jogador01.j_sorte_inicial + 1

                # Atualizar sorte do jogador
                lb_batalha_j_nome = Label(self.inventario,
                                          text=self.jogador01.j_sorte,
                                          background="gold"
                                          )
                lb_batalha_j_nome.place(relx=0.47,
                                        rely=0.83,
                                        relwidth=0.04,
                                        relheight=0.08)

            self.bt_usar_pocao.configure(state=DISABLED)
        else:
            self.bt_usar_pocao.configure(state=DISABLED)
            print('Voce ja usou poção')

    def usar_provisao(self):
        if self.jogador01.j_energia < self.jogador01.j_energia_inicial:
            if self.jogador01.j_provisao > 0:
                print("Comendo Provisão")
                self.jogador01.j_provisao = self.jogador01.j_provisao - 1
                self.lb_provisao = Label(self.inventario,
                                         background="gold",
                                         text=f"Provisão = {self.jogador01.j_provisao}",
                                         font="arial",
                                         anchor="w")

                self.lb_provisao.place(relx=0.06,
                                       rely=0.25,
                                       relwidth=0.32,
                                       relheight=0.1)

                self.jogador01.j_energia = self.jogador01.j_energia + 4
                lb_batalha_j_nome = Label(self.inventario,
                                          text=self.jogador01.j_energia,
                                          background="gold"
                                          )
                lb_batalha_j_nome.place(relx=0.27,
                                        rely=0.83,
                                        relwidth=0.04,
                                        relheight=0.08)
            else:
                print("Acabaram as Provisoes.")
        else:
            print("Vida ja esta no maximo")
            messagebox.showinfo(title="Vida no Maximo", message=f"Sua vida ja esta no maximo", )

    def exibir_cabecalho(self):
        # Exibir a imgagem
        self.cabecalho = tkinter.Toplevel()
        self.cabecalho.title("Dados do Personagem")
        self.cabecalho.geometry("564x180+10+15")
        self.cabecalho.configure(background='#DBBF9B')
        # self.cabecalho.resizable(False, False)

        # Cabeçalho
        cabecalho_imagem = PhotoImage(file=pastaApp + "\\Tela de Cabeçalho.png")
        lb_j_cabecalho_imagem = Label(self.cabecalho,
                                      image=cabecalho_imagem,
                                      background="#DBBF9B",
                                      anchor="n")
        lb_j_cabecalho_imagem.photo = cabecalho_imagem
        lb_j_cabecalho_imagem.place(relx=0,
                                    rely=0,
                                    relwidth=1,
                                    relheight=1)

        # Mostrar Nome
        lb_nome = Label(self.cabecalho,
                        text=self.jogador01.j_nome,
                        background="#D4B795",  # 98d37e"
                        font="arial")
        lb_nome.place(relx=0.20,
                      rely=0.23,
                      relwidth=0.25,
                      relheight=0.10)

        # Mostrar Energia
        lb_energia = Label(self.cabecalho,
                           text=self.jogador01.j_energia,
                           font="arial",
                           background="#D4B795")  # 98d37e"
        lb_energia.place(relx=0.23,
                         rely=0.365,
                         relwidth=0.2,
                         relheight=0.10)

        # Mostrar Habilidade
        lb_habilidade = Label(self.cabecalho,
                              text=self.jogador01.j_habilidade,
                              font="arial",
                              background="#D4B795")  # 98d37e"
        lb_habilidade.place(relx=0.23,
                            rely=0.5,
                            relwidth=0.2,
                            relheight=0.10)

        # Mostrar Sorte
        lb_sorte = Label(self.cabecalho,
                         text=self.jogador01.j_sorte,
                         font="arial",
                         background="#D4B795")  # 98d37e"
        lb_sorte.place(relx=0.23,
                       rely=0.65,
                       relwidth=0.2,
                       relheight=0.10)

        # Mostrar status
        lb_status = Label(self.cabecalho,
                          text=self.jogador01.j_status,
                          font="arial",
                          background="#D4B795")  # 98d37e"
        lb_status.place(relx=0.65,
                        rely=0.23,
                        relwidth=0.25,
                        relheight=0.12)

        # Mostrar ouro
        lb_ouro = Label(self.cabecalho,
                        text=self.jogador01.j_ouro,
                        font="arial",
                        background="#D4B795")  # 98d37e"
        lb_ouro.place(relx=0.65,
                      rely=0.365,
                      relwidth=0.25,
                      relheight=0.10)

        # Mostrar provisão
        lb_provisao = Label(self.cabecalho,
                            text=self.jogador01.j_provisao,
                            font="arial",
                            background="#D4B795")  # 98d37e"
        lb_provisao.place(relx=0.65,
                          rely=0.500,
                          relwidth=0.25,
                          relheight=0.10)

        # Mostrar poção
        lb_pocao = Label(self.cabecalho,
                         text=self.jogador01.j_pocao,
                         font="arial",
                         background="#D4B795")  # 98d37e"
        lb_pocao.place(relx=0.65,
                       rely=0.65,
                       relwidth=0.25,
                       relheight=0.10)

        # Botão de Cancelar
        bt_cabecalho = Button(self.cabecalho,
                              text="Cancelar",
                              background="#85735D",
                              command=self.cabecalho.destroy)
        bt_cabecalho.place(relx=0.35,
                           rely=0.82,
                           relwidth=0.25,
                           relheight=0.12)

    def iniciar_historia(self):
        self.frame_trechos = Frame(self.root,
                                   bd=1,
                                   background='#dfe3ee',
                                   highlightbackground='gold',
                                   highlightthickness=2)
        self.frame_trechos.place(relx=0.51, rely=0.026, relwidth=0.475, relheight=0.96)
        print(f'Você esta na fase {self.jogo.n_trecho}')

        # Int Var e botoes
        self.destino = IntVar()
        self.jogo.livro()
        # Exibição do numero de Trechos
        lb_trecho = Label(self.frame_trechos,
                          text=f'Você esta na fase {self.jogo.n_trecho}',
                          background="#dfe3ee")
        lb_trecho.place(relx=0.3, rely=0.005, relwidth=0.40, relheight=0.03)

        # Exibição do Texto de Trechos
        lb_trecho = Label(self.frame_trechos,
                          text=self.jogo.texto_trecho,
                          background="blue")
        lb_trecho.place(relx=0.025, rely=0.04, relwidth=0.95, relheight=0.7)

        # Exibição das interaçoes
        self.frame_interacao = Frame(self.frame_trechos,
                                     bd=1,
                                     background='red',
                                     highlightthickness=2)
        self.frame_interacao.place(relx=0.025,
                                   rely=0.75,
                                   relwidth=0.95,
                                   relheight=0.2)

        # Radio do para onde ir
        # Opção 1
        if self.jogo.tem_trecho_a == True:
            if self.jogo.n_trecho_a > 0:
                validar_trecho_a = True
                self.validar_trecho_a = validar_trecho_a
                self.rd_n_trecho_a = Radiobutton(self.frame_interacao,
                                                 text=self.jogo.texto_trecho_a,
                                                 value=self.jogo.n_trecho_a,
                                                 variable=self.destino,
                                                 background="blue",
                                                 anchor=W,
                                                 command=self.exibe)
                self.rd_n_trecho_a.grid(column=0,
                                        row=0)
                '''
                self.rd_n_trecho_a.place(relx=0.06,
                                         rely=0.1,
                                         relwidth=0.88,
                                         relheight=0.2)
                print(self.jogo.n_trecho_a)
                '''
                self.rd_n_trecho_a.select()  # Setar a primeira opção como defalt
                self.jogo.tem_trecho_a = False

        # Opção 2
        if self.jogo.tem_trecho_b == True:
            if self.jogo.n_trecho_b > 0:
                validar_trecho_b = True
                self.validar_trecho_b = validar_trecho_b
                self.rd_n_trecho_b = Radiobutton(self.frame_interacao,
                                                 text=self.jogo.texto_trecho_b,
                                                 value=self.jogo.n_trecho_b,
                                                 variable=self.destino,
                                                 anchor=W,
                                                 background="blue",
                                                 command=self.exibe)
                self.rd_n_trecho_b.grid(column=0,
                                        row=1)
                '''
                self.rd_n_trecho_b.place(relx=0.06,
                                         rely=0.83,
                                         relwidth=0.88,
                                         relheight=0.03)
                print(self.jogo.n_trecho_b)
                '''
                self.jogo.tem_trecho_b = False

        # Opção 3
        if self.jogo.tem_trecho_c == True:
            if self.jogo.n_trecho_c > 0:
                validar_trecho_c = True
                self.validar_trecho_c = validar_trecho_c
                self.rd_n_trecho_c = Radiobutton(self.frame_interacao,
                                                 text=self.jogo.texto_trecho_c,
                                                 value=self.jogo.n_trecho_c,
                                                 variable=self.destino,
                                                 background="blue",
                                                 anchor=W,
                                                 command=self.exibe)
                self.rd_n_trecho_c.grid(column=0,
                                        row=2)
                '''
                self.rd_n_trecho_c.place(relx=0.06,
                                         rely=0.87,
                                         relwidth=0.88,
                                         relheight=0.03)
                '''
                self.jogo.tem_trecho_c = False

        # Opção 4
        if self.jogo.tem_trecho_d == True:
            if self.jogo.n_trecho_d > 0:
                validar_trecho_d = True
                self.validar_trecho_d = validar_trecho_d
                self.rd_n_trecho_d = Radiobutton(self.frame_interacao,
                                                 text=self.jogo.texto_trecho_d,
                                                 value=self.jogo.n_trecho_d,
                                                 variable=self.destino,
                                                 background="blue",
                                                 anchor=W,
                                                 command=self.exibe)
                self.rd_n_trecho_d.grid(column=0,
                                        row=3)
                '''
                self.rd_n_trecho_d.place(relx=0.06,
                                         rely=0.91,
                                         relwidth=0.88,
                                         relheight=0.03)
                '''
                print(self.jogo.n_trecho_d)
                self.jogo.tem_trecho_d = False

        # Opção 5
        if self.jogo.tem_trecho_e == True:
            if self.jogo.n_trecho_e > 0:
                validar_trecho_e = True
                self.validar_trecho_e = validar_trecho_e
                self.rd_n_trecho_e = Radiobutton(self.frame_interacao,
                                                 text=self.jogo.texto_trecho_e,
                                                 value=self.jogo.n_trecho_e,
                                                 variable=self.destino,
                                                 background="blue",
                                                 anchor=W,
                                                 command=self.exibe)
                self.rd_n_trecho_e.grid(column=0,
                                        row=4)
                '''
                self.rd_n_trecho_e.place(relx=0.06,
                                         rely=0.95,
                                         relwidth=0.88,
                                         relheight=0.03)
                '''
                print(self.jogo.n_trecho_e)
                self.jogo.tem_trecho_e = False

        if self.jogo.temluta == True:
            print("tem luta teste Radio")
            if self.jogo.tem_trecho_a == True:
                self.rd_n_trecho_a.configure(state=DISABLED)
            if self.jogo.tem_trecho_b == True:
                self.rd_n_trecho_b.configure(state=DISABLED)
            if self.jogo.tem_trecho_c == True:
                self.rd_n_trecho_c.configure(state=DISABLED)
            if self.jogo.tem_trecho_d == True:
                self.rd_n_trecho_d.configure(state=DISABLED)
            if self.jogo.tem_trecho_e == True:
                self.rd_n_trecho_e.configure(state=DISABLED)
            # Criar o Radio da Luta
            self.rd_n_luta = Radiobutton(self.frame_interacao,
                                         text="Lutar contra " + self.jogo.m_nome,
                                         value=self.jogo.n_trecho_e,
                                         variable=self.destino,
                                         background="blue",
                                         anchor=W,
                                         command=self.luta)
            self.rd_n_luta.grid(column=0,
                                row=5)

            # criando a imagem da Luta
            batalha_imagem = PhotoImage(file=pastaApp + "\\Feiticeiro.png")
            lb_batalha_imagem = Label(self.frame_1,
                                      image=batalha_imagem,
                                      background="blue")
            lb_batalha_imagem.photo = batalha_imagem
            lb_batalha_imagem.place(relx=0.40, rely=0.74, relwidth=0.25, relheight=0.22)

            '''           
            self.rd_n_luta.place(relx=0.06,
                                 rely=0.95,
                                 relwidth=0.88,
                                 relheight=0.03)
            '''
            self.jogo.temluta = False

        # Testardo a sorte fora de luta
        if self.jogo.tem_testar_sorte == True:
            print("")
            print("Testar a sorte")
            if hasattr(self, 'rd_n_trecho_a') and self.rd_n_trecho_a.winfo_exists():
                self.rd_n_trecho_a.configure(state=DISABLED)
            if hasattr(self, 'rd_n_trecho_b') and self.rd_n_trecho_b.winfo_exists():
                self.rd_n_trecho_b.configure(state=DISABLED)
            if hasattr(self, 'rd_n_trecho_c') and self.rd_n_trecho_c.winfo_exists():
                self.rd_n_trecho_c.configure(state=DISABLED)
            if hasattr(self, 'rd_n_trecho_d') and self.rd_n_trecho_d.winfo_exists():
                self.rd_n_trecho_d.configure(state=DISABLED)
            if hasattr(self, 'rd_n_trecho_e') and self.rd_n_trecho_e.winfo_exists():
                self.rd_n_trecho_e.configure(state=DISABLED)

            # Criar o Radio da Sorte
            self.rd_n_sorte = Radiobutton(self.frame_interacao,
                                          text="Testar a Sorte",
                                          value=self.jogo.n_trecho_e,
                                          variable=self.destino,
                                          background="blue",
                                          anchor=W,
                                          command=self.testar_sorte)
            self.rd_n_sorte.grid(column=0,
                                 row=6)
            '''
            self.rd_n_sorte.place(relx=0.06,
                                  rely=0.95,
                                  relwidth=0.88,
                                  relheight=0.03)
            '''
            self.jogo.tem_testar_sorte = False

        # Pegando ouro da história
        if self.jogo.tem_ouro == True:
            print("Pegar Ouro")
            self.jogador01.j_ouro = self.jogador01.j_ouro + self.jogo.ouro_fase
            self.jogo.tem_ouro = False

        # alterando pontos de status
        if self.jogo.alterar_valor == True:
            print("alterar status")
            self.jogador01.j_sorte = self.jogador01.j_sorte + self.jogo.alterar_sorte
            self.jogo.alterar_sorte = 0
            self.jogador01.j_energia = self.jogador01.j_energia + self.jogo.alterar_energia
            self.jogo.alterar_energia = 0
            self.jogador01.j_habilidade = self.jogador01.j_habilidade + self.jogo.alterar_habilidade
            self.jogo.alterar_habilidade = 0
            self.jogo.alterar_valor = False

        # Item
        if self.jogo.tem_item == True:
            print ("Pegar Item Novo")
            if self.jogo.item in self.jogo.lista_item:
                print(f"Voce ja possui {self.jogo.item}")
                # self.bt_pegar_item.configure(state=DISABLED)
            else:
                self.jogo.lista_item.append(self.jogo.item)
                print(f"Você pegou {self.jogo.item}")
                print(f"voce adiquiriu {self.jogo.lista_item[self.jogo.contador]}")
                self.jogo.contador = self.jogo.contador + 1
        self.jogo.tem_item = False

        # Botões
        # Botão Cabeçalho

        self.bt_cabecalho = Button(self.frame_trechos,
                                   text="Cabeçalho",
                                   command=self.exibir_cabecalho)
        self.bt_cabecalho.place(relx=0.2, rely=0.96, relwidth=0.2, relheight=0.035)

        # Botão Inventario
        self.bt_inventario = Button(self.frame_trechos,
                                    text="Inventario",
                                    command=self.exibir_inventario)
        self.bt_inventario.place(relx=0.45, rely=0.96, relwidth=0.2, relheight=0.035)

        # Botão de Sair
        self.bt_sair = Button(self.frame_trechos,
                              text="Cancelar",
                              command=self.frame_trechos.destroy)
        self.bt_sair.place(relx=0.7, rely=0.96, relwidth=0.2, relheight=0.035)

    def start_historia(self):
        self.jogo = Fase()
        self.iniciar_historia()

    def criando_interface(self):
        # Apresentação
        lb_apresentacao = Label(self.frame_1,
                                text="Apresentando o Jogo",
                                background='#dfe3ee')
        lb_apresentacao.place(relx=0.25, rely=0.01, relwidth=0.5, relheight=0.035)

        # Titulo
        lb_titulo = Label(self.frame_1,
                          text="O Feiticeiro da Montanha \nde Fogo",
                          background='#dfe3ee',
                          font="arial")
        lb_titulo.place(relx=0.25, rely=0.08, relwidth=0.57, relheight=0.09)

        # Descrição
        lb_descricao = Label(self.frame_1,
                             text="Nas cavernas da Montanha de Fogo há um grande\n"
                                  "tesouro, guardado por um poderoso e maligno \n"
                                  "Feiticeiro. Ou, pelo menos, é o que dizem os rumores.\n "
                                  "Muitos aventureiros como você já entraram nas \n"
                                  "cavernas para recuperá-lo;\n "
                                  "nenhum jamais retornou\n "
                                  "Você ousa tentar?\n",
                             background='#dfe3ee')
        lb_descricao.place(relx=0.05, rely=0.20, relwidth=0.90, relheight=0.22)

        # O Jogo
        lb_o_jogo = Label(self.frame_1,
                          text="Parte história, parte jogo, \n"
                               "este é um tipo diferente de \n "
                               "livro. Aqui, você é o herói você precisa \n"
                               "apenas de um lápis, uma borracha e dois \n"
                               "dados para embarcar \n"
                               "nesta fantástica aventura.\n ",
                          background='#dfe3ee')
        lb_o_jogo.place(relx=0.05, rely=0.4, relwidth=0.90, relheight=0.24)

        # O Jogo
        lb_o_personagem = Label(self.frame_1,
                                text="Se estiver preparado para a Glória.\n"
                                     "Se tiver coragem para o Desconhecido.\n"
                                     "Se desejar ouro e Poder\n"
                                     "Crie seu personagem e vamos à Luta",
                                background='#dfe3ee')
        lb_o_personagem.place(relx=0.05, rely=0.6, relwidth=0.90, relheight=0.15)

        # Imagem do Feiticeiro
        feiticeiro_imagem = PhotoImage(file=pastaApp + "\\Feiticeiro.png")
        lb_feiticeiro_imagem = Label(self.frame_1,
                                     image=feiticeiro_imagem,
                                     background="blue")
        lb_feiticeiro_imagem.photo = feiticeiro_imagem
        lb_feiticeiro_imagem.place(relx=0.40, rely=0.74, relwidth=0.25, relheight=0.22)

        # Inicio da História
        lb_intuducao = Label(self.frame_2,
                             text=("INTRODUÇÃO\n"
                                   "\n"
                                   "Apenas um aventureiro muito tolo embarcaria em uma missão\n"
                                   " perigosa sem primeiro reunir tantas informações quanto \n"
                                   " possível sobre seu destino e os perigos que ele contém. \n"
                                   " Antes de chegar à Montanha de Fogo, você passou vários \n"
                                   " dias com os habitantes de uma aldeia local, a dois dias\n"
                                   " de viagem do sopé. Sendo uma pessoa carismática, você \n"
                                   " teve facilidad em entrosar-se com os aldeões. Embora \n"
                                   " eles tenham contado muitas histórias sobre o misterioso\n"
                                   " santuário do Feiticeiro, você não tem certeza se todas \n"
                                   " ou alguma delas baseiam-se em fatos. Os aldeões viram \n"
                                   " muitos aventureiros passar em viagem para a montanha, \n"
                                   " mas poucos retornaram. Você tem certeza de que a \n"
                                   " jornada à frente será perigosa. Dos poucos que \n"
                                   " conseguiram retornar à aldeia, nenhum pensou em voltar \n"
                                   " à Montanha de Fogo.\n"
                                   "Parece haver alguma verdade nos boatos de que o tesouro\n"
                                   " do Feiticeiro fica guardado em um magnífico baú com \n"
                                   " duas fechaduras, e que as chaves destas são protegidas \n"
                                   " por várias criaturas dentro da masmorra. O próprio \n"
                                   " Feiticeiro é extremamente poderoso. Alguns o descrevem\n"
                                   " como um velho, outros como um jovem. Alguns dizem que\n"
                                   " seu poder vem de um baralho encantado, outros, de um \n"
                                   " par de luvas de seda negra.\n"
                                   "A entrada da montanha é guardada por um grupo de goblins, \n"
                                   "estúpidas criaturas verruguentas que gostam mesmo é de \n"
                                   "comer e beber. Nas proximidades das câmaras internas, \n"
                                   "as criaturas se tornam mais perigosas. Para alcançar \n"
                                   "as câmaras internas você deve atravessar um rio. \n"
                                   "O serviço de balsa é confiável, mas o balseiro gosta\n"
                                   "de uma barganha, e você deve ter uma peça de ouro para \n"
                                   "pagar pela viagem. Os aldeões também o encorajam a\n"
                                   " manter um bom mapa de sua busca, pois sem um você \n"
                                   " acabará perdido e sem esperanças dentro da montanha.\n"
                                   "Quando finalmente chega seu dia de partir, toda a \n"
                                   "aldeia aparece para desejar uma boa viagem. Lágrimas\n"
                                   " vêm aos olhos de muitas mulheres, jovens ou velhas.\n"
                                   " Você não consegue deixar de se perguntar se são \n"
                                   " lágrimas de pena, derramadas por olhos que jamais \n"
                                   " voltarão a vê-lo...\n"),
                             font=("arial", 7),
                             background='#dfe3ee')
        lb_intuducao.place(relx=0.05, rely=0.03, relwidth=0.90, relheight=0.95)

        # Botão de Criar Personagem
        self.bt_criar = Button(self.frame_1,
                               text="Criar",
                               command=self.criar_personagem_tela)
        self.bt_criar.place(relx=0.06, rely=0.95, relwidth=0.2, relheight=0.035)
        # Botão de Regras
        self.bt_regras = Button(self.frame_1,
                                text="Regras",
                                command=self.abrir_regras)
        self.bt_regras.place(relx=0.45, rely=0.95, relwidth=0.2, relheight=0.035)
        # Botão de Cancelar
        self.bt_cancelar = Button(self.frame_1,
                                  text="Cancelar",
                                  command=root.quit)
        self.bt_cancelar.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.035)

        # Botão de Exibir cabeçalho
        self.bt_cabecalho = Button(self.frame_2,
                                   text="Cabeçalho",
                                   command=self.exibir_cabecalho)
        self.bt_cabecalho.place(relx=0.2, rely=0.95, relwidth=0.2, relheight=0.035)
        # Botão de Iniciar História
        self.bt_iniciar = Button(self.frame_2,
                                 text="Iniciar",
                                 command=self.start_historia)
        self.bt_iniciar.place(relx=0.6, rely=0.95, relwidth=0.2, relheight=0.035)

    def pegar_item(self):
        print("Botão de pegar item")
        '''
       self.jogo.lista_item = self.jogo.item
       print(self.jogo.lista_item, "rweasr")
       print(self.jogo.item)
       '''

        if self.jogo.item in self.jogo.lista_item:
            print(f"Voce ja possui {self.jogo.item}")
            # self.bt_pegar_item.configure(state=DISABLED)
        else:
            self.jogo.lista_item.append(self.jogo.item)
            print(f"Você pegou {self.jogo.item}")
            print(f"voce adiquiriu {self.jogo.lista_item[self.jogo.contador]}")
            self.jogo.contador = self.jogo.contador + 1

        self.bt_pegar_item.configure(state=DISABLED)

    def pegar_ouro(self):
        self.jogador01.j_ouro = self.jogo.ouro_fase + self.jogador01.j_ouro
        print("Pegou ", self.jogo.ouro_fase, "e agora possui ", self.jogador01.j_ouro)
        self.bt_pegar_ouro.configure(state=DISABLED)

    def exibe(self):
        self.jogo.n_trecho = self.destino.get()
        self.frame_trechos.destroy()
        self.iniciar_historia()

    def exibir_inventario(self):
        self.inventario = tkinter.Toplevel()
        self.inventario.title(f"Inventário do Jogador")
        self.inventario.geometry("450x200+10+15")
        self.inventario.resizable(False, False)
        self.inventario.configure(background="blue")

        lb_inventario = Label(self.inventario,
                              background="gold",
                              text="Inventario",
                              font="arial")
        lb_inventario.place(relx=0.12,
                            rely=0.06,
                            relwidth=0.16,
                            relheight=0.1)
        # Provisão
        lb_provisao = Label(self.inventario,
                            background="gold",
                            text=f"Provisão = {self.jogador01.j_provisao}",
                            font="arial",
                            anchor="w")
        lb_provisao.place(relx=0.06,
                          rely=0.25,
                          relwidth=0.32,
                          relheight=0.1)

        bt_usar_provisao = Button(self.inventario,
                                  text="Usar",
                                  command=self.usar_provisao)
        bt_usar_provisao.place(relx=0.4,
                               rely=0.25,
                               relwidth=0.07,
                               relheight=0.1)
        # Poção
        self.lb_pocao = Label(self.inventario,
                              background="gold",
                              text=f"Poção = {self.jogador01.j_pocao}",
                              font="arial",
                              anchor="w")
        self.lb_pocao.place(relx=0.06,
                            rely=0.36,
                            relwidth=0.32,
                            relheight=0.1)

        self.bt_usar_pocao = Button(self.inventario,
                                    text="Usar",
                                    command=self.usar_pocao)
        self.bt_usar_pocao.place(relx=0.4,
                                 rely=0.36,
                                 relwidth=0.07,
                                 relheight=0.1)

        # Exibir dados do personagem
        # Nome do jogador
        lb_batalha_j_nome = Label(self.inventario,
                                  text=self.jogador01.j_nome,
                                  background="gold")
        lb_batalha_j_nome.place(relx=0.07,
                                rely=0.83,
                                relwidth=0.1,
                                relheight=0.08)

        # Energia do jogador
        lb_batalha_j_nome = Label(self.inventario,
                                  text=self.jogador01.j_energia,
                                  background="gold"
                                  )
        lb_batalha_j_nome.place(relx=0.27,
                                rely=0.83,
                                relwidth=0.04,
                                relheight=0.08)

        # Habilidade do jogador
        lb_batalha_j_nome = Label(self.inventario,
                                  text=self.jogador01.j_habilidade,
                                  background="gold"
                                  )
        lb_batalha_j_nome.place(relx=0.37,
                                rely=0.83,
                                relwidth=0.04,
                                relheight=0.08)

        # Sorte do jogador
        lb_batalha_j_nome = Label(self.inventario,
                                  text=self.jogador01.j_sorte,
                                  background="gold"
                                  )
        lb_batalha_j_nome.place(relx=0.47,
                                rely=0.83,
                                relwidth=0.04,
                                relheight=0.08)

        # Itens label
        lbfra_inventario = LabelFrame(self.inventario,
                                      background="blue",
                                      text="Itens!!")
        lbfra_inventario.place(relx=0.48,
                               rely=0.06,
                               relwidth=0.5,
                               relheight=0.68)

        # itens itens dentro
        lb_j_itens = Label(self.inventario,
                           text=self.jogo.lista_item,
                           background="blue",
                           anchor=NW)
        lb_j_itens.place(relx=0.49,
                         rely=0.135,
                         relwidth=0.48,
                         relheight=0.58)

        # Botão para Fechar Janela
        bt_cancelar = Button(self.inventario,
                             text="Fechar",
                             command=self.inventario.destroy)
        bt_cancelar.place(relx=0.56,
                          rely=0.8,
                          relwidth=0.25,
                          relheight=0.14)

    def luta(self):
        # self.bt_luta.configure(state=DISABLED)
        self.rd_n_luta.configure(state=DISABLED)
        self.duelo = tkinter.Toplevel()
        self.duelo.title(f"Combate contra {self.jogo.m_nome}")
        self.duelo.geometry("450x200+10+15")
        self.duelo.resizable(False, False)
        self.duelo.configure(background="red")

        # Fotos do monstro
        imagem02 = ("\\" + self.jogo.m_nome + ".png")
        batalha_imagem = PhotoImage(file=pastaApp + imagem02)
        lb_batalha_imagem = Label(self.duelo,
                                  image=batalha_imagem,
                                  background="red")
        lb_batalha_imagem.photo = batalha_imagem
        lb_batalha_imagem.place(relx=0.02,
                                rely=0.15,
                                relwidth=0.25,
                                relheight=0.7)

        # Nome do jogador
        lb_batalha_j_nome = Label(self.duelo,
                                  text=self.jogador01.j_nome,
                                  background="gold"
                                  )
        lb_batalha_j_nome.place(relx=0.10,
                                rely=0.05,
                                relwidth=0.1,
                                relheight=0.08)

        # Energia do jogador
        lb_batalha_j_nome = Label(self.duelo,
                                  text=self.jogador01.j_energia,
                                  background="gold"
                                  )
        lb_batalha_j_nome.place(relx=0.30,
                                rely=0.05,
                                relwidth=0.04,
                                relheight=0.08)

        # Habilidade do jogador
        lb_batalha_j_nome = Label(self.duelo,
                                  text=self.jogador01.j_habilidade,
                                  background="gold"
                                  )
        lb_batalha_j_nome.place(relx=0.4,
                                rely=0.05,
                                relwidth=0.04,
                                relheight=0.08)

        # Sorte do jogador
        lb_batalha_j_nome = Label(self.duelo,
                                  text=self.jogador01.j_sorte,
                                  background="gold"
                                  )
        lb_batalha_j_nome.place(relx=0.5,
                                rely=0.05,
                                relwidth=0.04,
                                relheight=0.08)

        # Nome do monstro
        lb_batalha_m_nome = Label(self.duelo,
                                  text=self.jogo.m_nome,
                                  background="gold"
                                  )
        lb_batalha_m_nome.place(relx=0.30,
                                rely=0.2,
                                relwidth=0.2,
                                relheight=0.08)

        # Energia do Monstro
        lb_batalha_m_energia = Label(self.duelo,
                                     text=f"Energia {self.jogo.m_energia}",
                                     background="gold")
        lb_batalha_m_energia.place(relx=0.30,
                                   rely=0.3,
                                   relwidth=0.2,
                                   relheight=0.08)

        # Habilidade do Monstro
        lb_batalha_m_habilidade = Label(self.duelo,
                                        text=f"Habilidade {self.jogo.m_habilidade}",
                                        background="gold"
                                        )
        lb_batalha_m_habilidade.place(relx=0.30,
                                      rely=0.40,
                                      relwidth=0.2,
                                      relheight=0.08)

        # Escrever primeiro dado do jogador
        self.j_dado01 = 0
        self.lb_j_dado01 = Label(self.duelo,
                                 background="gold",
                                 text=f"{self.jogador01.j_nome}\n1º dado\n{self.j_dado01}")
        self.lb_j_dado01.place(relx=0.60,
                               rely=0.1,
                               relwidth=0.13,
                               relheight=0.22)

        # Escrever Segundo dado do jogador
        self.j_dado02 = 0
        self.lb_j_dado02 = Label(self.duelo,
                                 background="gold",
                                 text=f"2º dado\n{self.j_dado02}")
        self.lb_j_dado02.place(relx=0.60,
                               rely=0.34,
                               relwidth=0.13,
                               relheight=0.14)

        # Escrever primeiro dado do Monstro
        self.m_dado01 = 0
        self.lb_m_dado01 = Label(self.duelo,
                                 background="gold",
                                 text=f"{self.jogo.m_nome}\n 1º dado\n{self.m_dado01}")
        self.lb_m_dado01.place(relx=0.8,
                               rely=0.1,
                               relwidth=0.13,
                               relheight=0.22)

        # Escrever Segundo dado do Monstro
        self.m_dado02 = 0
        self.lb_j_dado02 = Label(self.duelo,
                                 background="gold",
                                 text=f"2º dado\n{self.m_dado02}")
        self.lb_j_dado02.place(relx=0.8,
                               rely=0.34,
                               relwidth=0.13,
                               relheight=0.14)

        # Escrever Ataque do Monstro
        self.m_ataque = 0
        self.lb_m_ataque = Label(self.duelo,
                                 text=f"Ataque do Monstro\n{self.m_ataque}",
                                 background="gold")
        self.lb_m_ataque.place(relx=0.74,
                               rely=0.50,
                               relwidth=0.25,
                               relheight=0.14)

        # Escrever ataque do Jogador
        self.j_ataque = 0
        self.lb_j_ataque = Label(self.duelo,
                                 text=f"Ataque do Jogador\n{self.j_ataque}",
                                 background="gold")
        self.lb_j_ataque.place(relx=0.47,
                               rely=0.50,
                               relwidth=0.25,
                               relheight=0.14)

        # Atualizar a Energia do Monstro
        lb_batalha_m_energia = Label(self.duelo,
                                     text=f"Energia {self.jogo.m_energia}",
                                     background="gold")
        lb_batalha_m_energia.place(relx=0.30,
                                   rely=0.3,
                                   relwidth=0.2,
                                   relheight=0.08)

        # Atualizar a Energia do jogador
        lb_batalha_j_nome = Label(self.duelo,
                                  text=self.jogador01.j_energia,
                                  background="gold"
                                  )
        lb_batalha_j_nome.place(relx=0.30,
                                rely=0.05,
                                relwidth=0.04,
                                relheight=0.08)

        # Botão Batalha
        self.bt_batalha = Button(self.duelo,
                                 text="Batalhar",
                                 command=self.round)
        self.bt_batalha.place(relx=0.37, rely=0.8, relwidth=0.2, relheight=0.12)

        # Botão de Sair
        self.bt_sair = Button(self.duelo,
                              text="Cancelar",
                              command=self.duelo.destroy)
        self.bt_sair.place(relx=0.75, rely=0.8, relwidth=0.2, relheight=0.12)

        # Desfecho da tela
        self.frame_2.destroy()
        # self.trechos()

    def testar_sorte_luta(self):
        self.bt_testar_sorte_luta.configure(state=DISABLED)
        dados_sorte = dado() + dado()
        if self.jogador01.j_sorte > 0:
            print(f'A soma dos Dados da Sorte é {dados_sorte}\n')
            if self.jogador01.j_sorte > dados_sorte:
                print(f'E sua sorte é de {self.jogador01.j_sorte} e os dados deram {dados_sorte}... \nvoce ganhou!')
                self.sorte_resultado = "sorte"
                if self.vitoria == "monstro":
                    print(f"Que Sorte! \n{self.jogador01.j_nome} recuperou 1 de Energia")
                    self.jogador01.j_energia = self.jogador01.j_energia + 1
                else:
                    print(f"Que Sorte \n{self.jogo.m_nome} perdeu 1 de Energia")
                    self.jogo.m_energia = self.jogo.m_energia - 1
            else:
                print(f'E sua sorte é de {self.jogador01.j_sorte} e os dados deram {dados_sorte}... \nvoce perdeu!')
                self.sorte_resultado = "azar"
                if self.vitoria == "monstro":
                    print(f"Que Azar!\n{self.jogador01.j_nome} perdeu 1 de Energia")
                    self.jogador01.j_energia = self.jogador01.j_energia - 1
                else:
                    print(f"Que Azar! {self.jogo.m_nome} recuperou 1 de Energia")
                    self.jogo.m_energia = self.jogo.m_energia + 1
            self.jogador01.j_sorte = self.jogador01.j_sorte - 1
            print(f"Sua sorte agora é {self.jogador01.j_sorte}\n\n")
            # atualizar os pontos apos calculo de sorte:
            # Energia do Monstro
            lb_batalha_m_energia = Label(self.duelo,
                                         text=f"Energia {self.jogo.m_energia}",
                                         background="gold")
            lb_batalha_m_energia.place(relx=0.30,
                                       rely=0.3,
                                       relwidth=0.2,
                                       relheight=0.08)

            # Energia do jogador
            lb_batalha_j_nome = Label(self.duelo,
                                      text=self.jogador01.j_energia,
                                      background="gold"
                                      )
            lb_batalha_j_nome.place(relx=0.30,
                                    rely=0.05,
                                    relwidth=0.04,
                                    relheight=0.08)

            # Sorte do jogador
            lb_batalha_j_nome = Label(self.duelo,
                                      text=self.jogador01.j_sorte,
                                      background="gold"
                                      )
            lb_batalha_j_nome.place(relx=0.5,
                                    rely=0.05,
                                    relwidth=0.04,
                                    relheight=0.08)

        else:
            print("Seus pontos de sorte acabaram")

    def testar_sorte(self):
        print("testar a sorte fora de luta ")
        self.rd_n_sorte.configure(state=DISABLED)
        self.j_dado_testar_sorte = dado()
        print(self.j_dado_testar_sorte)
        if self.j_dado_testar_sorte >= 4:
            print("deu Sorte")
            self.rd_n_trecho_a["state"] = NORMAL
        else:
            print("deu Azar")
            self.rd_n_trecho_b["state"] = NORMAL

    def round(self):
        self.j_dado01 = dado()
        self.j_dado02 = dado()
        self.m_dado01 = dado()
        self.m_dado02 = dado()

        self.j_ataque = self.j_dado01 + self.j_dado02 + self.jogador01.j_habilidade
        self.m_ataque = self.m_dado01 + self.m_dado02 + self.jogo.m_habilidade

        # Escrever primeiro dado do jogador
        self.lb_j_dado01 = Label(self.duelo,
                                 background="gold",
                                 text=f"{self.jogador01.j_nome}\n1º dado\n{self.j_dado01}")
        self.lb_j_dado01.place(relx=0.60,
                               rely=0.1,
                               relwidth=0.13,
                               relheight=0.22)

        # Escrever Segundo dado do jogador
        self.lb_j_dado02 = Label(self.duelo,
                                 background="gold",
                                 text=f"2º dado\n{self.j_dado02}")
        self.lb_j_dado02.place(relx=0.60,
                               rely=0.34,
                               relwidth=0.13,
                               relheight=0.14)

        # Escrever primeiro dado do Monstro
        self.lb_m_dado01 = Label(self.duelo,
                                 background="gold",
                                 text=f"{self.jogo.m_nome}\n 1º dado\n{self.m_dado01}")
        self.lb_m_dado01.place(relx=0.8,
                               rely=0.1,
                               relwidth=0.13,
                               relheight=0.22)

        # Escrever Segundo dado do Monstro
        self.lb_j_dado02 = Label(self.duelo,
                                 background="gold",
                                 text=f"2º dado\n{self.m_dado02}")
        self.lb_j_dado02.place(relx=0.8,
                               rely=0.34,
                               relwidth=0.13,
                               relheight=0.14)

        # Atualizar ataque do jogador
        self.lb_j_ataque = Label(self.duelo,
                                 text=f"Ataque do Jogador\n{self.j_ataque}",
                                 background="gold")
        self.lb_j_ataque.place(relx=0.47,
                               rely=0.50,
                               relwidth=0.25,
                               relheight=0.14)

        # Atualizar ataque do monstro
        self.lb_m_ataque = Label(self.duelo,
                                 text=f"Ataque do Monstro\n{self.m_ataque}",
                                 background="gold")
        self.lb_m_ataque.place(relx=0.74,
                               rely=0.50,
                               relwidth=0.25,
                               relheight=0.14)

        # Botão de testar a sorte
        self.bt_testar_sorte_luta = Button(self.duelo,
                                           text="Testar a Sorte",
                                           command=self.testar_sorte_luta)
        self.bt_testar_sorte_luta.place(relx=0.57, rely=0.8, relwidth=0.18, relheight=0.12)

        self.calcular_round()

    def calcular_round(self):
        print('Calculando round')
        if self.m_ataque == self.j_ataque:
            self.lb_b_resultado = Label(self.duelo,
                                        text=f"Round Empatado",
                                        background="gold")
            self.lb_b_resultado.place(relx=0.6,
                                      rely=0.64,
                                      relwidth=0.25,
                                      relheight=0.14)

            print("Round empatado")
        elif self.m_ataque < self.j_ataque:  # menor
            self.lb_b_resultado = Label(self.duelo,
                                        text=f"Vitória de {self.jogador01.j_nome}",
                                        background="gold")
            self.lb_b_resultado.place(relx=0.6,
                                      rely=0.64,
                                      relwidth=0.25,
                                      relheight=0.14)
            print("Vitoria do Jogador")
            self.jogo.m_energia = self.jogo.m_energia - 2
            self.vitoria = "jogador"
        elif self.m_ataque > self.j_ataque:  # maior
            self.lb_b_resultado = Label(self.duelo,
                                        text=f"Vitória de {self.jogo.m_nome}",
                                        background="gold")
            self.lb_b_resultado.place(relx=0.6,
                                      rely=0.64,
                                      relwidth=0.25,
                                      relheight=0.14)
            print("Vitoria do Monstro")
            self.jogador01.j_energia = self.jogador01.j_energia - 2
            self.vitoria = "monstro"

        # Energia do Monstro
        lb_batalha_m_energia = Label(self.duelo,
                                     text=f"Energia {self.jogo.m_energia}",
                                     background="gold")
        lb_batalha_m_energia.place(relx=0.30,
                                   rely=0.3,
                                   relwidth=0.2,
                                   relheight=0.08)

        # Energia do jogador
        lb_batalha_j_nome = Label(self.duelo,
                                  text=self.jogador01.j_energia,
                                  background="gold"
                                  )
        lb_batalha_j_nome.place(relx=0.30,
                                rely=0.05,
                                relwidth=0.04,
                                relheight=0.08)

        if self.jogo.m_energia < 1:
            print(f"{self.jogo.m_nome} morreu")
            messagebox.showinfo(title="Vitória",
                                message=f"Vitória de {self.jogador01.j_nome}!\n"
                                        f"{self.jogo.m_nome} Morreu",
                                )
            self.duelo.destroy()
            # self.bt_batalha.configure(state=DISABLED)

            if self.jogo.tem_trecho_a == True:
                self.rd_n_trecho_a["stat"] = NORMAL
                self.jogo.tem_trecho_a = False

            if self.jogo.tem_trecho_b == True:
                self.rd_n_trecho_b["stat"] = NORMAL
                self.jogo.tem_trecho_b = False

            if self.jogo.tem_trecho_c == True:
                self.rd_n_trecho_c["stat"] = NORMAL
                self.jogo.tem_trecho_c = False

            if self.jogo.tem_trecho_d == True:
                self.rd_n_trecho_d["stat"] = NORMAL
                self.validar_trecho_d = False

            if self.jogo.tem_trecho_e == True:
                self.rd_n_trecho_e["stat"] = NORMAL
                self.validar_trecho_e = False

            self.duelo.destroy()

        if self.jogador01.j_energia < 1:
            print(f"{self.jogador01.j_nome} morreu \n Tente de Novo")
            messagebox.showinfo(title="Game Over", message=f"{self.jogo.m_nome} Venceu!\n Tente Novamente!")
            self.j_status = "Morto"
            self.trecho.destroy()
            self.duelo.destroy()
            self.criar_personagem()
        self.sorte = False
        print("")

        return ()


Application()
