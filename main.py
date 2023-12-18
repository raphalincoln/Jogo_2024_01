import tkinter as tk
from tkinter import messagebox

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste de Matemática")

        self.opcao_avancar = tk.StringVar()
        self.opcao_avancar.set(None)

        self.criar_interface()

    def criar_interface(self):
        # Configuração dos radio buttons
        self.radio_avancar = tk.Radiobutton(self.root, text="Avançar", variable=self.opcao_avancar, value="Avancar", state=tk.DISABLED)
        self.radio_tentar_novamente = tk.Radiobutton(self.root, text="Tentar novamente", variable=self.opcao_avancar, value="TentarNovamente", state=tk.DISABLED)

        # Configuração do botão de teste
        self.botao_teste = tk.Button(self.root, text="Teste", command=self.realizar_teste)

        # Posicionamento dos elementos na janela
        self.radio_avancar.pack()
        self.radio_tentar_novamente.pack()
        self.botao_teste.pack()

    def realizar_teste(self):
        resposta = self.perguntar_usuario()

        if resposta == 2:  # 1 + 1 = 2
            messagebox.showinfo("Resultado", "Resposta correta! Avance para a próxima etapa.")
            self.radio_avancar.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Resultado", "Resposta incorreta. Tente novamente.")
            self.radio_tentar_novamente.config(state=tk.NORMAL)

    def perguntar_usuario(self):
        resposta = messagebox.askquestion("Pergunta", "Quanto é 1 + 1?")
        return 1 if resposta == "yes" else 0

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()
