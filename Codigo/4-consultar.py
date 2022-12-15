import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException



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
    cita = driver.find_element(By.XPATH,"(//a[@target='_blank'])[19]")  
    action.move_to_element(cita).perform()
    cita.click()
    driver.switch_to.window(driver.window_handles[1])
    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "identificacion")))

    identifacion = driver.find_element(By.ID, "identificacion").send_keys("675008000")

    send = driver.find_element(By.ID,"botonConsultar").click()


    try:
        print(WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "CM"))).text)
        
    except TimeoutException as ex:
        print(driver.find_element(By.ID, "Ajax").text)
    

    time.sleep(4)

    print("Prueba terminada en ")
    print("--- %s seconds ---" % (time.time() - start_time))


  


