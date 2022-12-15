import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


if __name__ == '__main__':
    driver = uc.Chrome(version_main=107)
    action = ActionChains(driver)

    driver.get("https://www.mopt.go.cr/wps/portal/Home/inicio/!ut/p/z1/")

    driver.maximize_window()
    print("--- iniciando prueba ---")
    start_time = time.time()
    time.sleep(2)

    elements = driver.find_elements(By.XPATH, "//div[@class='tp-bullets  horizontal noSwipe']//div")
    count = 1
    for element in elements:
        element.click()
        time.sleep(3)
        ver_mas = driver.find_element(By.XPATH, "//ul//li[" + str(count) +"]//a//div[@class='tp-mask-wrap']//parent::div//parent::div//parent::a//parent::li")
        visiby = ver_mas.value_of_css_property("visibility")
        if(visiby == "visible"):
            print("El boton ver mas del elemento "+ str(count) +" es visible")
        else:
            print("El boton ver mas del elemento "+ str(count) +" no es visible")

        count += 1

        
    wait = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, "//ul//li[1]//a//div[@class='tp-mask-wrap']//parent::div//parent::div//parent::a//parent::li")))


    print("Prueba terminada en ")
    print("--- %s seconds ---" % (time.time() - start_time))
        