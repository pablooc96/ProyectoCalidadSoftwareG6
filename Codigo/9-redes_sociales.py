import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium import webdriver


if __name__ == '__main__':
    driver = uc.Chrome(version_main=107)

    driver.get("https://www.mopt.go.cr/wps/portal/Home/inicio/!ut/p/z1/")

    driver.maximize_window()
    print("--- iniciando prueba ---")
    start_time = time.time()
    count = 1
    time.sleep(1)

    socials = driver.find_elements(By.XPATH,"//header/div[1]/div[1]/div[1]/div[2]/a")
    print("Encontramos " + str(len(socials)) + " enlaces a redes sociales")

    for social in socials:
        social.click()
        time.sleep(2)
        print("Boton "+str(count)+ " probado con exito")
        count += 1
    time.sleep(1)
    print("Todos los botones sociales han sido testeados con exito")
    print("Prueba terminada en ")
    print("--- %s seconds ---" % (time.time() - start_time))

