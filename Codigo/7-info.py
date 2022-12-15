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
    time.sleep(1)
    

    info = driver.find_element(By.XPATH,"(//a[@href='#'])[4]")

    action.move_to_element(info).perform()

    audi = driver.find_element(By.XPATH,"//a[contains(.,'Auditoría General')]")


    audi.click()

    print("Redireccionando correctamente")

    
    time.sleep(4)
    print("Prueba terminada en ")
    print("--- %s seconds ---" % (time.time() - start_time))