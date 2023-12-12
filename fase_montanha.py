class Fase:
    def __init__(self,
                 texto_trecho="Inicio",
                 n_trecho=1,
                 n_trecho_a=0,
                 n_trecho_b=0,
                 n_trecho_c=0,
                 n_trecho_d=0,
                 n_trecho_e=0,
                 texto_trecho_a="",
                 texto_trecho_b="",
                 texto_trecho_c="",
                 texto_trecho_d="",
                 texto_trecho_e="",
                 m_nome="",
                 m_energia=0,
                 m_habilidade=0,
                 tem_luta=False,
                 tem_trecho_a=False,
                 tem_trecho_b=False,
                 tem_trecho_c=False,
                 tem_trecho_d=False,
                 tem_trecho_e=False,
                 tem_item=False,
                 lista_item=[""],
                 item="",
                 tem_ouro=False,
                 ouro_fase=0,
                 contador=0):
        self.n_trecho = n_trecho
        self.texto_trecho = texto_trecho
        self.n_trecho_a = n_trecho_a
        self.n_trecho_b = n_trecho_b
        self.n_trecho_c = n_trecho_c
        self.n_trecho_d = n_trecho_d
        self.n_trecho_e = n_trecho_e
        self.texto_trecho_a = texto_trecho_a
        self.texto_trecho_b = texto_trecho_b
        self.texto_trecho_c = texto_trecho_c
        self.texto_trecho_d = texto_trecho_d
        self.texto_trecho_e = texto_trecho_e
        self.tem_trecho_a = tem_trecho_a
        self.tem_trecho_b = tem_trecho_b
        self.tem_trecho_c = tem_trecho_c
        self.tem_trecho_d = tem_trecho_d
        self.tem_trecho_e = tem_trecho_e
        self.m_nome = m_nome
        self.m_energia = m_energia
        self.m_habilidade = m_habilidade
        self.temluta = tem_luta
        self.tem_item = tem_item
        self.lista_item = lista_item
        self.item = item
        self.contador = contador
        self.tem_ouro = tem_ouro
        self.ouro_fase = ouro_fase

    def livro(self):
        if self.n_trecho == 1:
            self.texto_trecho = "Texto do Trecho 001\n" \
                                "Diante de ti ergue-se um colossal portão de ferro. \n" \
                                "Ao examinar a fechadura, percebes sua complexidade. \n" \
                                "O portão, adornado com pontas afiadas, desafia-te a \n" \
                                "superá-lo com opções igualmente desafiadoras."
            self.n_trecho_a = 3
            self.n_trecho_b = 2
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Arrombar o portão - avance para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Saltar o muro - prosseguir para {self.n_trecho_b}?"

        elif self.n_trecho == 2:
            self.texto_trecho = "Texto do trecho 002\n" \
                                "Escalar o portão revelou-se uma tarefa menos árdua do \n" \
                                "que imaginavas, mas as lanças posicionadas sobre ele \n" \
                                "são ameaçadoras.\n" \
                                "Ao atingir o topo, um sobressalto toma conta de \n" \
                                "ti ao deparar com uma colossal fera voadora, suas asas \n" \
                                "imponentes e garras capazes de triturar ferro.\n" \
                                "\n" \
                                "A fera começa a circundar-te, preparada para o ataque."
            self.n_trecho_a = 4
            self.n_trecho_b = 5
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Saltar nas costas da fera voadora. Vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Jogar-se ao chão para se ocultar. Vá para {self.n_trecho_b}?"

        elif self.n_trecho == 3:
            self.texto_trecho = "Texto do trecho 003\n" \
                                "Com determinação, retiras um kit de arrombamento \n" \
                                "e inicia o trabalho na fechadura."
            self.n_trecho_a = 9
            self.n_trecho_b = 3.1
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Se tiver sucesso vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Se falhar vá para {self.n_trecho_b}?"

        elif self.n_trecho == 3.1:
            self.texto_trecho = "Texto do trecho 003.1\n" \
                                "Ao atravessar o portão, este produz um estrondo mais \n" \
                                "alto do que antecipavas. \n" \
                                "O barulho atrai a atenção de outra fera voadora que \n" \
                                "agora circula sobre ti.\n" \
                                "Tentas esconder-te.\n" \
                                "\n" \
                                "Teste de sorte:"
            self.n_trecho_a = 11
            self.n_trecho_b = 10
            self.tem_ouro = True
            self.ouro_fase = 100
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Se tiver sucesso vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Se falhar vá para {self.n_trecho_b}?"

        elif self.n_trecho == 4:
            self.texto_trecho = "Texto do trecho 004\n" \
                                "Ao vislumbrar uma oportunidade, tentas saltar nas \n" \
                                "costas da fera para dominá-la. No entanto, em um \n" \
                                "movimento ágil, a fera acerta-te com a cauda,\n" \
                                "projetando-te de volta ao portão, onde as lanças \n" \
                                "perfuram tuas costas, levando-te à morte.\n" \
                                "É o fim da tua jornada."
            '''
            self.n_trecho_a = 7 
            self.n_trecho_b = 8
            self.tem_ouro = True
            self.ouro_fase = 100
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"
            '''

        elif self.n_trecho == 5:
            self.texto_trecho = "Texto do trecho 005\n" \
                                "Enquanto a fera circula, desapareces de sua vista, \n" \
                                "saltando uma, duas vezes, até alcançar o solo. \n" \
                                "\n" \
                                "Antes que ela te localize você pode:\n"
            self.n_trecho_a = 6
            self.n_trecho_b = 8
            self.n_trecho_c = 10
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.texto_trecho_a = f"Fugir - avance para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Esconder-se - prosseguir para {self.n_trecho_b}?"
            self.texto_trecho_c = f"Lutar - Vá para {self.n_trecho_c}?"

        elif self.n_trecho == 6:
            self.texto_trecho = "Saltas para a sombra, tentando permanecer\n" \
                                " oculto para evitar um destino sombrio." \
                                "\n" \
                                "Teste a sorte"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 7
            self.n_trecho_b = 8
            self.texto_trecho_a = f"Se tiver sucesso vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Se falhar vá para {self.n_trecho_b}?"

        elif self.n_trecho == 7:
            self.texto_trecho = "Texto do trecho 007\n" \
                                "Tua velocidade não é suficiente, e um \n" \
                                "mergulho da fera arranca tua cabeça com \n" \
                                "um único golpe de suas garras afiadas."
            '''
            #self.tem_item = True
            #self.item = "Espada"
            '''
            self.n_trecho_a = 8
            self.n_trecho_b = 4
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"

        elif self.n_trecho == 8:
            self.texto_trecho = "Texto do trecho 008\n" \
                                "Consegues esgueirar-te pela sombra, \n" \
                                "mas isso não é sem consequências. \n" \
                                "\n" \
                                "Recebes a marca do covarde.\n" \
                                "Tua fuga não passará impune."
            self.n_trecho_a = 5
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Vá para {self.n_trecho_a}?"

        elif self.n_trecho == 9:
            self.texto_trecho = "Texto do trecho 009\n" \
                                "A fera não te localiza, e após alguns instantes, \n" \
                                "ela pousa à tua frente, a apenas dois passos de \n" \
                                "um ataque furtivo que pode ser fatal para ela.\n" \
                                "Tentas atacá-la.\n" \
                                "Teste de sorte:"
            self.n_trecho_a = 10
            self.n_trecho_b = 11
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Falha - Vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Sucesso - Vá para {self.n_trecho_b}?"

        elif self.n_trecho == 10:
            self.texto_trecho = "Texto do trecho 010\n" \
                                "É hora de enfrentar a fera voadora.\n" \
                                "Fera Voadora\n" \
                                "Habilidade 10\n" \
                                "Energia 8\n"
            self.temluta = True
            self.m_nome = "Fera Voadora"
            self.m_energia = 10
            self.m_habilidade = 8
            self.n_trecho_a = 4
            self.n_trecho_b = 6
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"

        elif self.n_trecho == 11:
            self.texto_trecho = "Texto do Trecho 011\n" \
                                "Teu golpe certeiro perfura o \n" \
                                "coração da Besta Voadora, \n" \
                                "e ela cai morta à tua frente.\n" \
                                "Agora mais calmo, percebes uma \n" \
                                "porta pesada de madeira onde \n" \
                                "antes estavas escondido.\n" \
                                "Tentas abri-la.\n" \
                                "\n" \
                                "Teste de sorte:"
            self.n_trecho_a = 12
            self.n_trecho_b = 15.1
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Se tiver sucesso vá para  {self.n_trecho_a}?"
            self.texto_trecho_b = f"Se falhar, vá para {self.n_trecho_b}?"

        elif self.n_trecho == 12:
            self.texto_trecho = "Texto do Trecho 012\n" \
                                "Consegues abrir a porta, mas não há nada dentro. \n" \
                                "Ao tentar sair, és interceptado por um \n" \
                                "demônio de aparência necróptica. \n" \
                                "Não existe escolha além de lutar.\n"
            self.n_trecho_a = 14
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Lute contra o Demonio - avance para {self.n_trecho_a}?"

        elif self.n_trecho == 13:
            self.texto_trecho = "Texto do Trecho 0013\n" \
                                "Morte pela Besta Voadora."

        elif self.n_trecho == 14:
            self.texto_trecho = "Texto do Trecho 001\n" \
                                "Luta contra o Demônio das Sombras\n" \
                                "Demônio das Sombras\n" \
                                "Habilidade 12\n" \
                                "Energia 6\n" \
                                "\n" \
                                "Se morreres, é o fim da tua aventura."
            self.n_trecho_a = 16
            self.temluta = True
            self.m_nome = "Demonio das Sombras"
            self.m_habilidade = 12
            self.m_energia = 6
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Vitória na Luta. Vá para {self.n_trecho_a}?"

        elif self.n_trecho == 15:
            self.texto_trecho = "Texto do Trecho 001\n" \
                                "A Morte pelo Demônio."

        elif self.n_trecho == 15.1:
            self.texto_trecho = "Texto do Trecho 015.1\n" \
                                "Sem perceber, pisas numa alavanca que \n" \
                                "aciona uma armadilha mortal. Estacas \n" \
                                "surgem das paredes, perfurando teu \n" \
                                "corpo por completo.\n" \
                                "\n" \
                                "É o fim da tua aventura.\n"

        elif self.n_trecho == 16:
            self.texto_trecho = "Texto do Trecho 001\n" \
                                "Percebes uma pequena bolsa de couro preto " \
                                "presa à cintura do demônio." \
                                "Ao abri-la, encontra uma pequena " \
                                "chave de cobre."
            self.n_trecho_a = 16
            self.tem_item = True
            self.item = "Chave de Cobre"
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Arrombar o portão - avance para {self.n_trecho_a}?"

        elif self.n_trecho == 17:
            self.texto_trecho = "Texto do Trecho 001\n" \
                                "Finalmente, alcanças a porta do castelo. \n" \
                                "A verdadeira aventura inicia-se agora."
            self.n_trecho_a = 18
            self.tem_trecho_a = True
            self.texto_trecho_a = f"avance para {self.n_trecho_a}?"

        elif self.n_trecho == 18:
            self.texto_trecho = "Texto do Trecho 001\n" \
                                "Adquira o jogo completo e continue a tua jornada!"
