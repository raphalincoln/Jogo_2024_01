import os
import tkinter as tk
from PIL import Image, ImageTk

def exibir_imagem():
    # Especifique o diretório que contém suas imagens
    diretorio = "C:\\Users\\rlreis1\\OneDrive - Stefanini\\Documents\\GitHub\\Projeto_2024_1"

    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Criar uma janela
    janela = tk.Tk()
    janela.title("Exemplo de Exibição de Imagens")

    for arquivo in arquivos:
        # Verificar se o arquivo é uma imagem (pode ajustar para suportar outros formatos)
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Caminho completo para a imagem
            caminho_imagem = os.path.join(diretorio, arquivo)

            # Carregar a imagem
            imagem = Image.open(caminho_imagem)

            # Converter a imagem para o formato Tkinter
            imagem_tk = ImageTk.PhotoImage(imagem)

            # Criar um widget Label para exibir a imagem
            label_imagem = tk.Label(janela, image=imagem_tk)
            label_imagem.pack()

    # Iniciar o loop principal da interface gráfica
    janela.mainloop()

# Chamar a função para exibir as imagens no diretório
exibir_imagem()