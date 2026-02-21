from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By


#Stworzenie instancji klasy Chrome
driver = Chrome()
driver.get("https://automationpractice.techwithjatin.com/")

class Sex:
    MALE = 0
    FEMALE = 1


DATA_EMAIL = "abcedef@spam.xo"
DATA_SEX = Sex.FEMALE

#maksymalizacja okna
driver.maximize_window()

#znajdz element sign in
sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")

#klikamy w element
sign_in_a.click()

driver.find_element(By.ID, "email_create").send_keys(DATA_EMAIL)
#klikamy "create account"
driver.find_element(By.ID, "SubmitCreate").click()

#czeka do 5 sekund na doładowanie elementów
driver.implicitly_wait(5)

#klikanie radiobuttona w zależności od płci
if DATA_SEX == Sex.FEMALE:
    driver.find_element(By.XPATH, '//label[@for="id_gender2"]').click()
else:
    driver.find_element(By.XPATH, '//label[@for="id_gender1"]').click()

sleep(5)

