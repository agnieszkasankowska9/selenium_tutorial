from selenium.webdriver.common.by import By
from selenium import webdriver
from datatools import TestData
from datatools import Gender
from time import sleep
import unittest


class RegisterNewUserTest(unittest.TestCase):
    def setUp(self):
        #warunki wstępne:
        #1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationpractice.techwithjatin.com/")
        #2. Użytkownik niezalogowany
        # opcjonalnie można sprawdzić ale nie trzeba bo on i tak jest niezalogowany po otworzenius strony
    def test_no_name_in_registration_form(self):
        # Kroki:
        # 1. kliknij sign in
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()
        # czekam, usunę po napisaniu testu
        sleep(2)
        # 2. Wpisz email
        self.driver.find_element(By.ID, "email_create").send_keys(TestData.EMAIL)
        # 3. kliknij create account
        self.driver.find_element(By.ID, "SubmitCreate").click()
        # czekamy na załadowanie formularza
        self.driver.implicitly_wait(5)
        # 4. kliknij plec
        if TestData.GENDER == Gender.FEMALE:
            self.driver.find_element(By.XPATH, '//label[@for="id_gender2"]').click()
        else:
            self.driver.find_element(By.XPATH, '//label[@for="id_gender1"]').click()
        # wyłączamy czekanie
        self.driver.implicitly_wait(0)






    def tearDown(self):
        self.driver.quit()

