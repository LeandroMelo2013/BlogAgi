from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configurar o caminho do driver
chrome_driver_path = "/Users/user/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# URL do site
url = "https://blogdoagi.com.br/"
driver.get(url)

# Encontrar o campo de pesquisa e enviar a consulta
search_open = driver.find_element("Pesquisar")
search_query = "Sua consulta de pesquisa"
search_open.send_keys(search_query)
search_open.send_keys(Keys.RETURN)

# Aguardar um pouco para a página carregar os resultados
time.sleep(3)

# Realizar ações adicionais, se necessário
# ...

# Fechar o navegador
driver.quit()
