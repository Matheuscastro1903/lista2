import pyautogui
import time
import pyperclip
import pandas as pd

# abre o arquivo csv excluindo a linha do cabeçalho
tabela = pd.read_csv("botwhatsapp.csv")


pyautogui.press("win")
time.sleep(0.5)
pyautogui.write("Whatsapp")
time.sleep(1)
pyautogui.press("Enter")
time.sleep(3)


for linha in tabela.index:
    # .loc[] é um método que permite acessar valores específicos no DataFrame.
    # "Acesse o valor da coluna 'nome' na linha com índice linha."
    nome = tabela.loc[linha, "nome"]
    # Procurando pelo nome do contato
    pyautogui.click(225,120)
    pyautogui.write(nome)
    time.sleep(2)
    pyautogui.click(222, 159)
    time.sleep(2)
    pyautogui.click(937, 1017)
    time.sleep(2)

    # ESSA AQUI SERIA A MENSAGEM PADRÃO ENVIADA PARA TODOS OS PACIENTES

    # pyautogui não funciona bem com acentos,então a melhor opção seria copiar e colar diretamente a mensagem

    # ESSA AQUI SERIA A MENSAGEM PADRÃO ENVIADA PARA TODOS OS PACIENTES
    mensagem = (f"Bom dia {nome}")

    pyperclip.copy(mensagem)  # Copia com todos os acentos certinho
    pyautogui.hotkey('ctrl', 'v')  # Cola no WhatsApp

    pyautogui.press("enter")
    time.sleep(2)
