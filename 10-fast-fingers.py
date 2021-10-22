from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Navegando até a URL
driver.get("https://10fastfingers.com/typing-test/portuguese")


# Espera janela dos cookies
WebDriverWait(driver,timeout=10).until(lambda d: d.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
# Permitindo todos os cookies
driver.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()


# Fecha banner de anúncio
WebDriverWait(driver,timeout=30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[10]/div/button")))
driver.find_element(By.XPATH,"/html/body/div[10]/div/button").click()

# Fechando vídeo de anúncio
WebDriverWait(driver,timeout=30).until(lambda d: d.find_element(By.ID,"closeIcon"))
driver.find_element(By.ID,"closeIcon").click()

# Capturando elementos das palavras
palavras = driver.find_elements(By.XPATH,"//*[@id='row1']/span")

# Área de digitação
textinput = driver.find_element(By.XPATH,"/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[2]/div/div[1]/input")

# Iterando sobre elementos das palavras
for elemento in palavras:
    # Capturando palavra
    palavra = elemento.text

    # Inserindo palavra e apertando barra de espaço
    textinput.send_keys(palavra + Keys.SPACE)

