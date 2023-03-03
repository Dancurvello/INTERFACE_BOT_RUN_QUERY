import pyautogui
import time



pyautogui.press("win")
time.sleep(1)
pyautogui.write("Any desk")
time.sleep(1)
pyautogui.press("enter") #Abrindo o Ndesk
time.sleep(3)
pyautogui.click(x=219, y=969, clicks=2) #Abrindo o desktop remotamente
time.sleep(10)
pyautogui.click(x=509, y=208, clicks=2) #Abrindo o IBM data studio
time.sleep(12)
pyautogui.click(x=1051, y=620) #cancelando a homologacao
time.sleep(6)
pyautogui.click(x=316, y=207) #Clicando em arquivo
time.sleep(1)
pyautogui.click(x=361, y=533) #indo alterar o workspace
time.sleep(1)
pyautogui.click(x=668, y=531) #Clicando em alterar workspace
time.sleep(15)
pyautogui.click(x=466, y=401, clicks=2) #Abrindo pasta1
time.sleep(2)
pyautogui.press('down') #Descendo para primeira SQL
time.sleep(2)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=801, y=290) #Abrindo o seletor da localizacao do banco de dados
time.sleep(3)
pyautogui.click(x=709, y=361) #Selecionando RJ
time.sleep(2)
pyautogui.press("enter")











