import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


if __name__ == '__main__':
    driver = uc.Chrome(version_main=107)

    driver.get("https://www.mopt.go.cr/wps/portal/Home/inicio/!ut/p/z1/")

    driver.maximize_window()
    print("--- iniciando prueba ---")
    start_time = time.time()

    time.sleep(1)

    search = driver.find_element(By.XPATH,"//input[contains(@id,'gsc-i-id1')]")
    keyword = "carros"
    print("buscando la palabra:" + keyword)
    search.send_keys(keyword, Keys.RETURN)
    
    time.sleep(2)
    print("Prueba terminada en ")
    print("--- %s seconds ---" % (time.time() - start_time))
