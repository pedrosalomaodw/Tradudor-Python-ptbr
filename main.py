#tradutor 
import customtkinter as tk
from googletrans import Translator
import pyperclip
import os 

os.system("cls")

root = tk.CTk()
root.geometry("350x420")
root.title("Python Tradutor para PT")
root.resizable(False, False)

lista = []
#font do programa
fonts = tk.CTkFont(size=15, family="Helvetica")
#comandos
def traduzir():
    #pegar texto
    texto_traduzir = caixa1.get(1.0, tk.END+"")    
    #traduzir texto
    tradutor = Translator()
    traduzindo =tradutor.translate(texto_traduzir, dest='pt')
    textos_traduzidos = traduzindo.text
    lista.append(textos_traduzidos)
    caixa2 = tk.CTkLabel(root, height=150, width=260, text=lista, bg_color="blue", fg_color="blue", font=fonts)
    caixa2.place(x=45, y=210)
    lista.remove(textos_traduzidos)
    #inserir texto

#caixa de receber o texto
caixa1 = tk.CTkTextbox(root, height=150, width=260, font=fonts)
caixa1.place(x=45, y=50)


traduzir_botao = tk.CTkButton(root, text="Traduzir", height=30, width=150, 
                            fg_color="#8354f7", command=traduzir)
traduzir_botao.place(x=100, y=380)

root.mainloop()