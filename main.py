from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By


#Stworzenie instancji klasy Chrome
driver = Chrome()
driver.get("https://automationpractice.techwithjatin.com/")

DATA_EMAIL = "abcedef@spam.xo"

#maksymalizacja okna
driver.maximize_window()

#znajdz element sign in
sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")

#klikamy w element
sign_in_a.click()

driver.find_element(By.ID, "email_create").send_keys(DATA_EMAIL)


sleep(5)

