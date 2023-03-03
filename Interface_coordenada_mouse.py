import pyautogui
from tkinter import *
import time

#Definindo variavel global para controle do bot
bot_em_execucao = False

#Definindo funcao de coordenada do mouse
def text_executing():
    global bot_em_execucao
    bot_em_execucao = True
    texto_feedback.configure(text="O bot vai iniciar em 3 segundos")
    janela.after(3000, execute_coordinates_mouse)
    
def execute_coordinates_mouse():
    global bot_em_execucao
    if bot_em_execucao:
        print(pyautogui.position())
        texto_feedback.configure(text="O bot terminou a execucao.")
    else:
        texto_feedback.configure(text="O bot foi cancelado.")

#Definindo funcao de cancelamento do bot
def cancelar_bot():
    global bot_em_execucao
    bot_em_execucao = False
    texto_feedback.configure(text="O bot foi cancelado.")

janela = Tk()
janela.title("Bot PASTA 1 - Manha")
janela.geometry("400x130")

texto_orientacao = Label(janela, text="Bot que executa todas as queries da Pasta 1 (manha)")
texto_orientacao.grid(column=1, row=1, padx=1, pady=10)

botao = Button(janela, text="Executar", command=text_executing)
botao.grid(column=1, row=4, padx=2, pady=10)

botao_cancelar = Button(janela, text="Parar", command=cancelar_bot)
botao_cancelar.grid(column=2, row=4, padx=10, pady=10)

texto_feedback = Label(janela)
texto_feedback.grid(column=1, row=10)

janela.mainloop()