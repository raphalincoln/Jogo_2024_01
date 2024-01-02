
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
                 contador=0,
                 livro_titulo="",
                 tem_testar_sorte=False):
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
        self.livro_titulo = livro_titulo
        self.tem_testar_sorte = tem_testar_sorte
        self.livro_titulo = "O Feiticeiro da Montanha \n" \
                            "de Fogo!"

    def livro(self):
        if self.n_trecho == 1:
            self.texto_trecho = ("Texto do trecho 001\n"
                                 "Finalmente a sua caminhada de dois dias chegou ao \n"
                                 "fim. Você desembainha a sua espada, coloca-a no chão\n "
                                 "e suspira aliviado, enquanto se abaixa para se sentar \n"
                                 "nas pedras cheias de musgo para um momento de descanso.\n "
                                 "Você se espreguiça, esfrega os olhos e, afinal, olha \n"
                                 "para a Montanha do Cume de Fogo. A própria montanha em si\n"
                                 "já tem um ar ameaçador. Algum animal gigantesco parece ter\n "
                                 "deixado as marcas de suas garras na encosta íngreme diante\n"
                                 "de você. Penhascos rochosos e pontudos se projetam, formando\n"
                                 "ângulos estranhos. No cume você já pode vislumbrar a \n"
                                 "sinistra coloração vermelha - provavelmente alguma \n"
                                 "vegetação misteriosa - que deu nome à montanha. Talvez\n "
                                 "ninguém jamais chegue a saber o que cresce lá em cima, uma\n"
                                 "vez que escalar o pico deve ser com certeza impossível.\n"
                                 "Sua busca está para começar. Do outro lado da clareira\n "
                                 "há uma escura entrada de caverna. Você pega sua espada,\n "
                                 "levanta-se e considera que perigos podem estar à sua frente.\n"
                                 " Mas, com determinação, você recoloca a sua espada na \n"
                                 "bainha e se aproxima da caverna.Você dá uma primeira "
                                 "olhada na penumbra e vê-paredes escuras e úmidas com \n"
                                 "poças de água no chão de pedra à sua frente. O ar é frio\n"
                                 " e úmido. Você acende a sua lanterna e avança cautelosamente\n"
                                 "pela escuridão. Teias de aranha tocam seu rosto e você ouve\n"
                                 " a movimentação de pés minúsculos: muito provavelmente,"
                                 " ratazanas. Você adentra a caverna. Depois de uns poucos\n"
                                 "metros, chega logo a uma encruzilhada.")
            self.n_trecho_a = 71
            self.n_trecho_b = 278
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Você vai virar para o oeste {self.n_trecho_a}?"
            self.texto_trecho_b = f"ou para o leste {self.n_trecho_b}?"

        elif self.n_trecho == 2:
            self.texto_trecho = "Teste a sua Sorte. Se você tiver sorte, \n" \
                                "escapa sem atrair a atenção do Ogro. \n" \
                                "Se você não tiver sorte, chuta acidentalmente \n" \
                                "uma pequena pedra que sai quicando pelo \n" \
                                "chão da caverna, o que faz você rogar \n" \
                                "uma praga. Você puxa a espada para o caso \n" \
                                "do Ogro ter ouvido o barulho - vá para 16. \n" \
                                "Se você tiver tido sorte, retorna \n" \
                                "silenciosamente pelo corredor até a \n" \
                                "encruzilhada. Vá para 269."
            self.n_trecho_a = 16
            self.n_trecho_b = 269
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_testar_sorte = True
            self.texto_trecho_a = f"o Ogro te ouviu, vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Voce não foi ouvido, retorne para  {self.n_trecho_b}?"

        elif self.n_trecho == 3:
            self.texto_trecho = "O sino solta um som abafado e, passados \n" \
                                "alguns minutos, você vê um velho encarquilhado\n" \
                                " entrar em um pequeno bote a remo atracado na \n" \
                                "margem oposta. Ele rema lentamente até a sua margem,\n" \
                                " atraca o barco e vem mancando até você. Ele pede\n" \
                                " três Peças de Ouro. Quando você protesta por causa \n" \
                                "do preço, ele resmunga alguma desculpa esfarrapada \n" \
                                "sobre a “inflação.” Ele começa a ficar zangado com \n" \
                                "as suas reclamações. Você paga as três Peças de Ouro \n" \
                                "(vá para 272) ou o ameaça (vá para 127)?"
            self.n_trecho_a = 272
            self.n_trecho_b = 127
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Pagar as peças de ouro vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Ameaça-lo, vá para {self.n_trecho_a}?"

        elif self.n_trecho == 4:
            self.texto_trecho = "Você se encontra em um corredor que vai do norte\n" \
                                " para o sul. Para o norte, a passagem vira para \n" \
                                "leste alguns metros à frente. Se quiser investigar\n" \
                                ", vá para 46. Para o sul, a passagem também vira \n" \
                                "para o leste. Vá para 332, se quiser ir para o sul.\n "
            self.n_trecho_a = 46
            self.n_trecho_b = 332
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"

        elif self.n_trecho == 5:
            self.texto_trecho = "Há uma porta de madeira rústica na parede \n" \
                                "leste da passagem. Você coloca o ouvido colado\n" \
                                "na porta e percebe uma espécie de cantilena \n" \
                                "alegre em surdina. Você quer bater na porta e \n" \
                                "entrar (vá para 97) ou continuar para o \n" \
                                "norte (vá para 292)?"
            self.n_trecho_a = 97
            self.n_trecho_b = 292
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Bater na porta, vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Seguir para Norte, vá para {self.n_trecho_b}?"

        elif self.n_trecho == 6:
            self.texto_trecho = "A grande porta maciça não possui maçaneta.\n" \
                                "Você tenta arrombá-la, mas não adianta. \n" \
                                "A porta nem se mexe. Você resolve desistir e\n" \
                                "passar pela abertura no caminho leste-oeste, \n" \
                                "retornando um pouco. Vá para 89."
            self.tem_trecho_a = True
            self.n_trecho_a = 7
            self.texto_trecho_a = f"Seguir para Leste-Oeste - {self.n_trecho_a}?"

        elif self.n_trecho == 7:
            self.texto_trecho = "Você está na margem norte de um \n" \
                                "rio de correnteza rápida que corre\n" \
                                " em uma grande caverna subterrânea.\n" \
                                " Vá para 214."
            self.n_trecho_a = 214
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"

        elif self.n_trecho == 8:
            self.texto_trecho = "A passagem à sua frente termina em \n" \
                                "uma porta sólida. Você tenta escutar algo\n" \
                                " mas não ouve nada. Você experimenta a \n" \
                                "maçaneta, ela gira e você entra no aposento.\n" \
                                " Você olha em volta e, de repente, ouve um \n" \
                                "grito de guerra atrás de você: ao se virar, \n" \
                                "vê um homem selvagem que salta sobre você, \n" \
                                "brandindo uma grande arma. Trata-se de um \n" \
                                "BÁRBARO louco e você terá que lutar contra ele!"
            self.temluta = True
            self.m_nome = "Bárbaro"
            self.m_habilidade = 7
            self.m_energia = 6
            self.n_trecho_a = 273
            self.n_trecho_b = 189
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Se Vencer. vá para {self.n_trecho_a}?"
            self.texto_trecho_a = f"Se optar por fugir. vá para {self.n_trecho_b}?"

        elif self.n_trecho == 9:
            self.texto_trecho = "Surpreso com o sucesso de seu próprio blefe,\n" \
                                "você resolve apelar um pouco mais para a \n" \
                                "sua sorte. Você pode examinar as ferramentas\n" \
                                "dos Esqueletos ou fingir que está procurando\n" \
                                "por papéis de trabalho e vasculharas gavetas\n" \
                                "dos vários bancos. Se você escolher as \n" \
                                "ferramentas, vá para 34. Se você revistar as\n" \
                                "gavetas, vá para 322. Você ouve um ruído que\n" \
                                "vem do outro lado da porta norte e compreende \n" \
                                "que precisa se apressar em sair dali."
            self.n_trecho_a = 34
            self.n_trecho_b = 322
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f" Feramentas, vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Gavetas, vá para{self.n_trecho_b}?"

        elif self.n_trecho == 10:
            self.texto_trecho = "Você chega de volta à encruzilhada\n" \
                                "e toma o caminho do norte. \n" \
                                "Vá para 77. \n"
            self.n_trecho_a = 77
            self.tem_trecho_a = True
            self.texto_trecho_a = f"seguir para o norte - {self.n_trecho_a}?"

        elif self.n_trecho == 11:
            self.texto_trecho = "Você segue a passagem na direção oeste\n " \
                                "até que ela vira, contornando uma curva, \n" \
                                "para o sul. Pouco antes da curva há um aviso\n" \
                                " que diz “Em Construção”. À sua frente começa\n" \
                                " uma escada que desce. Somente três degraus \n" \
                                "foram construídos até agora. Diversas pás,\n" \
                                " picaretas e outras ferramentas estavam \n" \
                                "espalhadas pelo chão junto aos degraus mas, \n" \
                                "quando você virou a curva, elas subitamente \n" \
                                "entraram em atividade sozinhas e começaram a \n" \
                                "trabalhar nos degraus. Você está agora assistindo\n" \
                                " às várias ferramentas cavando e martelando, \n" \
                                "como se fossem manuseadas por trabalhadores invisíveis. \n" \
                                "Uma cantoria em surdina vai se tornando cada vez mais alta e \n" \
                                "você identifica as palavras: “Rá-rá, Rá-rá, Lá vamos\n" \
                                "nós trabalhar...” Enquanto você fica assistindo, começa \n" \
                                "a rir - a cena é bem divertida. Você senta e fica assistindo, \n" \
                                "conseguindo até mesmo bater um papo com algumas das ferramentas \n" \
                                "mágicas. Ganhe 2 pontos de ENERGIA e 1 ponto de HABILIDADE \n" \
                                "enquanto relaxa. Depois retorne pela passagem até a \n" \
                                "encruzilhada, por onde você pode ir para o norte \n" \
                                "(vá para 366) ou para o sul (vá para 250)."
            self.n_trecho_a = 366
            self.n_trecho_b = 250
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Seguir para o Norte -   {self.n_trecho_a}?"
            self.texto_trecho_b = f"Seguir para o Sul, vá para {self.n_trecho_b}?"

        elif self.n_trecho == 12:
            self.texto_trecho = "Quando você puxa a alavanca, um barulho \n" \
                                "ensurdecedor de campainha ecoa pelas passagens. \n" \
                                "Você desesperadamente empurra a alavanca de volta para \n" \
                                "parar o alarme, mas ela já teve o seu efeito. Você \n" \
                                "ouve passos que se aproximam pelo corredor. \n" \
                                "Vá para 161 para descobrir o que você atraiu. \n" \
                                ""
            self.n_trecho_a = 161
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Descobrir o que atraiu, vá para {self.n_trecho_a}?"

        elif self.n_trecho == 13:
            self.texto_trecho = "Sua cabeça dói e você se sente tonto ao se levantar. \n" \
                                "Os quatro homens começam a se movimentar e caminham \n" \
                                "em sua direção com suas armas apontadas. Você tateia \n" \
                                "pelo caminho junto à parede para chegar à porta sul, \n" \
                                "mas parece pouco provável que você vá conseguir. \n" \
                                "Seu pé escorrega em uma pedra solta e você cai no chão. \n" \
                                "Antes que você consiga se levantar, os seres já estão \n" \
                                "em cima de você. Vá para 282.\n"
            self.n_trecho_a = 282
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Seguir para {self.n_trecho_a}?"

        elif self.n_trecho == 14:
            self.texto_trecho = "Não há sinais de quaisquer passagens \n" \
                                "secretas, mas você subitamente ouve passos \n" \
                                "que vêm na sua direção. Para descobrir o que \n" \
                                "está se aproximando, vá para 161. Você terá que\n" \
                                "lutar contra mais esta criatura. Se você derrotar\n" \
                                " o monstro, vá para 117. Anote esta referência \n" \
                                "para que você saiba para onde retornar."
            self.n_trecho_a = 161
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"

        elif self.n_trecho == 15:
            self.texto_trecho = "Enquanto você está sentado no banco comendo a sua\n " \
                                "refeição, começa a se sentir profundamente relaxado, \n" \
                                "e as dores de seu corpo parecem estar desaparecendo \n" \
                                "aos poucos. Este lugar de descanso é encantado. Você pode\n" \
                                "recuperar 2 pontos adicionais de ENERGIA, como também até \n" \
                                "a quantidade normal (mas somente se isso não ultrapassar seu \n" \
                                "índice Inicial de ENERGIA), e recuperar 1 ponto de HABILIDADE, \n" \
                                "se algum já tiver sido perdido. Quando estiver pronto para\n" \
                                "continuar, siga pela passagem e vá para 367."
            self.n_trecho_a = 367
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Seguir para {self.n_trecho_a}?"

        elif self.n_trecho == 16:
            self.texto_trecho = "Você desembainha a sua espada\n" \
                                "e, ao fazê-lo, o Ogro o Ouve\n" \
                                "e se prepara para atacar:\n"
            self.n_trecho_a = 50
            self.n_trecho_b = 269
            self.temluta = True
            self.m_nome = "Ogro"
            self.m_habilidade = 8
            self.m_energia = 10
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Vencer o Ogro - Vá para {self.n_trecho_a}?"
            self.texto_trecho_a = f"Fugir - Avance para {self.n_trecho_a}?"

        elif self.n_trecho == 17:
            self.texto_trecho = "Usando a estaca de madeira e a marreta\n" \
                                "(ou uma marreta improvisada, se não estiver\n" \
                                "levando uma), você forma uma cruz e avança\n" \
                                "na direção do Vampiro, encurralando-o em um\n" \
                                "canto. Ele geme e tenta alcançá-lo, mas não pode\n" \
                                "se aproximar. Porém não vai ser fácil cravar a\n" \
                                "estaca em seu coração. Ao avançar, você tropeça e \n" \
                                "cai para a frente. Por obra e graça da sorte, a estaca\n" \
                                "voa.e atinge a criatura que solta um grito. \n" \
                                "Teste a sua Sorte. \n" \
                                "Se você tiver sorte, a estaca penetra no coração do Vampiro.\n" \
                                "Se você não tiver sorte, o Vampiro sofre apenas um \n" \
                                "ferimento leve (deduza 3 pontos de sua ENERGIA) e \n" \
                                "atira você para o outro lado do aposento, na direção \n" \
                                "da porta oeste. Para Fugir por ela, vá para 380. \n" \
                                "Para continuar lutando, vá para 144. Se você teve sorte e \n" \
                                "matou o Vampiro, pode procurar o tesouro dele – \n" \
                                "vá para 327"
            self.n_trecho_a = 327  # Sorte
            self.n_trecho_b = 144  # azar
            self.n_trecho_c = 380  # Fugir
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_testar_sorte = True
            self.texto_trecho_a = f"Sorte - Matou o Vampiro - Vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Azar - Feriu o vampiro e vai lutar - {self.n_trecho_b}?"
            self.texto_trecho_c = f"Azar - Fugir {self.n_trecho_c}?"

        elif self.n_trecho == 18:
            self.texto_trecho = "Você anda para o oeste pela passagem. \n" \
                                "Após uns 50 metros mais ou menos, o caminho\n" \
                                "vira para o norte. Depois de andar dois ou\n" \
                                "três passos nesta direção, você ouve um ruído\n" \
                                "de desmoronamento embaixo de seus pés e tenta \n" \
                                "recuar, enquanto o chão desaba. Teste a sua Sorte. \n" \
                                "Se você tiver sorte, consegue pular rapidamente \n" \
                                "para trás antes que se abra um poço. Se você não tiver\n" \
                                "sorte é porque foi lento demais e acaba caindo mais\n" \
                                "de dois metros abaixo em um poço – perde um ponto de\n" \
                                "ENERGIA. Se você teve sorte, é melhor voltar para\n" \
                                "a encruzilhada (vá para 261). Se você não teve sorte, \n" \
                                "vá para 348."
            self.n_trecho_a = 261  # Sorte
            self.n_trecho_b = 348  # azar
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_testar_sorte = True
            self.texto_trecho_a = f"Sorte - Retornou para encruzilhada -  {self.n_trecho_a}?"
            self.texto_trecho_b = f"Azar - Caiu e vai para  {self.n_trecho_b}?"

        elif self.n_trecho == 19:
            self.texto_trecho = "Estes dois seres cruéis são Goblins. \n" \
                                "Eles atacarão você, um de cada vez."
            self.n_trecho_a = 317
            self.temluta = True
            self.m_nome = "Goblin 1"
            self.m_habilidade = 5
            self.m_energia = 5
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Se vencer, vá para {self.n_trecho_a}?"

        elif self.n_trecho == 20:
            self.texto_trecho = "O confronto começa. Você tem sua espada, \n" \
                                "eles têm suas armas. Eles atacam você, \n" \
                                "um de cada vez:\n"
            self.n_trecho_a = 376
            self.n_trecho_b = 291
            self.temluta = True
            self.m_nome = "Anão 1"
            self.m_habilidade = 7
            self.m_energia = 4
            self.tem_trecho_a = True
            self.tem_trecho_b = True

            self.texto_trecho_a = f"Se Vencer, vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Se fugir, vá para {self.n_trecho_b}?"

        elif self.n_trecho == 21:
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho = "O sangue verde dos Orças mortos cheira mal, " \
                                "escorrendo lentamente de seus corpos. Você \n" \
                                "contorna os cadáveres e examina a arca. \n" \
                                "É um objetivo sólido, feito de carvalho rijo \n" \
                                "\ne ferro, e está trancada firmemente. Você pode \n" \
                                "tentar arrebentar a fechadura com sua espada \n" \
                                " ou deixá-la de lado e sair pela \n" \
                                "porta aberta."
            self.n_trecho_a = 339
            self.n_trecho_b = 293
            self.texto_trecho_a = f"Bater com a Espada, vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f"Deixar de lado, vá para {self.n_trecho_b}?"

        elif self.n_trecho == 22:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 293
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 23:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 326
            self.n_trecho_b = 229
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 24:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 369
            self.n_trecho_b = 135
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 25:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 90
            self.n_trecho_b = 340
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 26:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 371
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 27:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 319
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 28:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 351
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 29:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 375
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 30:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 67
            self.n_trecho_b = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 31:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 90
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 32:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 124
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 33:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.temluta = True
            self.m_nome = "Orca"
            self.m_habilidade = 6
            self.m_energia = 4
            self.n_trecho_a = 320
            self.n_trecho_b = 147
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 34:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 96
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 35:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 136
            self.n_trecho_b = 361
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 36:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 263
            self.n_trecho_b = 353
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 37:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 366
            self.n_trecho_b = 11
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 38:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 66
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 39:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 396
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 40:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 355
            self.n_trecho_b = 265
            self.n_trecho_b = 181
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 41:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Monstro"
            self.m_habilidade = 9
            self.m_energia = 6
            self.tem_trecho_a = True
            self.n_trecho_a = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 42:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 257
            self.n_trecho_b = 113
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 43:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 354
            self.n_trecho_b = 52
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 44:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 399
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 45:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 90
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 46:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 4
            self.n_trecho_b = 206
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 47:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 158
            self.n_trecho_b = 298
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 48:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 391
            self.n_trecho_b = 60
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 49:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 122
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 50:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 269
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 51:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 287
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 52:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.tem_trecho_e = True
            self.n_trecho_a = 391
            self.n_trecho_b = 362
            self.n_trecho_c = 354
            self.n_trecho_d = 234
            self.n_trecho_e = 291
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_a = f" vá para {self.n_trecho_c}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_d}?"
            self.texto_trecho_a = f" vá para {self.n_trecho_e}?"

        elif self.n_trecho == 53:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 155
            self.n_trecho_b = 300
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 54:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 308
            self.n_trecho_b = 179
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 55:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 7
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 56:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 399
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 57:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 16
            self.n_trecho_b = 2
            self.n_trecho_c = 119
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 58:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 15
            self.n_trecho_b = 367
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 59:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 150
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 60:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 48
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 61:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.temluta = True
            self.m_nome = "Aranha Gigante"
            self.m_habilidade = 7
            self.m_energia = 8
            self.n_trecho_a = 29
            self.n_trecho_b = 375
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 62:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 6
            self.n_trecho_b = 89
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 63:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 281
            self.n_trecho_b = 10
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 64:
            self.texto_trecho = "Morte"

        elif self.n_trecho == 65:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 293
            self.n_trecho_b = 372
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 66:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 104
            self.n_trecho_b = 99
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 67:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 267
            self.n_trecho_b = 177
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 68:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 303
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 69:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 244
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 70:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 71:
            self.texto_trecho = "Há uma curva na passagem para a \n" \
                                "direita, levando para o norte. \n" \
                                "Cautelosamente, você se aproxima de \n" \
                                "um posto de sentinela em um canto e,\n" \
                                "ao olhar para dentro, vê um ser estranho,\n" \
                                "parecido com um Goblin, vestido de \n" \
                                "armadura de couro e adormecido em seu \n" \
                                "posto. Você tenta passar por ele na \n" \
                                "ponta dos pés. Teste a sua Sorte. \n" \
                                "Se você tiver sorte, ele não acorda e \n" \
                                "continua a roncar alto – vá para 248. \n" \
                                "Se você não tiver sorte, você pisa em\n " \
                                "terreno mole e faz um barulho, e os olhos \n" \
                                "do ser se abrem instantaneamente – \n" \
                                "vá para 301."
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 301
            self.n_trecho_b = 248
            self.texto_trecho_a = f" vá para (Falha) {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para (Sucesso) {self.n_trecho_b}?"

        elif self.n_trecho == 72:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 319
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 73:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 218
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 74:
            self.texto_trecho = ""
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 118
            self.n_trecho_b = 279
            self.texto_trecho_a = f" vá para (Falha) {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para (Sucesso) {self.n_trecho_b}?"

        elif self.n_trecho == 75:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 93
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 76:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 244
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 77:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 345
            self.n_trecho_b = 18
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 78:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 159
            self.n_trecho_b = 237
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 79:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 137
            self.n_trecho_b = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 80:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 129
            self.n_trecho_b = 123
            self.n_trecho_b = 195
            self.n_trecho_c = 140
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_a = f" vá para {self.n_trecho_c}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_d}?"

        elif self.n_trecho == 81:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 205
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 82:
            self.texto_trecho = ""
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 208
            self.n_trecho_b = 147
            self.n_trecho_c = 33
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 83:
            self.texto_trecho = ""
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 154
            self.n_trecho_b = 360
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 84:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 204
            self.n_trecho_b = 280
            self.n_trecho_c = 377
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 85:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 106
            self.n_trecho_b = 373
            self.n_trecho_c = 318
            self.n_trecho_d = 59
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_a = f" vá para {self.n_trecho_c}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_d}?"

        elif self.n_trecho == 86:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.temluta = True
            self.m_nome = "Crocodilo"
            self.m_habilidade = 7
            self.m_energia = 6
            self.n_trecho_a = 259
            self.n_trecho_b = 350
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 87:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 262
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 88:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 216
            self.n_trecho_b = 384
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 89:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 286
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 90:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 253
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 91:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_testar_sorte = True
            self.n_trecho_a = 20
            self.n_trecho_b = 131
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para (Sucesso) {self.n_trecho_b}?"

        elif self.n_trecho == 92:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 71
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 93:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 8
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 94:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 260
            self.n_trecho_b = 329
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 95:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 205
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 96:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 374
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 97:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 334
            self.n_trecho_b = 247
            self.n_trecho_c = 292
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 98:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 358
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 99:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 383
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 100:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 346
            self.n_trecho_b = 91
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 101:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 327
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 102:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 303
            self.n_trecho_b = 19
            self.n_trecho_c = 68
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 103:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 252
            self.n_trecho_b = 359
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 104:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 49
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 105:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.tem_trecho_e = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.n_trecho_c = 1
            self.n_trecho_d = 1
            self.n_trecho_e = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_d = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_e = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 106:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 152
            self.n_trecho_b = 126
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 107:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 148
            self.n_trecho_b = 197
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 108:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Mão"
            self.m_habilidade = 6
            self.m_energia = 4
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 185
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 109:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 120
            self.n_trecho_b = 212
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 110:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 319
            self.tem_ouro = True
            self.ouro_fase = 10
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 111:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 249
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 112:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 142
            self.n_trecho_b = 105
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 113:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 285
            self.n_trecho_b = 78
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 114:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 359
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 115:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 95
            self.n_trecho_b = 313
            self.n_trecho_c = 330
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 116:
            self.texto_trecho = ""
            self.m_nome = "Orca"
            self.m_energia = 4
            self.m_habilidade = 5
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 378
            self.n_trecho_b = 42
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 117:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 354
            self.n_trecho_b = 308
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 118:
            self.texto_trecho = "Quando você se aproxima, ele se levanta\n" \
                                " de seu caixão, abre sua capa e envolve\n" \
                                " você com ela. Sua última lembrança desta\n" \
                                " vida é uma pontada de dor quando os\n" \
                                " dentes afiados do monstro se cravam\n" \
                                " no seu pescoço. Você jamais deveria ter\n" \
                                " se permitido olhar nos olhos de um VAMPIRO!"

        elif self.n_trecho == 119:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 269
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 120:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 197
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 121:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 103
            self.n_trecho_b = 359
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 122:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 268
            self.n_trecho_b = 282
            self.n_trecho_c = 13
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_b}?"


        elif self.n_trecho == 123:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 184
            self.n_trecho_b = 164
            self.n_trecho_c = 140
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 124:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 138
            self.n_trecho_b = 76
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 125:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 73
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 126:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 152
            self.n_trecho_b = 26
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 127:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 272
            self.n_trecho_b = 188
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 128:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 210
            self.n_trecho_b = 58
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 129:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 104
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 130:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 280
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 131:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 291
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 132:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 319
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 133:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 52
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 134:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 202
            self.n_trecho_b = 325
            self.n_trecho_c = 87
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"


        elif self.n_trecho == 135:
            self.texto_trecho = ""
            self.tem_ouro = True
            self.ouro_fase = 18
            self.tem_trecho_a = True
            self.n_trecho_a = 360
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 136:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 229
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 137:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 354
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 138:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 163
            self.n_trecho_b = 351
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 139:
            self.texto_trecho = "Durante a sua aventura, você deverá ter \n " \
                                "encontrado diversas chaves e provavelmente\n" \
                                " terá recolhido algumas delas. Você pode \n" \
                                "agora usar três destas chaves para tentar \n" \
                                "abrir as fechaduras da arca.\n" \
                                "Cada chave está identificada por um número.\n" \
                                " Para determinar se você tem as chaves \n" \
                                "certas, some seus três números. Agora vá \n" \
                                "até a seção que possui o mesmo número que \n" \
                                "este total, onde você descobrirá se usou \n" \
                                "as chaves corretas.\n"\
                                "Se você não tiver três chaves numeradas, \n" \
                                "então chegou ao fim de sua jornada. Você \n" \
                                "senta na arca e chora ao tomar consciência \n" \
                                "de que terá que explorar a montanha mais\n" \
                                " uma vez a fim de encontrar as tais chaves.\n"
            self.tem_trecho_a = True
            self.n_trecho_a = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 140:
            self.texto_trecho = ""
            self.m_nome = "Esqueleto"
            self.m_habilidade = 7
            self.m_energia = 5
            self.tem_trecho_a = True
            self.n_trecho_a = 395
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 141:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 66
            self.n_trecho_b = 111
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 142:
            self.texto_trecho = ""
            self.m_nome = "Esqueleto"
            self.m_habilidade = 7
            self.m_energia = 5
            self.tem_trecho_a = True
            self.n_trecho_a = 396
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"


        elif self.n_trecho == 143:
            self.texto_trecho = ""
            self.m_nome = "Verme de Areia"
            self.m_habilidade = 7
            self.m_energia = 7
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 44
            self.n_trecho_b = 399
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 144:
            self.texto_trecho = ""
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 217
            self.n_trecho_b = 101
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 145:
            self.texto_trecho = ""
            self.tem_item = True
            self.item = "Chave 99"
            self.tem_trecho_a = True
            self.n_trecho_a = 363
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 146:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 366
            self.n_trecho_b = 11
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 147:
            self.texto_trecho = ""
            self.tem_ouro = True
            self.ouro_fase = 1
            self.tem_trecho_a = True
            self.n_trecho_a = 208
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 148:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 230
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 149:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 181
            self.n_trecho_b = 265
            self.n_trecho_c = 355
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"


        elif self.n_trecho == 150:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 222
            self.n_trecho_b = 297
            self.n_trecho_c = 133
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 151:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 218
            self.n_trecho_b = 86
            self.n_trecho_c = 158
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 152:
            self.texto_trecho = ""
            self.m_nome = "Dragão"
            self.m_habilidade = 10
            self.m_energia = 12
            self.tem_trecho_a = True
            self.n_trecho_a = 371
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 153:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 399
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 154:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 41
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 155:
            self.texto_trecho = ""
            self.tem_item = True
            self.item = "Escudo Dourado"
            self.tem_trecho_a = True
            self.n_trecho_a = 300
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 156:
            self.texto_trecho = ""
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 92
            self.n_trecho_b = 343
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 157:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 4
            self.n_trecho_b = 329
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 158:
            self.texto_trecho = ""
            self.m_nome = "Piranha"
            self.m_habilidade = 5
            self.m_energia = 5
            self.tem_trecho_a = True
            self.n_trecho_a = 218
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 159:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 237
            self.n_trecho_b = 365
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 160:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 161:
            self.texto_trecho = ""
            self.m_nome = "Goblin"
            self.m_habilidade = 5
            self.m_energia = 3
            self.tem_trecho_a = True
            self.n_trecho_a = 14
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 162:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 23
            self.n_trecho_b = 69
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 163:
            self.texto_trecho = ""
            self.tem_testar_sorte = True
            self.m_nome = "Gigante"
            self.m_habilidade = 8
            self.m_energia = 9
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 28
            self.n_trecho_b = 351
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 164:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 129
            self.n_trecho_b = 236
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 165:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 141
            self.n_trecho_b = 66
            self.n_trecho_c = 249
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 166:
            self.texto_trecho = ""
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 158
            self.n_trecho_b = 218
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 167:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 187
            self.n_trecho_b = 359
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 168:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 327
            self.n_trecho_b = 65
            self.n_trecho_c = 293
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 169:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 400
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 170:
            self.texto_trecho = ""
            self.tem_ouro = True
            self.ouro_fase = 4
            self.tem_trecho_a = True
            self.n_trecho_a = 319
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 171:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 337
            self.n_trecho_b = 187
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 172:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 249
            self.n_trecho_b = 141
            self.n_trecho_c = 165
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 173:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 24
            self.n_trecho_b = 135
            self.n_trecho_c = 360
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 174:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 198
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 175:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 177
            self.n_trecho_b = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 176:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 270
            self.n_trecho_b = 375
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 177:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 52
            self.n_trecho_b = 391
            self.n_trecho_c = 175
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 178:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 162
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 179:
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.temluta = True
            self.m_nome = "Gigante"
            self.m_habilidade = 9
            self.m_energia = 9
            self.n_trecho_a = 54
            self.n_trecho_b = 258
            self.n_trecho_c = 54
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 180:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 70
            self.n_trecho_b = 329
            self.n_trecho_c = 22
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 181:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 355
            self.n_trecho_b = 265
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 182:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 183:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 266
            self.n_trecho_b = 237
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 184:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 322
            self.n_trecho_b = 34
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 185:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 162
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 186:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 198
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 187:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 171
            self.n_trecho_b = 308
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 188:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Ratisomem"
            self.m_habilidade = 8
            self.m_energia = 5
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 342
            self.n_trecho_b = 209
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 189:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 90
            self.n_trecho_b = 25
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 190:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 167
            self.n_trecho_b = 359
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 191:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 308
            self.n_trecho_b = 392
            self.n_trecho_c = 46
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 192:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 169
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 193:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 93
            self.n_trecho_b = 338
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 194:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 142
            self.n_trecho_b = 105
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 195:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 140
            self.n_trecho_b = 164
            self.n_trecho_c = 9
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 196:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 280
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 197:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 48
            self.n_trecho_b = 295
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 198:
            self.texto_trecho = ""
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.n_trecho_a = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 199:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Home da Cavena"
            self.m_habilidade = 7
            self.m_energia = 6
            self.tem_trecho_a = True
            self.n_trecho_a = 283
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 200:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 387
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 201:
            self.texto_trecho = ""

            self.tem_ouro = True
            self.ouro_fase = 25
            self.tem_item = True
            self.item = "Poção da Invisibilidade"
            self.tem_trecho_a = True
            self.n_trecho_a = 293
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 202:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 87
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 203:
            self.texto_trecho = ""
            self.tem_item = True
            self.item = "Chave Casa Autuante"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 38
            self.n_trecho_b = 66
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 204:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 130
            self.n_trecho_b = 377
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 205:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 254
            self.n_trecho_b = 380
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 206:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 284
            self.n_trecho_b = 341
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 207:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 83
            self.n_trecho_b = 154
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 208:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 397
            self.n_trecho_b = 363
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 209:
            self.texto_trecho = ""
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 158
            self.n_trecho_b = 47
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 210:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 225
            self.n_trecho_b = 357
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 211:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 173
            self.n_trecho_b = 360
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 212:
            self.texto_trecho = ""
            self.tem_item = True
            self.item = "Mapa do Labirinto"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 369
            self.n_trecho_b = 120
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 213:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 36
            self.n_trecho_b = 314
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 214:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 271
            self.n_trecho_b = 104
            self.n_trecho_c = 99
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"

        elif self.n_trecho == 215:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 142
            self.n_trecho_b = 105
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 216:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 384
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 217:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 118
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 218:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 3
            self.n_trecho_b = 386
            self.n_trecho_c = 209
            self.n_trecho_d = 316
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}?"

        elif self.n_trecho == 219:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 182
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 220:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 171
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 221:
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.tem_trecho_e = True
            self.n_trecho_a = 72
            self.n_trecho_b = 132
            self.n_trecho_c = 27
            self.n_trecho_d = 110
            self.n_trecho_e = 170
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}?"
            self.texto_trecho_e = f" vá para {self.n_trecho_e}?"

        elif self.n_trecho == 222:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 85
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 223:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 53
            self.n_trecho_b = 300
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 224:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 118
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 225:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 77
            self.n_trecho_b = 63
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 226:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"

        elif self.n_trecho == 227:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.tem_trecho_e = True
            self.n_trecho_a = 131
            self.n_trecho_b = 291
            self.n_trecho_c = 100
            self.n_trecho_d = 20
            self.n_trecho_e = 291
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}?"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}?"
            self.texto_trecho_e = f" vá para {self.n_trecho_e}?"

        elif self.n_trecho == 228:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 229:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 230:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 231:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 232:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 233:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 234:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 235:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 236:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 237:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 238:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 239:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 240:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 241:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 242:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 243:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 244:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 245:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 246:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 247:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 248:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 249:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 250:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 251:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 252:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 253:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 254:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 255:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 256:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 257:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 258:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 259:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 260:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 261:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 262:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 263:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 264:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 265:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 266:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 267:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 268:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 269:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 270:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 271:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 272:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 273:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 274:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 275:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 276:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 277:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 278:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 279:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 280:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 281:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 282:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 283:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 284:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 285:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 286:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 287:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 288:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 289:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 290:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 291:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 292:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 293:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 294:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 295:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 296:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 297:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 298:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 299:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 300:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 301:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 302:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 303:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 304:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 305:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 306:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 307:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 308:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 309:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 310:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 311:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 312:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 313:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 314:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 315:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 316:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 317:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 318:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 319:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 320:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 321:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 322:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 323:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 324:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 325:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 326:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 327:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 328:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 329:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 330:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 331:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 332:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 333:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 334:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 335:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 336:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 337:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 338:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 339:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 340:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 341:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 342:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 343:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 344:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 345:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 346:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 347:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 348:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 349:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 350:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 351:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 352:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 353:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 354:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 355:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 356:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 357:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 358:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 359:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 360:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 361:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 362:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 363:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 364:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 365:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 366:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 367:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 368:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 369:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 370:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 371:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 372:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 373:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 374:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 375:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 376:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 377:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 378:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 379:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 380:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 381:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 382:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 383:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 384:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 385:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 386:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 387:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 388:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 389:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 390:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 391:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 392:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 393:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 394:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 395:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 396:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 397:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 398:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 399:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"

        elif self.n_trecho == 400:
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f" vá para {self.n_trecho_a}?"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}?"
