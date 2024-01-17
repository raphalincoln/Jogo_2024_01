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
                 m_nome1="",
                 m_nome2="",
                 m_nome3="",
                 m_nome4="",
                 m_energia=0,
                 m_energia1=0,
                 m_energia2=0,
                 m_energia3=0,
                 m_energia4=0,
                 m_habilidade=0,
                 m_habilidade1=0,
                 m_habilidade2=0,
                 m_habilidade3=0,
                 m_habilidade4=0,
                 tem_luta=False,
                 tem_multiluta=False,
                 quantas_lutas=0,
                 tem_trecho_a=False,
                 tem_trecho_b=False,
                 tem_trecho_c=False,
                 tem_trecho_d=False,
                 tem_trecho_e=False,
                 tem_item=False,
                 lista_item=[],
                 item="",
                 soltar_item=False,
                 item_a_soltar="",
                 tem_ouro=False,
                 ouro_fase=0,
                 contador=0,
                 livro_titulo="",
                 tem_testar_sorte=False,
                 alterar_valor=False,
                 alterar_energia=0,
                 alterar_habilidade=0,
                 alterar_sorte=0,
                 altera_provisao=False,
                 alterar_provisao=0,
                 desistir = False,
                 tem_fuga=False,
                 destino_fuga=0):
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
        self.tem_multiluta = tem_multiluta
        self.quantas_lutas = quantas_lutas
        self.tem_item = tem_item
        self.soltar_item = soltar_item
        self.item_a_soltar = item_a_soltar
        self.lista_item = lista_item
        self.item = item
        self.contador = contador
        self.tem_ouro = tem_ouro
        self.ouro_fase = ouro_fase
        self.livro_titulo = livro_titulo
        self.tem_testar_sorte = tem_testar_sorte
        self.livro_titulo = "O Feiticeiro da Montanha \n" \
                            "de Fogo!"
        self.alterar_valor = alterar_valor
        self.alterar_energia = alterar_energia
        self.alterar_habilidade = alterar_habilidade
        self.alterar_sorte = alterar_sorte
        self.m_nome1 = m_nome1
        self.m_nome2 = m_nome2
        self.m_nome3 = m_nome3
        self.m_nome4 = m_nome4
        self.m_energia1 = m_energia1
        self.m_energia2 = m_energia2
        self.m_energia3 = m_energia3
        self.m_energia4 = m_energia4
        self.m_habilidade1 = m_habilidade1
        self.m_habilidade2 = m_habilidade2
        self.m_habilidade3 = m_habilidade3
        self.m_habilidade4 = m_habilidade4
        self.altera_provisao = altera_provisao
        self.alterar_provisao = alterar_provisao
        self.desistir = desistir
        self.tem_fuga = tem_fuga
        self.destino_fuga = destino_fuga

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
                                 "bainha e se aproxima da caverna.Você dá uma primeira \n"
                                 "olhada na penumbra e vê-paredes escuras e úmidas com \n"
                                 "poças de água no chão de pedra à sua frente. O ar é frio\n"
                                 " e úmido. Você acende a sua lanterna e avança cautelosamente\n"
                                 "pela escuridão. Teias de aranha tocam seu rosto e você ouve\n"
                                 " a movimentação de pés minúsculos: muito provavelmente,\n"
                                 " ratazanas. Você adentra a caverna. Depois de uns poucos\n"
                                 "metros, chega logo a uma encruzilhada.")
            self.n_trecho_a = 71
            self.n_trecho_b = 278
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Você vai virar para o oeste {self.n_trecho_a}"
            self.texto_trecho_b = f"ou para o leste {self.n_trecho_b}"

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
            self.n_trecho_a = 269
            self.n_trecho_b = 16
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_testar_sorte = True
            self.texto_trecho_a = f"Sorte - Voce não foi ouvido, retorne para {self.n_trecho_a}"
            self.texto_trecho_b = f"Azar - O Ogro te ouviu, vá para {self.n_trecho_b}"

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
            self.texto_trecho_a = f"Pagar as peças de ouro vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Ameaça-lo, vá para {self.n_trecho_a}"

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
            self.texto_trecho_a = f"Ir para {self.n_trecho_a}"
            self.texto_trecho_b = f"Ir para {self.n_trecho_b}"

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
            self.texto_trecho_a = f"Bater na porta, vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Seguir para Norte, vá para {self.n_trecho_b}"

        elif self.n_trecho == 6:
            self.texto_trecho = "A grande porta maciça não possui maçaneta.\n" \
                                "Você tenta arrombá-la, mas não adianta. \n" \
                                "A porta nem se mexe. Você resolve desistir e\n" \
                                "passar pela abertura no caminho leste-oeste, \n" \
                                "retornando um pouco. Vá para 89."
            self.tem_trecho_a = True
            self.n_trecho_a = 89
            self.texto_trecho_a = f"Seguir para Leste-Oeste - {self.n_trecho_a}"

        elif self.n_trecho == 7:
            self.texto_trecho = "Você está na margem norte de um \n" \
                                "rio de correnteza rápida que corre\n" \
                                " em uma grande caverna subterrânea.\n" \
                                " Vá para 214."
            self.n_trecho_a = 214
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Ir para {self.n_trecho_a}"

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
            self.n_trecho_a = 189
            self.n_trecho_b = 273
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Se optar em Fugir, vá para {self.n_trecho_a}"
            self.texto_trecho_a = f"Se Vencer. vá para {self.n_trecho_b}"

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
            self.texto_trecho_a = f" Feramentas, vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Gavetas, vá para{self.n_trecho_b}"

        elif self.n_trecho == 10:
            self.texto_trecho = "Você chega de volta à encruzilhada\n" \
                                "e toma o caminho do norte. \n" \
                                "Vá para 77. \n"
            self.n_trecho_a = 77
            self.tem_trecho_a = True
            self.texto_trecho_a = f"seguir para o norte - {self.n_trecho_a}"

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
                                "como se fossem manuseadas por trabalhadores \n" \
                                "invisíveis. Uma cantoria em surdina vai se tornando\n" \
                                " cada vez mais alta e você identifica as palavras:\n" \
                                " “Rá-rá, Rá-rá, Lá vamos Enquanto você fica assistindo,\n" \
                                " começa a rir - a cena é bem divertida. Você senta e " \
                                "fica assistindo, conseguindo até mesmo bater um papo " \
                                "com algumas das ferramentas mágicas. Ganhe 2 pontos de \n" \
                                "ENERGIA e 1 ponto de HABILIDADE enquanto relaxa. Depois " \
                                "retorne pela passagem até a \n" \
                                "encruzilhada, por onde você pode ir para o norte \n" \
                                "(vá para 366) ou para o sul (vá para 250)."
            self.n_trecho_a = 366
            self.n_trecho_b = 250
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Seguir para o Norte -   {self.n_trecho_a}"
            self.texto_trecho_b = f"Seguir para o Sul, vá para {self.n_trecho_b}"

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
            self.texto_trecho_a = f"Descobrir o que atraiu, vá para {self.n_trecho_a}"

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
            self.texto_trecho_a = f"Seguir para {self.n_trecho_a}"

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
            self.texto_trecho_a = f"Ir para {self.n_trecho_a}"

        elif self.n_trecho == 15:
            self.texto_trecho = "Enquanto você está sentado no banco comendo a sua\n " \
                                "refeição, começa a se sentir profundamente relaxado, \n" \
                                "e as dores de seu corpo parecem estar desaparecendo \n" \
                                "aos poucos. Este lugar de descanso é encantado. \n" \
                                "Você pode recuperar 2 pontos adicionais de ENERGIA, \n" \
                                "como também até a quantidade normal (mas somente se\n" \
                                " isso não ultrapassar seu \n" \
                                "índice Inicial de ENERGIA), e recuperar 1 ponto \n" \
                                "de HABILIDADE, se algum já tiver sido perdido. \n" \
                                "Quando estiver pronto para\n" \
                                "continuar, siga pela passagem e vá para 367."
            self.n_trecho_a = 367
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Seguir para {self.n_trecho_a}"

        elif self.n_trecho == 16:
            self.texto_trecho = "Você desembainha a sua espada\n" \
                                "e, ao fazê-lo, o Ogro o Ouve\n" \
                                "e se prepara para atacar:\n" \
                                "Lutar vá para 50 ou fugir, vá para 269"
            self.n_trecho_a = 269
            self.n_trecho_b = 50
            self.temluta = True
            self.m_nome = "Ogro"
            self.m_habilidade = 8
            self.m_energia = 10
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.texto_trecho_a = f"Fugir - Vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Lutar - Vá para {self.n_trecho_b}"

        elif self.n_trecho == 17:
            self.texto_trecho = "Usando a estaca de madeira e a marreta\n" \
                                "(ou uma marreta improvisada, se não estiver\n" \
                                "levando uma), você forma uma cruz e avança\n" \
                                "na direção do Vampiro, encurralando-o em um\n" \
                                "canto. Ele geme e tenta alcançá-lo, mas não pode\n" \
                                "se aproximar. Porém não vai ser fácil cravar a\n" \
                                "estaca em seu coração. Ao avançar, você tropeça e \n" \
                                "cai para a frente. Por obra e graça da sorte, \n" \
                                "a estaca voa.e atinge a criatura que solta um\n " \
                                "grito. \n" \
                                "Teste a sua Sorte. \n" \
                                "Se você tiver sorte, a estaca penetra no coração \n" \
                                "do Vampiro. Se você não tiver sorte, o Vampiro \n" \
                                "sofre apenas um ferimento leve (deduza 3 pontos \n" \
                                "de sua ENERGIA) e atira você para o outro lado do\n " \
                                "aposento, na direção \n" \
                                "da porta oeste. Para Fugir por ela, vá para 380. \n" \
                                "Para continuar lutando, vá para 144. Se você teve \n" \
                                "sorte e matou o Vampiro, pode procurar o \n" \
                                "tesouro dele – vá para 327"
            self.n_trecho_a = 380  # Fugir
            self.n_trecho_b = 327  # Sorte
            self.n_trecho_c = 144  # azar
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_testar_sorte = True
            self.texto_trecho_a = f"Fugir - Fugir {self.n_trecho_a}"
            self.texto_trecho_b = f"Sorte - Matou o Vampiro - Vá para {self.n_trecho_b}"
            self.texto_trecho_c = f"Azar - Feriu o vampiro e vai lutar - {self.n_trecho_c}"

        elif self.n_trecho == 18:
            self.texto_trecho = "Você anda para o oeste pela passagem. \n" \
                                "Após uns 50 metros mais ou menos, o caminho\n" \
                                "vira para o norte. Depois de andar dois ou\n" \
                                "três passos nesta direção, você ouve um ruído\n" \
                                "de desmoronamento embaixo de seus pés e tenta \n" \
                                "recuar, enquanto o chão desaba. Teste a sua Sorte. \n" \
                                "Se você tiver sorte, consegue pular rapidamente \n" \
                                "para trás antes que se abra um poço. Se você " \
                                "não tiver sorte é porque foi lento demais e acaba\n" \
                                " caindo mais\n" \
                                "de dois metros abaixo em um poço – perde um ponto de\n" \
                                "ENERGIA. Se você teve sorte, é melhor voltar para\n" \
                                "a encruzilhada (vá para 261). Se você não teve sorte, \n" \
                                "vá para 348."
            self.n_trecho_a = 261  # Sorte
            self.n_trecho_b = 348  # azar
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_testar_sorte = True
            self.texto_trecho_a = f"Sorte - Retornou para encruzilhada -  {self.n_trecho_a}"
            self.texto_trecho_b = f"Azar - Caiu e vai para  {self.n_trecho_b}"

        elif self.n_trecho == 19:
            self.texto_trecho = "Estes dois seres cruéis são Goblins. \n" \
                                "Eles atacarão você, um de cada vez."
            self.n_trecho_a = 317
            self.temluta = True
            self.m_nome = "Goblin"
            self.m_habilidade = 5
            self.m_energia = 5
            self.tem_trecho_a = True
            self.texto_trecho_a = f"Se vencer, vá para {self.n_trecho_a}"

        elif self.n_trecho == 20:
            self.texto_trecho = "O confronto começa. Você tem sua espada, \n" \
                                "eles têm suas armas. Eles atacam você, \n" \
                                "um de cada vez:\n"
            self.n_trecho_b = 376
            self.n_trecho_a = 291
            self.temluta = True
            self.m_nome = "Anão"
            self.m_habilidade = 7
            self.m_energia = 4
            self.tem_trecho_a = True
            self.tem_trecho_b = True

            self.texto_trecho_b = f"Se Vencer, vá para {self.n_trecho_a}"
            self.texto_trecho_a = f"Se fugir, vá para {self.n_trecho_b}"

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
            self.texto_trecho_a = f"Bater com a Espada, vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Deixar de lado, vá para {self.n_trecho_b}"

        elif self.n_trecho == 22:
            self.texto_trecho = "Você tateia a parede em busca de sinais de portas \n" \
                                "secretas, mas não consegue encontrar nada. Você \n" \
                                "pára para pensar em sua situação e um pequeno jato \n" \
                                "de gás esguicha do teto. Você tosse e engasga, tentando \n" \
                                "limpar os pulmões, mas cai de joelhos. Sua cabeça roda e \n" \
                                "você desmaia no chão, perdendo a consciência. Quando a \n" \
                                "recupera, se vê em um lugar desconhecido. Volte para 4."
            self.tem_trecho_a = True
            self.n_trecho_a = 4
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 23:
            self.texto_trecho = "A passagem termina em uma porta sólida, e você \n" \
                                "fica surpreso, ao ver uma saia de couro enfiada \n" \
                                "na parte de baixo da porta. Você põe o ouvido \n" \
                                "colado na porta, mas não ouve nada. Você prefere \n" \
                                "entrar no aposento (vá para 326) ou retornar à \n" \
                                "encruzilhada (vá para 229)?"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 326
            self.n_trecho_b = 229
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 24:
            self.texto_trecho = "Depois de ter sofrido o seu terceiro ferimento, \n " \
                                "você repara que sua força está se esgotando. \n" \
                                "Perca 1 ponto de HABILIDADE. Você deduz que \n" \
                                "isto é consequência de mais outro poder mágico \n" \
                                "deste ser repulsivo e sente um arrepio de pânico. \n" \
                                "Você continua ou corre? Se você quiser Fugir, pague \n" \
                                "a penalidade e vá para 360 para escapar pela porta \n" \
                                "norte. Do contrário, a luta continua. Se você \n" \
                                "derrotar o ser, vá para 135. Mas, de agora em \n" \
                                "diante, perderá 1 ponto da sua HABILIDADE a cada \n" \
                                "vez que a fera ferir você três vezes."
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 360
            self.n_trecho_b = 135
            self.texto_trecho_a = f"Fugir - vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Lutar - vá para {self.n_trecho_b}"

        elif self.n_trecho == 25:
            self.texto_trecho = "Os quadros pintados são retratos de homens.\n" \
                                " Você sente Um frio na espinha ao ler a inscrição\n" \
                                " embaixo do que está na parede oeste - é o nome de \n" \
                                "Zagor, o Feiticeiro, cujo tesouro você está \n" \
                                "procurando. Você olha para o retrato dele e \n" \
                                "compreende que está medindo forças com um adversário\n" \
                                " poderosíssimo. Você tem a sensação de estar sendo \n" \
                                "observado e repara nos olhos penetrantes que o \n" \
                                "seguem nos seus movimentos. Você se sente atraído\n" \
                                " para o retrato e o medo aumenta. Perca 1 ponto de\n" \
                                " HABILIDADE. Você tem mesmo coragem de enfrentar \n" \
                                "e combater o Feiticeiro? Você pode sair direto pela \n" \
                                "porta norte (vá para 90) - mas considere isso como uma \n" \
                                "Fuga. Ou você pode também procurar em sua mochila uma \n" \
                                "arma para usar contra o poder do Feiticeiro – \n" \
                                "vá para 340."
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 90
            self.n_trecho_b = 340
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 26:
            self.texto_trecho = "De repente você se lembra do pequeno livro de \n" \
                                "capa de couro de Di Maggio e murmura suavemente as \n" \
                                "palavras mágicas contidas em suas páginas. Você grita\n" \
                                " alto com o Dragão e ele pára de avançar. Vira a \n" \
                                "cabeça de lado e olha desconfiadamente para você. \n" \
                                "Você joga uma pedra na sua cabeça, que quica em seu\n" \
                                "nariz. A fera solta um berro raivoso e respira fundo, \n" \
                                "provocando o som de um rugido no fundo da garganta. \n" \
                                "O Dragão solta o ar e, entre seus dentes, você vê uma\n" \
                                " outra bola de fogo se formando. Você se prepara e, \n" \
                                "quando a bola de fogo sai de sua boca, grita:\n" \
                                "Ekil Erif Ekam Erif Erif Erif Di Maggio\n" \
                                "A bola de fogo interrompe seu avanço. Com um \n" \
                                "berro de agonia, o Dragão tenta se livrar das\n" \
                                " chamas em seu focinho. Mas elas continuam a queimar\n" \
                                " ali mesmo. Gemendo de dor, o Dragão se vira e salta \n" \
                                "para a escuridão, sacudindo a cabeça de um lado \n" \
                                "para o outro. Vá para 371"
            self.tem_trecho_a = True
            self.n_trecho_a = 371
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 27:
            self.texto_trecho = "A espada é encantada e o ajudará na batalha. Enquanto \n" \
                                "você usar esta espada, poderá aumentar sua HABILIDADE \n" \
                                "Inicial em 2 pontos. Você pode também aumentar 2 pontos\n" \
                                " no valor atual de sua HABILIDADE. Acrescente 2 pontos \n" \
                                "à sua SORTE por ter encontrado esta espada. Jogue fora \n" \
                                "a sua espada velha e vá para 319. Se você preferir ficar \n" \
                                "coma sua própria espada, deixe sua HABILIDADE como está \n" \
                                "e fique apenas com o prêmio da SORTE."
            self.tem_trecho_a = True
            self.n_trecho_a = 319
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 28:
            self.texto_trecho = "O poderoso Gigante está morto! Você examina a \n" \
                                "caverna dele e acha pouca coisa que tenha utilidade,\n" \
                                " embora uma bolsa no cinto dele contenha oito \n" \
                                "Peças de Ouro. Você está um pouco preocupado com \n" \
                                "relação à segunda cadeira. A quem pertence? Você \n" \
                                "resolve sair da caverna como entrou. Vá para 351. \n" \
                                "Mas acrescente 2 pontos à sua SORTE e 2 à sua \n" \
                                "HABILIDADE pela sua vitória."
            self.tem_trecho_a = True
            self.n_trecho_a = 351
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 29:
            self.texto_trecho = "A não ser pelas botas, as quais você resolve ignorar,\n" \
                                " parece haver pouca coisa de valor na caverna. \n" \
                                "Você decide voltar por onde veio. Vá para 375."
            self.tem_trecho_a = True
            self.n_trecho_a = 375
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 30:
            self.texto_trecho = "Uma pedra solta cai e revela a presença de uma \n" \
                                "corda presa na rocha. Se você quiser \n" \
                                "puxá-la, vá para 67. \n" \
                                "Se sentir que seria prudente não mexer nela, \n" \
                                "poderá retornar à encruzilhada (vá para 267)."
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 67
            self.n_trecho_b = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 31:
            self.texto_trecho = "Se você tiver a jóia do Olho do Ciclope, segure-a \n" \
                                "diante do Feiticeiro. Seu olhar intimidador se \n" \
                                "transforma em uma expressão de dor. Ele obviamente \n" \
                                "sente o poder da jóia. Subitamente os olhos dele\n" \
                                " ficambrancos e sua expressão torna-se ausente. \n" \
                                "A confiança cresce à medida em que você toma \n" \
                                "consciência de que venceu a sua primeira verdadeira \n" \
                                "batalha. Ganhe 2 pontos de HABILIDADE. Ponha a \n" \
                                "jóia de volta em sua mochila e \n" \
                                "saia pela porta norte. Vá para 90."
            self.tem_trecho_a = True
            self.n_trecho_a = 90
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 32:
            self.texto_trecho = "Você joga o Queijo para o outro lado do aposento e as\n" \
                                " Ratazanas correm atrás dele, mordendo-se e arranhando\n" \
                                " umas às outras enquanto lutam por ele. Já que as\n" \
                                " distraiu, você atravessa o aposento e sai pela porta da\n" \
                                " parede norte. Vá para 124. Adicione 2 pontos \n" \
                                "à sua SORTE pelo seu êxito."
            self.tem_trecho_a = True
            self.n_trecho_a = 124
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 33:
            self.texto_trecho = "O ser que dormia desperta sobressaltado. Ele fica \n" \
                                "em pé e avança sobre você desarmado. Com sua espada,\n" \
                                "você deve ser capaz de derrotá-lo, mas seus dentes\n" \
                                "afiados parecem bem perigosos. Você pode Fugir \n" \
                                "pela porta (vá para 320) ou ficar e lutar contra \n" \
                                "o Orc que está atacando você. Se você \n" \
                                "derrotar o ser, pode levar a caixa. Vá para 147.\n"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.temluta = True
            self.m_nome = "Orc"
            self.m_habilidade = 6
            self.m_energia = 4
            self.n_trecho_a = 320
            self.n_trecho_b = 147
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 34:
            self.texto_trecho = "Examinando as ferramentas, você encontra uma marreta\n" \
                                " com cabeça de madeira dura e um cinzel com uma sólida\n" \
                                " lâmina de prata. Você só pode ficar com uma das duas, \n" \
                                "isto se estiver preparado para dispensar um dos itens\n" \
                                " do equipamento que já está carregando. Se quiser fazer\n" \
                                " isso, faça as correções necessárias na sua Lista de \n" \
                                "Equipamento. O ruído na porta norte fica mais alto ainda\n" \
                                " e você vai até lá para investigar. Vá para 96."
            self.tem_trecho_a = True
            self.n_trecho_a = 96
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 35:
            self.texto_trecho = "Ao entrar no aposento, a porta se fecha imediatamente\n" \
                                " atrás de você. Ao se fechar, ouve-se um estalo e um\n" \
                                " esguicho. Do centro do teto, um jato de gás está enchendo\n" \
                                " o aposento com um vapor acre. Você tenta respirar e\n" \
                                " tosse convulsivamente. Você olha para a porta e depois\n" \
                                " para a chave. Você retornará à porta e escapará\n" \
                                " rapidamente (vá para 136) ou prenderá a respiração e \n" \
                                "correrá para pegar a chave primeiro (vá para 361)?"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 136
            self.n_trecho_b = 361
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 36:
            self.texto_trecho = "A porta trancada abre-se violentamente e um mau cheiro\n" \
                                " insuportável chega às suas narinas. Dentro do aposento, \n" \
                                "o chão está coberto de ossos, vegetação apodrecida e lodo.\n" \
                                " Um velho de cabelos desgrenhados, vestido de trapos,\n" \
                                " salta sobre você gritando. Tem uma barba longa e grisalha\n" \
                                " e sacode um velho pé de cadeira de madeira. Ele \n" \
                                "simplesmente está louco, como parece, ou isto é algum\n" \
                                " tipo de armadilha? Você pode gritar com ele para tentar\n" \
                                " acalmá-lo (vá para 263) ou pegar na sua espada\n" \
                                " e atacá-lo (vá para 353)."
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 263
            self.n_trecho_b = 353
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 37:
            self.texto_trecho = "Em pé na encruzilhada, você pode ir\n" \
                                " para o norte (vá para 366), \n" \
                                "para o oeste (volte para 11) ou para o \n" \
                                "sul (vá para 277)."
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 366
            self.n_trecho_b = 11
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 38:
            self.texto_trecho = "Você abre a porta e encontra a dispensa de comidas do\n" \
                                " Lobisomem, um estoque variado de ossos e carnes\n" \
                                " apodrecidas. O cheiro provoca náuseas, embora um vidro\n" \
                                " com ovos em salmoura pareça conter uma comida razoavelmente\n" \
                                " decente. Se você quiser levá-lo consigo, será suficiente\n" \
                                " para duas refeições: adicione 2 pontos às suas Provisões. \n" \
                                "De volta ao aposento, agora você pode sair pela porta sul.\n" \
                                " Vá para 66."
            self.tem_trecho_a = True
            self.n_trecho_a = 66
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 39:
            self.texto_trecho = "Seu adversário fica surpreso ao ver você desaparecer na frente\n" \
                                " dele, mas ele levanta as mãos, como se quisesse cobrir os olhos,\n" \
                                " e vasculha o aposento com um olhar atento. Ele consegue sentir\n" \
                                " a sua presença, mas não é capaz de saber exatamente onde você\n" \
                                " está. Você desembainha a sua espada e avança na direção dele. \n" \
                                "Ele inclina a cabeça e cheira o ar. Você terá que lutar com ele\n" \
                                "à distância uma vez que, se ele puser as mãos em você, a \n" \
                                "invisibilidade não será mais vantagem nenhuma. Mas enquanto você \n" \
                                "permanecer invisível, terá as seguintes vantagens: \n " \
                                "Você pode acrescentar 2 pontos ao resultado que der nos dados \n" \
                                "quando determinar a sua Força de Ataque. \n " \
                                "Cada ataque seu bem-sucedido causará danos ao adversário\n" \
                                "de 3 pontos uma vez que, como ele não pode vê-lo, não\n" \
                                "consegue se defender adequadamente. \n  " \
                                "Cada vez que ele lhe causar um ferimento, jogue apenas \n" \
                                "um dado. Se o número for ímpar, ele feriu você de verdade. \n" \
                                "Se o número for 2 ou 4, o ferimento causado só vale 1 ponto.\n" \
                                " Se você conseguir um 6, você evita o \n" \
                                "golpe que não lhe causa dano nenhum."

            # self.tem_testar_sorte = True
            self.temluta = True
            self.m_nome = "Feiticeiro"
            self.m_habilidade = 11
            self.m_energia = 18
            self.tem_trecho_a = True
            self.n_trecho_a = 396
            self.texto_trecho_a = f"Sorte - vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Azar -  vá para {self.n_trecho_b}"

        elif self.n_trecho == 40:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 355
            self.n_trecho_b = 265
            self.n_trecho_b = 181
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_b = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 41:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Monstro"
            self.m_habilidade = 9
            self.m_energia = 6
            self.tem_trecho_a = True
            self.n_trecho_a = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 42:
            self.texto_trecho = "Afinal você chega ao final da trilha, \n" \
                                "em um encontro de três caminhos.\n " \
                                "Você pode ir para o oeste (vá para 257) \n" \
                                "ou para o leste (vá para 113).\n"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 257
            self.n_trecho_b = 113
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 43:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 354
            self.n_trecho_b = 52
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 44:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 399
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 45:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 90
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 46:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 4
            self.n_trecho_b = 206
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 47:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 158
            self.n_trecho_b = 298
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 48:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 391
            self.n_trecho_b = 60
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 49:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 122
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 50:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 269
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 51:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 287
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_a = f" vá para {self.n_trecho_c}"
            self.texto_trecho_b = f" vá para {self.n_trecho_d}"
            self.texto_trecho_a = f" vá para {self.n_trecho_e}"

        elif self.n_trecho == 53:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 155
            self.n_trecho_b = 300
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 54:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 308
            self.n_trecho_b = 179
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 55:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 7
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 56:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 399
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 57:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 16
            self.n_trecho_b = 2
            self.n_trecho_c = 119
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_b = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 58:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 15
            self.n_trecho_b = 367
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 59:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 150
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 60:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 48
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 62:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 6
            self.n_trecho_b = 89
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 63:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 281
            self.n_trecho_b = 10
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 64:
            self.texto_trecho = "Morte"

        elif self.n_trecho == 65:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 293
            self.n_trecho_b = 372
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 66:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 104
            self.n_trecho_b = 99
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 67:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 267
            self.n_trecho_b = 177
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 68:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 303
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 69:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 244
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 70:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

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
            self.desistir = True
            self.texto_trecho_a = f"Sorte - Vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Azar - Vá para {self.n_trecho_b}"

        elif self.n_trecho == 72:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 319
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 73:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 218
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 74:
            self.texto_trecho = ""
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 118
            self.n_trecho_b = 279
            self.texto_trecho_a = f"Sorte - vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Azar - vá para {self.n_trecho_b}"

        elif self.n_trecho == 75:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 93
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 76:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 244
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 77:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 345
            self.n_trecho_b = 18
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 78:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 159
            self.n_trecho_b = 237
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 79:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 137
            self.n_trecho_b = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_a = f" vá para {self.n_trecho_c}"
            self.texto_trecho_b = f" vá para {self.n_trecho_d}"

        elif self.n_trecho == 81:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 205
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 82:
            self.texto_trecho = "A porta se abre para revelar um aposento pequeno e de\n" \
                                " cheiro forte. No centro do aposento há uma mesa de \n" \
                                "madeira instável onde está uma vela acesa. Embaixo da \n" \
                                "mesa há uma pequena caixa de madeira. Dormindo em \n" \
                                "um colchão de palha,no canto mais distante do \n" \
                                "aposento, está um ser baixo e robusto,com um rosto \n" \
                                "feio e cheio de verrugas: o mesmo tipo de ser \n" \
                                "que você encontrou dormindo no posto de sentinela. \n" \
                                "Deve ser o guarda do turno da noite. Você pode \n" \
                                "retornar para o \n" \
                                "corredor e seguir em frente para o norte \n" \
                                "(vá para 208) ou insinuar-se pelo aposento \n" \
                                "para tentar pegar a caixa sem acordar o ser. Se \n" \
                                "você quiser tentar roubar a caixa,\n" \
                                " Teste a sua Sorte. Se você tiver sorte, ele não \n" \
                                "acordará- vá para 147. Se não tiver, volte para 33.\n"
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 147
            self.n_trecho_b = 33
            self.n_trecho_c = 208
            self.texto_trecho_a = f"Sorte - vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Azar - vá para {self.n_trecho_b}"
            self.texto_trecho_c = f"Neutro - vá para {self.n_trecho_c}"

        elif self.n_trecho == 83:
            self.texto_trecho = "Teste a sua Sorte. Se você tiver sorte, \n" \
                                "consegue sair pela porta norte - \n" \
                                "vá para 360. Se não tiver, vá para 154\n"
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 154
            self.n_trecho_b = 360
            self.texto_trecho_a = f"Sorte - Vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Azar - Vá para {self.n_trecho_b}"

        elif self.n_trecho == 84:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 204
            self.n_trecho_b = 280
            self.n_trecho_c = 377
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_b = f" vá para {self.n_trecho_c}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_a = f" vá para {self.n_trecho_c}"
            self.texto_trecho_b = f" vá para {self.n_trecho_d}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 87:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 262
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 88:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 216
            self.n_trecho_b = 384
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 89:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 286
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 90:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 253
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 91:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_testar_sorte = True
            self.n_trecho_a = 131
            self.n_trecho_b = 20
            self.texto_trecho_a = f"Sorte - vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Azar -  vá para (Sucesso) {self.n_trecho_b}"

        elif self.n_trecho == 92:
            self.texto_trecho = "Você chega de volta à encruzilhada na passagem. \n" \
                                "Você olha à esquerda e vê a entrada da caverna à \n" \
                                "distância, na penumbra, mas segue em frente \n" \
                                "caminhando. Volte para 71.\n"
            self.tem_trecho_a = True
            self.n_trecho_a = 71
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 93:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 8
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 94:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 260
            self.n_trecho_b = 329
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 95:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 205
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 96:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 374
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 97:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 334
            self.n_trecho_b = 247
            self.n_trecho_c = 292
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_b = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 98:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 358
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 99:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 383
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 100:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 346
            self.n_trecho_b = 91
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 101:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 327
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 102:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 303
            self.n_trecho_b = 19
            self.n_trecho_c = 68
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 103:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 252
            self.n_trecho_b = 359
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 104:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 49
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_b}"
            self.texto_trecho_d = f" vá para {self.n_trecho_b}"
            self.texto_trecho_e = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 106:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 152
            self.n_trecho_b = 126
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 107:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 148
            self.n_trecho_b = 197
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 108:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Mão"
            self.m_habilidade = 6
            self.m_energia = 4
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 185
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 109:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 120
            self.n_trecho_b = 212
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 110:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 319
            self.tem_ouro = True
            self.ouro_fase = 10
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 111:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 249
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 112:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 142
            self.n_trecho_b = 105
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 113:
            self.texto_trecho = "Compre o Jogo completo!"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 114:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 359
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 115:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 95
            self.n_trecho_b = 313
            self.n_trecho_c = 330
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 116:
            self.texto_trecho = "Os dois Orcs bêbados que você está enfrentando agora\n" \
                                "estão evidentemente espantados com a sua entrada e, \n" \
                                "tão rápido quanto são capazes, saem em busca de armas. \n" \
                                "Você tem que atacar um de cada vez. A bebedeira deles\n" \
                                "permite que você acrescente 1 ponto ao resultado do \n" \
                                "dado quando jogar para estabelecera sua Força de Ataque, \n" \
                                "durante cada Série de Ataques. \n" \
                                "\n" \
                                "Se você vencer a batalha, vá para 378. Se você quiser \n" \
                                "Fugir durante a batalha, pode fazer isso voltando para 42"
            self.temluta = True
            self.tem_fuga = True
            self.destino_fuga = 42
            self.tem_multiluta = True
            self.quantas_lutas = 1

            self.m_nome = "Orc Bebado 1"
            self.m_energia = 4
            self.m_habilidade = 5

            self.m_nome1 = "Orc Bebado 2"
            self.m_energia1 = 5
            self.m_habilidade1 = 5

            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_b = 378
            self.n_trecho_a = 42
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 117:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 354
            self.n_trecho_b = 308
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 120:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 197
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 121:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 103
            self.n_trecho_b = 359
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 122:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 268
            self.n_trecho_b = 282
            self.n_trecho_c = 13
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 123:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 184
            self.n_trecho_b = 164
            self.n_trecho_c = 140
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 124:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 138
            self.n_trecho_b = 76
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 125:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 73
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 126:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 152
            self.n_trecho_b = 26
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 127:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 272
            self.n_trecho_b = 188
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 128:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 210
            self.n_trecho_b = 58
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 129:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 104
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 130:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 280
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 131:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 291
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 132:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 319
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 133:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 52
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 134:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 202
            self.n_trecho_b = 325
            self.n_trecho_c = 87
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 135:
            self.texto_trecho = ""
            self.tem_ouro = True
            self.ouro_fase = 18
            self.tem_trecho_a = True
            self.n_trecho_a = 360
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 136:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 229
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 137:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 354
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 138:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 163
            self.n_trecho_b = 351
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

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
                                "as chaves corretas.\n" \
                                "Se você não tiver três chaves numeradas, \n" \
                                "então chegou ao fim de sua jornada. Você \n" \
                                "senta na arca e chora ao tomar consciência \n" \
                                "de que terá que explorar a montanha mais\n" \
                                " uma vez a fim de encontrar as tais chaves.\n"
            self.tem_trecho_a = True
            self.n_trecho_a = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 140:
            self.texto_trecho = ""
            self.m_nome = "Esqueleto"
            self.m_habilidade = 7
            self.m_energia = 5
            self.tem_trecho_a = True
            self.n_trecho_a = 395
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 141:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 66
            self.n_trecho_b = 111
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 142:
            self.texto_trecho = ""
            self.m_nome = "Esqueleto"
            self.m_habilidade = 7
            self.m_energia = 5
            self.tem_trecho_a = True
            self.n_trecho_a = 396
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 143:
            self.texto_trecho = ""
            self.m_nome = "Verme de Areia"
            self.m_habilidade = 7
            self.m_energia = 7
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 44
            self.n_trecho_b = 399
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 144:
            self.texto_trecho = "O ser mantém o seu olhar preso no olhar \n" \
                                "dele e você fica incapaz de controlar as \n" \
                                "suas próprias ações. Ele faz um sinal \n" \
                                "para que você avance. Você se move \n" \
                                "lentamente na direção dele com a boca \n" \
                                "aberta. Ele lhe diz para jogar fora a \n" \
                                "estaca. Ao olhar para a estaca, você \n" \
                                "sente um alento de força retornar à sua \n" \
                                "própria vontade e joga a estaca nele bem de \n" \
                                "perto. Teste a sua Sorte. Se você tiver \n" \
                                "sorte, volte para 101. Se não \n" \
                                "tiver, vá para 217.\n"
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 101
            self.n_trecho_b = 217
            self.texto_trecho_a = f"Sorte - vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Azar - vá para {self.n_trecho_b}"

        elif self.n_trecho == 145:
            self.texto_trecho = "A caixa caiu no chão durante a sua luta com a \n" \
                                "Serpente, e de dentro dela caiu uma chave de cor \n" \
                                "de bronze com o número 99 gravado nela. \n" \
                                "Você pode levar esta chave com você \n" \
                                "(anote isto na sua Lista de Equipamento) \n" \
                                "e sair do aposento. Adicione 1 ponto de \n" \
                                "SORTE e vá para 363.\n"
            self.tem_item = True
            self.item = "Chave 99"
            self.tem_trecho_a = True
            self.alterar_valor = True
            self.alterar_sorte = +1
            self.n_trecho_a = 363
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 146:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 366
            self.n_trecho_b = 11
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 147:
            self.texto_trecho = "Você sai do aposento e abre a caixa na passagem.\n" \
                                "Lá dentro, você encontra uma única Peça de Ouro \n" \
                                "e um pequeno camundongo, que deve ter sido o animal \n" \
                                "de estimação do ser. Você guarda a moeda e solta \n" \
                                "o camundongo, que sai correndo pela passagem afora. \n" \
                                "Ganhe 2 pontos de SORTE e vá para 208."
            self.alterar_valor = True
            self.alterar_sorte = 2
            self.tem_ouro = True
            self.ouro_fase = 1
            self.tem_trecho_a = True
            self.n_trecho_a = 208
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 148:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 230
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 149:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 181
            self.n_trecho_b = 265
            self.n_trecho_c = 355
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 150:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 222
            self.n_trecho_b = 297
            self.n_trecho_c = 133
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 151:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 218
            self.n_trecho_b = 86
            self.n_trecho_c = 158
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 152:
            self.texto_trecho = ""
            self.m_nome = "Dragão"
            self.m_habilidade = 10
            self.m_energia = 12
            self.tem_trecho_a = True
            self.n_trecho_a = 371
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 153:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 399
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 154:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 41
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 155:
            self.texto_trecho = ""
            self.tem_item = True
            self.item = "Escudo Dourado"
            self.tem_trecho_a = True
            self.n_trecho_a = 300
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 156:
            self.texto_trecho = "Você bate contra aporta com o ombro. \n" \
                                "Jogue dois dados. Se o número obtido \n" \
                                "for menor ou igual a seu índice de HABILIDADE, \n" \
                                "você conseguiu – vá para 343. Se o número \n" \
                                "obtido for maior do que a sua HABILIDADE, \n" \
                                "você esfrega o ombro machucado e resolve \n" \
                                "não tentar de novo. Volte para 92 para \n" \
                                "retornar à encruzilhada.\n"
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 92
            self.n_trecho_b = 343
            self.texto_trecho_a = f"Sorte - vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Sorte - vá para {self.n_trecho_b}"

        elif self.n_trecho == 157:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 4
            self.n_trecho_b = 329
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 158:
            self.texto_trecho = ""
            self.m_nome = "Piranha"
            self.m_habilidade = 5
            self.m_energia = 5
            self.tem_trecho_a = True
            self.n_trecho_a = 218
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 159:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 237
            self.n_trecho_b = 365
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 160:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 161:
            self.texto_trecho = ""
            self.m_nome = "Goblin"
            self.m_habilidade = 5
            self.m_energia = 3
            self.tem_trecho_a = True
            self.n_trecho_a = 14
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 162:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 23
            self.n_trecho_b = 69
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 163:
            self.texto_trecho = "Você desembainha a sua espada e entra " \
                                "na caverna. O Gigante pára no meio de " \
                                "uma mastigadela, levanta a cabeça e " \
                                "cheira o ar. Ele se vira e consegue " \
                                "ver você se aproximando. Rugindo alto, " \
                                "ele atira a carcaça do porco em você. " \
                                "Teste a sua Sorte. Se tiver Sorte, ele " \
                                "erra. Se não tiver, ela o atinge com " \
                                "bastante força – você perde 1 ponto de " \
                                "ENERGIA. Ele então pega o seu martelo e " \
                                "se prepara para atingi-lo com ele. Resolva " \
                                "este combate." \
                                "Se você vencer, volte para 28. Você pode " \
                                "fugir depois de três Séries de Ataque, descendo " \
                                "pela passagem por onde ele não poderá " \
                                "segui-lo (vá para 351)"

            # self.tem_testar_sorte = True
            self.m_nome = "Gigante"
            self.m_habilidade = 8
            self.m_energia = 9
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 28
            self.n_trecho_b = 351
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 164:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 129
            self.n_trecho_b = 236
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 165:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 141
            self.n_trecho_b = 66
            self.n_trecho_c = 249
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 166:
            self.texto_trecho = "Você cai na água gelada e nada\n " \
                                "freneticamente para a margem sul. \n" \
                                "Para seu espanto, a jangada faz \n" \
                                "meia volta na metade do rio e retorna\n " \
                                "sozinha para a margem sul. Você \n" \
                                "acelera o ritmo, consciente de que \n" \
                                "as suas braçadas podem, a qualquer \n" \
                                "momento, atrair a atenção de quaisquer \n" \
                                "seres que vivam no fundo do rio. \n" \
                                "Jogue um dado. Se obtiver um, dois, \n" \
                                "três ou quatro, você chega em segurança à \n" \
                                "margem sul. Vá para 218. \n" \
                                "Se tirar um cinco ou um seis, volte para 158.\n"
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 158
            self.n_trecho_b = 218
            self.texto_trecho_a = f" Sorte - vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" Azar - vá para {self.n_trecho_b}"

        elif self.n_trecho == 167:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 187
            self.n_trecho_b = 359
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 168:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 327
            self.n_trecho_b = 65
            self.n_trecho_c = 293
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 169:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 400
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 170:
            self.texto_trecho = ""
            self.tem_ouro = True
            self.ouro_fase = 4
            self.tem_trecho_a = True
            self.n_trecho_a = 319
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 171:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 337
            self.n_trecho_b = 187
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 172:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 249
            self.n_trecho_b = 141
            self.n_trecho_c = 165
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 173:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 24
            self.n_trecho_b = 135
            self.n_trecho_c = 360
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 174:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 198
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 175:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 177
            self.n_trecho_b = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 176:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 270
            self.n_trecho_b = 375
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 177:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 52
            self.n_trecho_b = 391
            self.n_trecho_c = 175
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 178:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 162
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 180:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 70
            self.n_trecho_b = 329
            self.n_trecho_c = 22
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 181:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 355
            self.n_trecho_b = 265
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 182:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 183:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 266
            self.n_trecho_b = 237
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 184:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 322
            self.n_trecho_b = 34
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 185:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 162
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 186:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 198
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 187:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 171
            self.n_trecho_b = 308
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 189:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 90
            self.n_trecho_b = 25
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 190:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 167
            self.n_trecho_b = 359
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 191:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 308
            self.n_trecho_b = 392
            self.n_trecho_c = 46
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 192:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 169
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 193:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 93
            self.n_trecho_b = 338
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 194:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 142
            self.n_trecho_b = 105
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 195:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 140
            self.n_trecho_b = 164
            self.n_trecho_c = 9
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 196:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 280
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 197:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 48
            self.n_trecho_b = 295
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 198:
            self.texto_trecho = "Uma das chaves gira, mas as outras " \
                                "duas não servem. Enquanto você está " \
                                "lutando para tentar fazê-las girar, " \
                                "ouve dois pequenos estalos e depois silvos, " \
                                "quando dois dardos minúsculos são " \
                                "disparados da arca na sua direção. " \
                                "Você salta para trás para tentar se " \
                                "desviar deles e bate com a cabeça na " \
                                "parede atrás de você, o que faz com que " \
                                "você perca a consciência e caia no chão. " \
                                "Teste a sua Sorte. Se você tiver " \
                                "sorte, os dardos não acertam você e " \
                                "você acorda coma cabeça doendo. Perde 2 " \
                                "pontos de ENERGIA. Se não tiver " \
                                "sorte, os dardos acertam a sua cabeça " \
                                "e você jamais recupera a consciência. " \
                                "Se você tiver tido sorte, poderá tentar " \
                                "chaves diferentes (lembre-se - uma das " \
                                "chaves serviu perfeitamente). Some os " \
                                "totais das chaves e vá para esta etapa. " \
                                "Se você tiver tentado todas as combinações " \
                                "com as chaves que você tem, você enterra a " \
                                "cabeça nas mãos e chora, depois de ter " \
                                "chegado até aqui. Você está tão perto " \
                                "de atingir o seu objetivo, mas terá " \
                                "que tentar mais outra vez. Entre novamente " \
                                "no subterrâneo - mas lembre-se de sempre " \
                                "procurar chaves enquanto você avança!"
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.n_trecho_a = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 199:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Home da Cavena"
            self.m_habilidade = 7
            self.m_energia = 6
            self.tem_trecho_a = True
            self.n_trecho_a = 283
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 200:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 387
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 201:
            self.texto_trecho = ""

            self.tem_ouro = True
            self.ouro_fase = 25
            self.tem_item = True
            self.item = "Poção da Invisibilidade"
            self.tem_trecho_a = True
            self.n_trecho_a = 293
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 202:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 87
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 203:
            self.texto_trecho = ""
            self.tem_item = True
            self.item = "Chave Casa Autuante"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 38
            self.n_trecho_b = 66
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 204:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 130
            self.n_trecho_b = 377
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 205:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 254
            self.n_trecho_b = 380
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 206:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 284
            self.n_trecho_b = 341
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 207:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 83
            self.n_trecho_b = 154
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 208:
            self.texto_trecho = "Mais adiante na passagem, seguindo a parede oeste, você \n" \
                                "vê outra porta. Você escuta com o ouvido colado nela,\n" \
                                " mas não ouve nada. Se quiser tentar abrir esta porta,\n" \
                                " vá para 397. Se quiser continuar na direção norte,\n" \
                                " vá para 363."
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 397
            self.n_trecho_b = 363
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 209:
            self.texto_trecho = "As toras da ponte estão podres e em \n" \
                                "decomposição por causa dos anos de \n" \
                                "abandono. Uma das toras cede sob o seu \n" \
                                "pé. Jogue um dado. O número seis \n" \
                                "significa que você cai no rio que passa \n" \
                                "embaixo -volte para 158. Se o resultado \n" \
                                "for de um a cinco, significa que você \n" \
                                "recupera seu equilíbrio. Volte para 47.\n"
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 158
            self.n_trecho_b = 47
            self.texto_trecho_a = f" Sorte - Vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" Azar - Vá para {self.n_trecho_b}"

        elif self.n_trecho == 210:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 225
            self.n_trecho_b = 357
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 211:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 173
            self.n_trecho_b = 360
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 212:
            self.texto_trecho = ""
            self.tem_item = True
            self.item = "Mapa do Labirinto"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 369
            self.n_trecho_b = 120
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 213:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 36
            self.n_trecho_b = 314
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 214:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 271
            self.n_trecho_b = 104
            self.n_trecho_c = 99
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 215:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 142
            self.n_trecho_b = 105
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 216:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 384
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 217:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 118
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}"

        elif self.n_trecho == 219:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 182
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 220:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 171
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}"
            self.texto_trecho_e = f" vá para {self.n_trecho_e}"

        elif self.n_trecho == 222:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 85
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 223:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 53
            self.n_trecho_b = 300
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 224:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 118
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 225:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 77
            self.n_trecho_b = 63
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 226:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

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
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}"
            self.texto_trecho_e = f" vá para {self.n_trecho_e}"

        elif self.n_trecho == 228:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 85
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 229:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 69
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 230:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Espectro"
            self.m_habilidade = 8
            self.m_energia = 7
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 390
            self.n_trecho_b = 64
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 231:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 182
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 232:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 375
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 233:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 198
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 234:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 161
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 235:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 176
            self.n_trecho_b = 5
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 236:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Esqueleto"
            self.m_habilidade = 6
            self.m_energia = 5
            self.tem_trecho_a = True
            self.n_trecho_a = 395
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 237:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 285
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 238:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 70
            self.n_trecho_b = 180
            self.n_trecho_c = 329
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 239:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 88
            self.n_trecho_b = 149
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 240:
            self.texto_trecho = "A caixa é leve, mas alguma coisa chacoalha dentro dela. \n" \
                                "Você abre a tampa e uma pequena SERPENTE salta para \n" \
                                "morder seu pulso! Você terá que lutar contra a Serpente.\n" \
                                "Se você matar a Serpente, volte para 145"
            self.temluta = True
            self.m_nome = "Serpente"
            self.m_habilidade = 5
            self.m_energia = 2
            self.tem_trecho_a = True
            self.n_trecho_a = 145
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 241:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 90
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 242:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 379
            self.n_trecho_b = 139
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 243:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 128
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 244:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 143
            self.n_trecho_b = 198
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 245:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 198
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 246:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 329
            self.n_trecho_b = 180
            self.n_trecho_c = 70
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 247:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 292
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 248:
            self.texto_trecho = "O ser que acabou de acordar é um Orc! Ele se \n" \
                                "levanta rápido e se vira para puxar uma corda\n" \
                                " que provavelmente é a sineta do alarme. Você \n" \
                                "tem que atacá-lo imediatamente.Se você vencer, \n" \
                                "pode continuar seguindo a passagem vá para 301"
            self.temluta = True
            self.m_nome = "Orc"
            self.m_habilidade = 6
            self.m_energia = 5
            self.tem_trecho_a = True
            self.n_trecho_a = 301
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 249:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Cachorro"
            self.m_habilidade = 7
            self.m_energia = 6
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 66
            self.n_trecho_b = 304
            self.n_trecho_c = 66
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 250:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 366
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 251:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Morcego Gigante"
            self.m_habilidade = 6
            self.m_energia = 6
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 344
            self.n_trecho_b = 399
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 252:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 312
            self.n_trecho_b = 226
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 253:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 328
            self.n_trecho_b = 125
            self.n_trecho_c = 73
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 254:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 352
            self.n_trecho_b = 333
            self.n_trecho_c = 279
            self.n_trecho_d = 380
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}"

        elif self.n_trecho == 255:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 193
            self.n_trecho_b = 93
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 256:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 398
            self.n_trecho_b = 297
            self.n_trecho_c = 114
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 257:
            self.texto_trecho = "Compre o Jogo Completo!"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 1
            self.n_trecho_b = 1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 258:
            self.texto_trecho = ""
            self.tem_ouro = True
            self.ouro_fase = 8
            self.tem_item = True
            self.item = "Chave Vermelha - 111"
            self.tem_trecho_a = True
            self.n_trecho_a = 54
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 259:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 7
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 260:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 359
            self.n_trecho_b = 32
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 261:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 345
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 262:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 199
            self.n_trecho_b = 251
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 263:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 314
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 264:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 80
            self.n_trecho_b = 129
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 265:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 88
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 266:
            self.texto_trecho = ""
            self.tem_item = True
            self.item = "Arco e Flecha de Prata"
            self.tem_trecho_a = True
            self.n_trecho_a = 237
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 267:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 312
            self.n_trecho_b = 246
            self.n_trecho_c = 79
            self.n_trecho_c = 349
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_c = f" vá para {self.n_trecho_d}"

        elif self.n_trecho == 268:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 13
            self.n_trecho_b = 282
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 269:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 225
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 270:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 61
            self.n_trecho_b = 394
            self.n_trecho_c = 375
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 271:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 336
            self.n_trecho_b = 214
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 272:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 7
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 273:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 189
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 274:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 324
            self.n_trecho_b = 356
            self.n_trecho_c = 98
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 275:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 230
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 276:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 182
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 277:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 146
            self.n_trecho_b = 366
            self.n_trecho_c = 11
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 278:
            self.texto_trecho = "A passagem logo termina em uma porta de \n" \
                                "madeira trancada. Você cola o ouvido na porta. \n" \
                                "Mas não ouve nada. Você vai tentar derrubá-la? \n" \
                                "Em caso afirmativo, volte para 156. \n" \
                                "Se você preferir dar meia volta e retornar à \n" \
                                "encruzilhada, volte para 92.\n"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 156
            self.n_trecho_b = 92
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 279:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 380
            self.n_trecho_b = 17
            self.n_trecho_c = 333
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 280:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 311
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 281:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 10
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 282:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Zumbi"
            self.m_habilidade = 7
            self.m_energia = 6
            self.tem_trecho_a = True
            self.n_trecho_a = 115
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 283:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 251
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 284:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 46
            self.n_trecho_b = 251
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 285:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 213
            self.n_trecho_b = 314
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 286:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 294
            self.n_trecho_b = 275
            self.n_trecho_c = 148
            self.n_trecho_c = 107
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_c = f" vá para {self.n_trecho_d}"

        elif self.n_trecho == 287:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 32
            self.n_trecho_b = 309
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 288:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 182
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 289:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Feiriceiro"
            self.m_habilidade = 7
            self.m_energia = 12
            self.tem_trecho_a = True
            self.n_trecho_a = 396
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 290:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 198
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 291:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 315
            self.n_trecho_b = 52
            self.n_trecho_c = 227
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 292:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 239
            self.n_trecho_b = 40
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 293:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 113
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 294:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 275
            self.n_trecho_b = 148
            self.n_trecho_c = 107
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 295:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 48
            self.n_trecho_b = 161
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 296:
            self.texto_trecho = "A caixa contém um pequeno livro encadernado em \n" \
                                "couro, intitulado A Origem e Emissão do Fogo de \n" \
                                "Dragão. Você abre o livro e começa a ler. \n" \
                                "Felizmente está escrito na sua língua e, por \n" \
                                "isso, provavelmente não foi compreendido pelos Orçs \n" \
                                "- do contrário, este tesouro não estaria guardado \n" \
                                "tão desleixadamente quanto estava. O livro foi escrito \n" \
                                "à mão, em letra pequena, por Farrigo Di Maggio. \n" \
                                "Nele, o autor conta a história da obra de sua \n" \
                                "vida: a criação do feitiço do Fogo de Dragão, \n" \
                                "com o qual se poderia enfrentar Dragões cruéis. \n" \
                                "Você lê como, nos últimos anos, Farrigo finalmente \n" \
                                "aperfeiçoou seu feitiço mas, na época, já estava velho \n" \
                                "demais para fazer uso dele. Por isso ele completou \n" \
                                "seu livro, trancou-o em uma arca e o escondeu nas \n" \
                                "profundezas da Montanha de Fogo, com medo de que \n" \
                                "caísse em mãos erradas. A última página dizia assim:\n" \
                                "Subitamente, as páginas parecem brilhar e,\n " \
                                "Você profere estas palavras lenta e suavemente.\n " \
                                " Subitamente, as páginas parecem brilhar e,\n " \
                                " quando este brilho desaparece, também \n " \
                                "desaparecem as palavras nas páginas do livro.\n " \
                                " Você repete o feitiço para si mesmo, a fim de \n " \
                                "memorizar as palavras, e sai do aposento. \n " \
                                "Volte para 42."
            self.tem_item = True
            self.item = "Livro do Fogo"
            self.tem_trecho_a = True
            self.n_trecho_a = 42
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 297:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 150
            self.n_trecho_b = 256
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 298:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 86
            self.n_trecho_b = 7
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 299:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 260
            self.n_trecho_b = 359
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 300:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 102
            self.n_trecho_b = 303
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 301:
            self.texto_trecho = "À sua esquerda, na parte oeste da passagem, há uma \n" \
                                "porta de madeira rústica. Você pára junto a ela e \n" \
                                "ouve um som áspero que poderia ser de algum tipo \n" \
                                "de criatura roncando. \n" \
                                "Você quer abrir a porta? Em caso afirmativo,\n" \
                                " volte para 82. \n" \
                                "Se quiser seguir adiante para o norte, \n" \
                                "volte para 208.\n"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 82
            self.n_trecho_b = 208
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 302:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 198
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 303:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 128
            self.n_trecho_b = 243
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 304:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Lobisomem"
            self.m_habilidade = 8
            self.m_energia = 8
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 66
            self.n_trecho_b = 203
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 305:
            self.texto_trecho = "Teste a sua Sorte três vezes. " \
                                "Se você tiver sorte todas as vezes, " \
                                "consegue chegar à porta mais distante e " \
                                "sair do aposento. Volte para 162. " \
                                "Na primeira vez em que você não tiver " \
                                "sorte, pisa em um azulejo em forma de " \
                                "mão - volte para 108"
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 162
            self.n_trecho_b = 108
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 306:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 161
            self.n_trecho_b = 291
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 307:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 134
            self.n_trecho_b = 87
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 308:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 187
            self.n_trecho_b = 54
            self.n_trecho_c = 160
            self.n_trecho_d = 354
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}"

        elif self.n_trecho == 309:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Ratazana"
            self.m_habilidade = 5
            self.m_energia = 4
            self.tem_trecho_a = True
            self.n_trecho_a = 124
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 310:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 211
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 311:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 305
            self.n_trecho_b = 178
            self.n_trecho_c = 108
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 312:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 308
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 313:
            self.tem_item = True
            self.item = "Cricifixo"
            self.tem_ouro = True
            self.ouro_fase = 8
            self.item = "Espada de Aço"
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 221
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 314:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 223
            self.n_trecho_b = 300
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 315:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 306
            self.n_trecho_b = 291
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 316:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 151
            self.n_trecho_b = 218
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 317:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 303
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 318:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 228
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 319:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 221
            self.n_trecho_b = 81
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 320:
            self.texto_trecho = "Você sai correndo do aposento e fecha a porta com \n" \
                                "violência ao passar. Você vira na direção norte \n" \
                                "subindo a passagem, onde vê uma porta \n" \
                                "de aparência semelhante. Vá para 363"
            self.tem_trecho_a = True
            self.n_trecho_a = 363
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 321:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 169
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 322:
            self.texto_trecho = ""
            self.tem_item = True
            self.item = "Chave de Cobre - 66"
            self.tem_trecho_a = True
            self.n_trecho_a = 96
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 323:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 8
            self.n_trecho_b = 255
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 324:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 358
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 325:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 87
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 326:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 35
            self.n_trecho_b = 229
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 327:
            self.texto_trecho = ""
            self.ouro_fase = True
            self.ouro_fase = 30
            self.tem_item = True
            self.item = "Forquilha"
            self.item = "Livro do Vampiro"
            self.tem_trecho_a = True
            self.n_trecho_a = 380
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 328:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 73
            self.n_trecho_b = 125
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 329:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 157
            self.n_trecho_b = 392
            self.n_trecho_c = 299
            self.n_trecho_d = 238
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}"

        elif self.n_trecho == 330:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 81
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 331:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Troll"
            self.m_habilidade = 8
            self.m_energia = 8
            self.tem_trecho_a = True
            self.n_trecho_a = 287
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 332:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 329
            self.n_trecho_b = 4
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 333:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Vampiro"
            self.m_habilidade = 10
            self.m_energia = 10
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 327
            self.n_trecho_b = 224
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 334:
            self.texto_trecho = ""
            self.tem_item = True
            self.item = "Vela Azul"
            self.tem_trecho_a = True
            self.n_trecho_a = 292
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 335:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 182
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 336:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 66
            self.n_trecho_b = 172
            self.n_trecho_c = 249
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 337:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 267
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 338:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Ciclope de Ferro"
            self.m_habilidade = 10
            self.m_energia = 10
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 75
            self.n_trecho_b = 93
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 339:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 201
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 340:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 388
            self.n_trecho_b = 31
            self.n_trecho_c = 241
            self.n_trecho_d = 45
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}"

        elif self.n_trecho == 341:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 46
            self.n_trecho_b = 392
            self.n_trecho_c = 220
            self.n_trecho_d = 191
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}"

        elif self.n_trecho == 342:
            self.texto_trecho = ""
            self.tem_ouro = True
            self.ouro_fase = 2
            self.tem_trecho_a = True
            self.n_trecho_a = 7
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 343:
            self.texto_trecho = "A porta abre de repente e você se sente cair \n" \
                                "em um aposento. Mas seu coração acelera ao \n" \
                                "compreender que você não está caindo no chão, \n" \
                                "mas mergulhando em uma espécie de poço! Por sorte, \n" \
                                "o poço não é particularmente fundo e você bate no chão \n" \
                                "a menos de dois metros abaixo. Perca 1 ponto de \n" \
                                "ENERGIA pelas escoriações que sofreu, suba para a \n" \
                                "superfície do poço e saia do aposento pela porta, \n" \
                                "dirigindo-se para o oeste. Volte para 92"
            self.tem_trecho_a = True
            self.n_trecho_a = 92
            self.alterar_valor = True
            self.alterar_habilidade = -1
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 344:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 56
            self.n_trecho_b = 153
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 345:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 381
            self.n_trecho_b = 311
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 346:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 131
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 347:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 182
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 348:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 331
            self.n_trecho_b = 51
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 349:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 267
            self.n_trecho_b = 30
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 350:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Piranha"
            self.m_habilidade = 5
            self.m_energia = 5
            self.tem_trecho_a = True
            self.n_trecho_a = 7
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 351:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 76
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 352:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 74
            self.n_trecho_b = 279
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 353:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 314
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 354:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 308
            self.n_trecho_b = 52
            self.n_trecho_c = 14
            self.n_trecho_d = 234
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}"

        elif self.n_trecho == 355:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 181
            self.n_trecho_b = 256
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 356:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 358
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 357:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 269
            self.n_trecho_b = 57
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 358:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 142
            self.n_trecho_b = 105
            self.n_trecho_c = 389
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 359:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.tem_trecho_d = True
            self.n_trecho_a = 190
            self.n_trecho_b = 94
            self.n_trecho_c = 121
            self.n_trecho_d = 385
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"
            self.texto_trecho_d = f" vá para {self.n_trecho_d}"

        elif self.n_trecho == 360:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 89
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 361:
            self.texto_trecho = ""
            self.tem_item = True
            self.item = "Chave Dourada - 125"
            self.tem_trecho_a = True
            self.n_trecho_a = 136
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 362:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 177
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 363:
            self.texto_trecho = "Seguindo pela passagem na parede oeste, você vê\n" \
                                " outra porta semelhante. Você escuta junto \n" \
                                "à porta e faz uma careta ao ouvir a voz mais \n" \
                                "desafinada que seus ouvidos  já conheceram! \n" \
                                "Você quer entrar no aposento para\n" \
                                " investigar o horroroso som (vá para 370) \n" \
                                "ou seguir adiante pela passagem (volte para 42)?"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 370
            self.n_trecho_b = 42
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 364:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 256
            self.n_trecho_b = 373
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 365:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Orc"
            self.m_habilidade = 6
            self.m_energia = 4
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 183
            self.n_trecho_b = 237
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 366:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 89
            self.n_trecho_b = 62
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 367:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 235
            self.n_trecho_b = 323
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 368:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 142
            self.n_trecho_b = 105
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 369:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 109
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 370:
            self.texto_trecho = "A porta se abre e revela um pequeno aposento, \n" \
                                "que está sujo e mal cuidado. Um colchão de \n" \
                                "palha se encontra em um dos cantos. No centro \n" \
                                "do aposento há uma mesa de madeira, na\n" \
                                " qual brilha uma vela iluminando o ambiente \n" \
                                "com sua luz trêmula. Uma pequena caixa repousa \n" \
                                "sobre a mesa. Sentados em volta da mesa estão \n" \
                                "dois seres pequenos, com a pele cheia de verrugas \n" \
                                "e vestidos com armaduras de couro.\n" \
                                " Estão tomando algum tipo de bebida forte e, \n" \
                                "pelo jeito como se levantam cambaleantes quando \n" \
                                "você chega, demonstram estar muito embriagados. \n" \
                                "Você pode empunha a sua espada e atacá-los \n" \
                                "(volte para 116) ou fechar\n" \
                                " a porta rapidamente e correr subindo pela passagem\n" \
                                " (volte para 42).\n"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 116
            self.n_trecho_b = 42
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 371:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 274
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 372:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Chefe dos Orcs"
            self.m_habilidade = 7
            self.m_energia = 6
            self.tem_trecho_a = True
            self.n_trecho_a = 21
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 373:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 85
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 374:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 207
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 375:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 5
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 376:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 291
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 377:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Gremilin"
            self.m_habilidade = 5
            self.m_energia = 7
            self.tem_trecho_a = True
            self.n_trecho_a = 196
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 378:
            self.texto_trecho = "Você limpa a sua espada ensanguentada no colchão. \n" \
                                "O sangue  verde deixa uma mancha pastosa na palha. \n" \
                                "Passando por cima dos corpos na direção da mesa, \n" \
                                "você enjoa com o cheiro repelente dos seres mortos. Você\n" \
                                " pega a caixa que está embaixo da mesa e a examina.\n" \
                                " É uma pequena caixa de madeira com dobradiças \n" \
                                "rústicas. O nome “Farrigo Di Maggio” está gravado \n" \
                                "em uma placa de metal na tampa. Se quiser abrir a \n" \
                                "caixa, volte para 296. Se resolver deixá-la \n" \
                                "de lado e sair do aposento, volte para 42."
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 296
            self.n_trecho_b = 42
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 379:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 139
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 380:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 37
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 381:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 84
            self.n_trecho_b = 280
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 382:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 396
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 383:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 80
            self.n_trecho_b = 264
            self.n_trecho_c = 129
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 384:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 262
            self.n_trecho_b = 307
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 385:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 114
            self.n_trecho_b = 297
            self.n_trecho_c = 398
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 386:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 55
            self.n_trecho_b = 166
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 387:
            self.texto_trecho = "Morreu"
            exit()

        elif self.n_trecho == 388:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 90
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 389:
            self.texto_trecho = ""
            self.tem_testar_sorte = True
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 289
            self.n_trecho_b = 112
            self.texto_trecho_a = f"Sorte - vá para {self.n_trecho_a}"
            self.texto_trecho_b = f"Azar - vá para {self.n_trecho_b}"

        elif self.n_trecho == 390:
            self.texto_trecho = ""
            self.tem_ouro = True
            self.ouro_fase = 6
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 120
            self.n_trecho_b = 393
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 391:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.tem_trecho_c = True
            self.n_trecho_a = 52
            self.n_trecho_b = 362
            self.n_trecho_c = 48
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"
            self.texto_trecho_c = f" vá para {self.n_trecho_c}"

        elif self.n_trecho == 392:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 206
            self.n_trecho_b = 329
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 393:
            self.texto_trecho = ""
            self.tem_ouro = True
            self.ouro_fase = 8
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 212
            self.n_trecho_b = 369
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 394:
            self.texto_trecho = ""
            self.temluta = True
            self.m_nome = "Aranha"
            self.m_habilidade = 7
            self.m_energia = 28
            self.tem_trecho_a = True
            self.n_trecho_a = 232
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 395:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 322
            self.n_trecho_b = 34
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 396:
            self.texto_trecho = ""
            self.tem_trecho_a = True
            self.n_trecho_a = 242
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 397:
            self.texto_trecho = "A porta abre e revela um pequeno aposento de \n" \
                                "chão de pedra e paredes sujas. Há um cheiro de \n" \
                                "mofo no ar. No centro do aposento, há uma mesa \n" \
                                "improvisada de madeira, em cima da qual está uma \n" \
                                "vela acesa. Sob a mesa, há uma pequena caixa. \n" \
                                "No canto mais distante do aposento, há um colchão \n" \
                                "de palha. Você pode abrir a caixa (volte para 240) \n" \
                                "ou sair do aposento (volte para 363).\n"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 240
            self.n_trecho_b = 363
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 398:
            self.texto_trecho = "Você tateia pela parede rochosa no fim da passagem. \n" \
                                "Um pedaço de rocha se solta e revela uma pequena \n" \
                                "alavanca com um cabo na ponta. Você vai empurrá-la \n" \
                                "(volte para 364) ou puxá-la (volte para 12)?\n"
            self.tem_trecho_a = True
            self.tem_trecho_b = True
            self.n_trecho_a = 364
            self.n_trecho_b = 12
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"
            self.texto_trecho_b = f" vá para {self.n_trecho_b}"

        elif self.n_trecho == 399:
            self.texto_trecho = "A correnteza é forte e leva você rapidamente \n" \
                                "rio abaixo. Você é arrastado, passando através \n" \
                                "de uma abertura estreita que sai em uma caverna \n" \
                                "grande com margens em ambos os lados. \n" \
                                "A correnteza joga você direto para a margem sul. \n" \
                                "Volte para 218."
            self.tem_trecho_a = True
            self.n_trecho_a = 218
            self.texto_trecho_a = f" vá para {self.n_trecho_a}"

        elif self.n_trecho == 400:
            self.texto_trecho = "O Feiticeiro da Montanha de Fogo já não existe \n" \
                                "mais, e agora você é o dono das riquezas do Bruxo. \n" \
                                "pelo menos mil Peças de Ouro, além de jóias, \n" \
                                "diamantes, rubis e pérolas estão na arca. \n" \
                                "Escondido bem abaixo dessas coisas, você acha \n" \
                                "o livro de encantos do Feiticeiro e, ao folheá-lo,\n" \
                                " compreende que este compêndio é provavelmente \n" \
                                "mais valioso do que todo o tesouro. Nele são \n" \
                                "dadas instruções para controlar todos os segredos - e\n" \
                                " seres - da Montanha de Fogo. Com este livro você \n" \
                                "possui um poder ilimitado, e a segurança \n" \
                                "de seu retorno à vila está garantida. Ou, se \n" \
                                "você preferir, poderá permanecer por lá como senhor\n" \
                                " do domínio da Montanha de Fogo..."
