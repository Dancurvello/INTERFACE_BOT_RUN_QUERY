import tkinter as tk
import pyautogui

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.execute_button = tk.Button(self, text="Executar", command=self.execute_bot)
        self.execute_button.pack(side="left")

        self.pause_button = tk.Button(self, text="Pausar", command=self.pause_bot)
        self.pause_button.pack(side="left")

        self.cancel_button = tk.Button(self, text="Cancelar", command=self.cancel_bot)
        self.cancel_button.pack(side="left")

    def execute_bot(self):
        # Coloque aqui o codigo que executa o bot
        # Exemplo:
        pyautogui.click(100, 100) # Clica na posicao (100, 100)

    def pause_bot(self):
        # Coloque aqui o codigo que pausa o bot
        # Exemplo:
        pyautogui.press('pause') # Pausa o bot usando a tecla "Pause"

    def cancel_bot(self):
        # Coloque aqui o codigo que cancela o bot
        # Exemplo:
        pyautogui.hotkey('ctrl', 'c') # Cancela o bot pressionando "Ctrl + C"

root = tk.Tk()
app = Application(master=root)
app.mainloop()