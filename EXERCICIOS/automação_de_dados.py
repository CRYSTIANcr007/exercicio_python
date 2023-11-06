from time import sleep
import pyautogui, pyperclip, pandas

pyautogui.PAUSE = 2
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=366, y=326, clicks=2)
time.sleep(3)
pyautogui.click(x=366, y=326)
pyautogui.click(x=1160, y=188)
pyautogui.click(x=1069, y=563)
tabela = pandas.read_excel(r'C:\Users\cryst\Downloads\Vendas - Dez.xlsx')
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
pyautogui.hotkey('ctrl', 't')
pyperclip.copy(r'https://mail.google.com/mail/u/0/?hl=pt-BR#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x=125, y=182)
pyperclip.copy('crystianrodrigues1309@gmail.com')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
pyautogui.write('Relatório de Vendas')
pyautogui.press('tab')
texto = f'''prezados, 
boa noite.
segue o relatório de vendas da empresa.
FATURAMENTO R${faturamento:,.2f}.
quantidade de produtos vendidos {quantidade}'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.click(x=984, y=684)
pyautogui.write('vendas')
pyautogui.click(x=363, y=430)
pyautogui.click(x=513, y=439)
time.sleep(5)
pyautogui.hotkey('ctrl', 'enter')