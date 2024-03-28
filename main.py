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
    login = str(input("Você já está logado no site? [s/n]"))
    if login == "n" or "N":
        email = str(input("DIGITE SEU EMAIL DE ACESSO: "))
        senha = str(input("DIGITE SUA SENHA: "))
    else:
        return none,none
    return email, senha

email, senha = info_login()
#Para especificar qual vai ser o navegador que vamos usar
navegador = webdriver.Chrome()
#abrindo o site do LINKEDIN
navegador.get("https://www.linkedin.com/home")
time.sleep(2)

#O código usa espera explícita para aguardar a presença de um elemento com o ID "session_key" na página. Isso é útil para testes automatizados, garantindo que os elementos necessários estejam disponíveis antes das interações. Ele cria uma instância de WebDriverWait, aguarda até que o elemento esteja presente e, em seguida, permite interações adicionais com o elemento encontrado.
campo_email = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.ID, "session_key"))
)
campo_email.send_keys(email)

campo_senha = navegador.find_element(By.ID, "session_password")
campo_senha.send_keys(senha)
pyautogui.press("enter")


time.sleep(5)
