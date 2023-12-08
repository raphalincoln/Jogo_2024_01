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

   def livro(self):
       if self.n_trecho == 1:
           self.texto_trecho = "Texto do trecho 001\n" \
                               "voce pode ir para o trecho 2 ou para o trecho 6 ou trecho 7"
           self.n_trecho_a = 2
           self.n_trecho_b = 6
           self.n_trecho_c = 7
           self.tem_trecho_a = True
           self.tem_trecho_b = True
           self.tem_trecho_c = True
           self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
           self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"
           self.texto_trecho_c = f"Ir para {self.n_trecho_c}?"

       elif self.n_trecho == 2:
           self.texto_trecho = "Texto do trecho 002\n" \
                               "voce pode ir para o trecho 3 ou para o trecho 6"
           self.n_trecho_a = 3
           self.n_trecho_b = 6
           self.tem_trecho_a = True
           self.tem_trecho_b = True
           self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
           self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"

       elif self.n_trecho == 3:
           self.texto_trecho = "Texto do trecho 003\n" \
                               "voce pode ir para o trecho 4 ou para o trecho 5"
           self.n_trecho_a = 4
           self.n_trecho_b = 5
           self.tem_trecho_a = True
           self.tem_trecho_b = True
           self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
           self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"

       elif self.n_trecho == 4:
           self.texto_trecho = "Texto do trecho 004\n" \
                               "voce pode ir para o trecho 7 ou para o trecho 8"
           self.n_trecho_a = 7
           self.n_trecho_b = 8
           self.tem_trecho_a = True
           self.tem_trecho_b = True
           self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
           self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"

       elif self.n_trecho == 5:
           self.texto_trecho = "Texto do trecho 005\n" \
                               "voce pode ir para o trecho 10 ou para o trecho 9"
           self.n_trecho_a = 10
           self.n_trecho_b = 9
           self.tem_trecho_a = True
           self.tem_trecho_b = True
           self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
           self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"

       elif self.n_trecho == 6:
           self.temluta = True
           self.m_nome = "Demon"
           self.m_energia = 9
           self.m_habilidade = 9
           self.n_trecho_a = 3
           self.n_trecho_b = 4
           self.n_trecho_c = 9
           self.tem_trecho_a = True
           self.tem_trecho_b = True
           self.tem_trecho_c = True
           self.texto_trecho = "Texto do trecho 006\n" \
                               f"Você fez muito barulho e {self.m_nome} despertou.\n"
           self.texto_trecho_a = f"Se vencer, vá para {self.n_trecho_a}?"
           self.texto_trecho_b = f"Se morrer, vá para {self.n_trecho_b}?"

       elif self.n_trecho == 7:
           self.texto_trecho = "Voce Encontrou uma Espada!\n" \
                                "Pegue-a\n"\
                               "voce pode ir para o trecho 8 ou para o trecho 4"
           self.tem_item = True
           self.item = "Espada"
           self.n_trecho_a = 8
           self.n_trecho_b = 4
           self.tem_trecho_a = True
           self.tem_trecho_b = True

           self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
           self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"

       elif self.n_trecho == 8:
           self.texto_trecho = "Texto do trecho 008\n" \
                               "voce pode ir para o trecho 5 ou para o trecho 9"
           self.n_trecho_a = 5
           self.n_trecho_b = 9
           self.tem_trecho_a = True
           self.tem_trecho_b = True
           self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
           self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"

       elif self.n_trecho == 9:
           self.texto_trecho = "Texto do trecho 009\n" \
                               "voce pode ir para o trecho 6 ou para o trecho 10"
           self.n_trecho_a = 6
           self.n_trecho_b = 10
           self.tem_trecho_a = True
           self.tem_trecho_b = True
           self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
           self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"

       elif self.n_trecho == 10:
           self.texto_trecho = "Texto do trecho 010\n" \
                               "voce pode ir para o trecho 4 ou para o trecho 6"
           self.n_trecho_a = 4
           self.n_trecho_b = 6
           self.tem_trecho_a = True
           self.tem_trecho_b = True
           self.texto_trecho_a = f"Ir para {self.n_trecho_a}?"
           self.texto_trecho_b = f"Ir para {self.n_trecho_b}?"
