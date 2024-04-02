from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import time

#crucial para acessar a página do usuário as informações de login
#OBS: Nenhuma das informaçõe fornecdidas aqui será acessado por terceiros
def info_login():
    print("PRECCISAMOS DE SUAS INFORMAÇÕES DE LOGIN! ")
    email = str(input("DIGITE SEU EMAIL DE ACESSO: "))
    senha = str(input("DIGITE SUA SENHA: "))

    return email, senha

profissao = input("POR QUAL PROFISSÃO VOCÊ BUSCAR AUMENTAR SUA REDE: ")
email, senha = info_login()
#Para especificar qual vai ser o navegador que vamos usar
navegador = webdriver.Chrome()

navegador.maximize_window()
#abrindo o site do LINKEDIN
navegador.get("https://www.linkedin.com/home")
time.sleep(2)

#logando com as informações de usuário
campo_email = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "session_key")))
campo_email.send_keys(email)
campo_senha = navegador.find_element(By.ID, "session_password")
campo_senha.send_keys(senha)
campo_senha.submit()
time.sleep(5)

#indo para a área de pessoas para se conectar 
time.sleep(5)
busca_pessoas = navegador.get(f"https://www.linkedin.com/search/results/people/?keywords={profissao}&origin=SWITCH_SEARCH_VERTICAL&sid=8)k")
time.sleep(5)

