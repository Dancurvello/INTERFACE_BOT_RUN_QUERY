import pyautogui
import time
from tkinter import *

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
        pyautogui.press("win")
        time.sleep(1)
        pyautogui.write("Any desk")
        time.sleep(1)
        pyautogui.press("enter") #Abrindo o Ndesk
        time.sleep(3)
        pyautogui.click(x=219, y=969, clicks=2) #Abrindo o desktop remotamente
        time.sleep(20)
        pyautogui.click(x=509, y=208, clicks=2) #Abrindo o IBM data studio
        time.sleep(12)
        pyautogui.click(x=316, y=207) #Clicando em arquivo
        time.sleep(1)
        pyautogui.click(x=361, y=533) #indo alterar o workspace
        time.sleep(1)
        pyautogui.click(x=668, y=531) #Clicando em alterar workspace
        time.sleep(25)
        pyautogui.click(x=399, y=425, clicks=2) #Abrindo pasta1
        time.sleep(2)
        pyautogui.press('down') #Descendo para primeira SQL da pasta 1
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(5)
        executa_sql()        
        pyautogui.click(x=270, y=1348, clicks=2) #Descendo para a segunda SQL da pasta 1  
        executa_sql()
        pyautogui.click(x=443, y=454, clicks=2) #descendo para a terceira SQL
        executa_sql()
        pyautogui.click(x=448, y=471, clicks=2) #descendo para a quarta SQL
        executa_sql()
        pyautogui.click(x=448, y=489, clicks=2) #descendo para a quinta SQL
        executa_sql()
        pyautogui.click(x=448, y=506, clicks=2) #descendo para a sexta SQL
        executa_sql()
        pyautogui.click(x=448, y=520, clicks=2) #descendo para a setima SQL
        executa_sql()
        pyautogui.click(x=448, y=537, clicks=2) #descendo para a oitava SQL
        executa_sql()


                
        texto_feedback.configure(text="O bot terminou a execucao.")
    else:
        texto_feedback.configure(text="O bot foi cancelado.")

#Definindo funcao de cancelamento do bot
def cancelar_bot():
    global bot_em_execucao
    bot_em_execucao = False
    texto_feedback.configure(text="O bot foi cancelado.")


#funcao que seleciona e executa os 2 bancos de dados RJ e SP (a query tem que estar aberta)
def executa_sql():
        pyautogui.click(x=801, y=290) #Abrindo o seletor da localizacao do banco de dados
        time.sleep(3)
        pyautogui.click(x=709, y=361) #Selecionando RJ
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)
        #pyautogui.click(x=1039, y=1244) EXECUTAR
        time.sleep(2) #aumentar esse tempo depois quando for executar mesmo
        pyautogui.click(x=1057, y=356) #Abrindo o seletor da localizacao do banco de dados
        time.sleep(3)
        pyautogui.click(x=709, y=381) #Selecionando SP        
        time.sleep(2)
        pyautogui.press("enter")
        #pyautogui.click(x=1039, y=1244) #Executar
        time.sleep(2) #aumentar esse tempo depois quando for executar mesmo

     








#Interface do bot

janela = Tk()
janela.title("Bot PASTA 1 e Pasta 2 - Manha")
janela.geometry("600x200")

texto_orientacao = Label(janela, text="Bot que executa todas as queries da Pasta 1 (manha)")
texto_orientacao.grid(column=0, row=0, padx=0, pady=0)

botao = Button(janela, text="Executar", command=text_executing)
botao.grid(column=0, row=4, padx=0, pady=40)

botao_cancelar = Button(janela, text="Parar", command=cancelar_bot)
botao_cancelar.grid(column=1, row=4, padx=0, pady=40)

texto_feedback = Label(janela)
texto_feedback.grid(column=0, row=10, padx=0, pady=0)

janela.mainloop()



