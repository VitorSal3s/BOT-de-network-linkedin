from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#Para especificar qual vai ser o navegador que vamos usar
navegador = webdriver.Chrome()
#abrindo o site do LINKEDIN
navegador.get("https://www.linkedin.com/feed/")
time.sleep(2)

