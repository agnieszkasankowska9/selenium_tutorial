from selenium.webdriver import Chrome
from time import sleep


#Stworzenie instancji klasy Chrome
driver = Chrome()
driver.get("https://www.kozminski.edu.pl")

#maksymalizacja okna
driver.maximize_window()
sleep(5)