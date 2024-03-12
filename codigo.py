# Passo a Passo do Projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

pyautogui.PAUSE = 1

# pyautogui.click -> clicar em algum lugar da tela 
# pyautogui.write -> escrever um texto 
# pyautogui.press -> pressionar 1 tecla do teclado

# pyautogui.hotkey("ctrl", "v")

# Abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no Site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior 
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=3398, y=470)
pyautogui.write("lucasvchaves22@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")

# clicar no botão de logar ou apertar enter, as duas dão certo
# pyautogui.press("enter")
pyautogui.click(x=3605, y=669)
time.sleep(3)

# Passo 3: Importar a base de dados
# pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
# pra cada linha da minha tabela

for linha in tabela.index:
    # clicar no primeiro campo
    # pyautogui.press("tab")
    pyautogui.click(x=3470, y=324)
    # codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

    # Passo 5: Repetir o processo de cadastro até acabar a base de dados