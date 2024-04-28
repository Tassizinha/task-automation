  
  #Passo a passo

#1 - Entrar no sistema da empresa  
  #https://dlp.hashtagtreinamentos.com/python/intensivao/login   
#2 - Fazer login
#3 - Importar a base de dados
#4 - Cadastrar um produto
#5 - Repetir isso até acabar a base de dados

import pyautogui 
import time

pyautogui.PAUSE = 1 #tempo da automação

#1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

acesso = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #variavel 
pyautogui.write(acesso) #acessando o link da variavel 
pyautogui.press("enter")

time.sleep(2)

#2
pyautogui.click(x=664, y=368)
email = "fireday34@gmail.com"
pyautogui.write(email)
pyautogui.press("tab")
senha = "fire2424"
pyautogui.write(senha)

pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)


#3
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    #4
    pyautogui.click(x=576, y=258)

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
            pyautogui.write(obs)
    #pyautogui.press("tab")

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

    
    #pyautogui.press("tab")
    #pyautogui.press("enter")






