import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

if __name__ == '__main__':
    driver = uc.Chrome(version_main=107)
    action = ActionChains(driver)

    driver.get("https://www.mopt.go.cr/wps/portal/Home/inicio/!ut/p/z1/")

    driver.maximize_window()
    print("--- iniciando prueba ---")
    start_time = time.time()

    licencias = driver.find_element(By.XPATH,"//a[@href='http://www.educacionvial.go.cr/']")  
    action.move_to_element(licencias).perform()
    time.sleep(1)
    cita = driver.find_element(By.XPATH,"(//a[@target='_blank'])[20]")  
    action.move_to_element(cita).perform()
    cita.click()
    time.sleep(6)


    print("Prueba terminada en ")
    print("--- %s seconds ---" % (time.time() - start_time))


  


