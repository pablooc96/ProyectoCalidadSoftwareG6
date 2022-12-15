import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



if __name__ == '__main__':
    driver = uc.Chrome(version_main=107)
    action = ActionChains(driver)

    driver.get("https://www.mopt.go.cr/wps/portal/Home/inicio/!ut/p/z1/")

    driver.maximize_window()
    print("--- iniciando prueba ---")
    start_time = time.time()
    time.sleep(2)

    driver.find_element(By.ID, "google_translate_element").click()
    time.sleep(2)
    driver.switch_to.frame(0)

    select = "Árabe"

    idiomas = driver.find_elements(By.XPATH,"//td//a[@class='goog-te-menu2-item']")
    
    for idioma in idiomas:
        if(idioma.text == select):
            idioma.click()
    time.sleep(5)

    print("Se a cambiado al idioma "+ select + " con exito")

    
    time.sleep(5)
    print("Prueba terminada en ")
    print("--- %s seconds ---" % (time.time() - start_time))