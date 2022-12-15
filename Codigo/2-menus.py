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
    count = 1

    menus = driver.find_elements(By.XPATH,"//ul[contains(@class,'main-menu cf')]/li/a/span")
    print("Encontramos " + str(len(menus)) + " elementos desplegables en el menu")
    for menu in menus:
        action.move_to_element(menu).perform()
        time.sleep(1)
        
        print("Elemento del menu "+str(count)+ " probado con exito")
        count += 1

        
    print("Prueba terminada en ")
    print("--- %s seconds ---" % (time.time() - start_time))


  


