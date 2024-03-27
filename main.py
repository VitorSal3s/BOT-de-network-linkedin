from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#crucial para acessar a página do usuário as informações de login
#OBS: Nenhuma das informaçõe fornecdidaas aqui será acessado por terceiros
def info_login():
    login = str(input("Você já está logado no site? [s/n]"))
    if login == "n" or "N":
        email = str(input("DIGITE SEU EMAIL DE ACESSO: "))
        senha = str(input("DIGITE SUA SENHA: "))
    return email, senha
#Para especificar qual vai ser o navegador que vamos usar
navegador = webdriver.Chrome()
#abrindo o site do LINKEDIN
navegador.get("https://www.linkedin.com/feed/")
time.sleep(2)

