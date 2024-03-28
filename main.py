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


campo_email = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "session_key")))
campo_email.send_keys(email)
campo_senha = navegador.find_element(By.ID, "session_password")
campo_senha.send_keys(senha)
campo_senha.submit()
time.sleep(5)

time.sleep(10)
busca =  WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-global-typeahead__input")))
busca.send_keys(profissao)
pyautogui.press("enter")
time.sleep(10)

campo_pessoas = navegador.find_element(By.CSS_SELECTOR, '[data-target-section-id="5O3aCjkkT2ehDubv1pCsnQ=="]')
campo_pessoas.click()
time.sleep(10)

