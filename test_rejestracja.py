from selenium.webdriver.common.by import By
from selenium import webdriver
from datatools import TestData
from datatools import Gender
from time import sleep
import unittest
from selenium.webdriver.support.select import Select


class RegisterNewUserTest(unittest.TestCase):
    def setUp(self):
        #warunki wstępne:
        #1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationpractice.techwithjatin.com/")
        self.driver.implicitly_wait(10)
        #2. Użytkownik niezalogowany
        # opcjonalnie można sprawdzić ale nie trzeba bo on i tak jest niezalogowany po otworzenius strony

    def test_password_too_short(self):
        # Kroki:
        # 1. kliknij sign in
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()
        # czekam, usunę po napisaniu testu
        # sleep(2)
        # 2. Wpisz email
        self.driver.find_element(By.ID, "email_create").send_keys(TestData.EMAIL)
        # 3. kliknij create account
        self.driver.find_element(By.ID, "SubmitCreate").click()
        # czekamy na załadowanie formularza
        # self.driver.implicitly_wait(5)
        # 4. kliknij plec
        if TestData.GENDER == Gender.FEMALE:
            self.driver.find_element(By.XPATH, '//label[@for="id_gender2"]').click()
        else:
            self.driver.find_element(By.XPATH, '//label[@for="id_gender1"]').click()
        # wyłączamy czekanie
        # self.driver.implicitly_wait(0)
        #5a. - wpisz imie
        self.driver.find_element(By.XPATH, '//*[@id="customer_firstname"]').send_keys(TestData.FIRST_NAME)
        # 5b. - wpisz nazwisko
        self.driver.find_element(By.XPATH, '//*[@id="customer_lastname"]').send_keys(TestData.LAST_NAME)
        # 6. porównanie
        email_input = self.driver.find_element(By.ID, "email")
        email_actual = email_input.get_attribute("value")
        self.assertEqual(TestData.EMAIL, email_actual)

        # 7.hasło
        self.driver.find_element(By.XPATH, '//*[@id="passwd"]').send_keys(TestData.PASSWORD)

        # 8. data urodzenia
        days = Select(self.driver.find_element(By.ID, "days"))
        days.select_by_value(TestData.BIRTH_DAY)

        months = Select(self.driver.find_element(By.ID, "months"))
        months.select_by_value(TestData.BIRTH_MONTH)

        years = Select(self.driver.find_element(By.ID, "years"))
        years.select_by_value(TestData.BIRTH_YEAR)

        # 8. register button
        self.driver.find_element(By.ID, "submitAccount").click()


        ##### UWAGA, TUTAJ BĘDZIE TEST !!!!!!!
        no_of_errors_message = self.driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p[1]')

        print(no_of_errors_message.text)
        self.assertEqual("There is 1 error", no_of_errors_message.text)

        sleep(2)
        errors_list = self.driver.find_elements(By.XPATH, '//div[@class="alert alert-danger"]/ol/li')
        self.assertEqual(1, len(errors_list))
        self.assertEqual("passwd is invalid.", errors_list[0].text)





    @unittest.skip("skipping test_no_name_in_registration")
    def test_no_name_in_registration_form(self):
        # Kroki:
        # 1. kliknij sign in
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()
        # czekam, usunę po napisaniu testu
        #sleep(2)
        # 2. Wpisz email
        self.driver.find_element(By.ID, "email_create").send_keys(TestData.EMAIL)
        # 3. kliknij create account
        self.driver.find_element(By.ID, "SubmitCreate").click()
        # czekamy na załadowanie formularza
        #self.driver.implicitly_wait(5)
        # 4. kliknij plec
        if TestData.GENDER == Gender.FEMALE:
            self.driver.find_element(By.XPATH, '//label[@for="id_gender2"]').click()
        else:
            self.driver.find_element(By.XPATH, '//label[@for="id_gender1"]').click()
        # wyłączamy czekanie
        #self.driver.implicitly_wait(0)
        # # 5a. - wpisz imie
        # self.driver.find_element(By.XPATH, '//*[@id="customer_firstname"]').send_keys(TestData.FIRST_NAME)
        # 5b. - wpisz nazwisko
        self.driver.find_element(By.XPATH, '//*[@id="customer_lastname"]').send_keys(TestData.LAST_NAME)
        # 6. porównanie
        email_input = self.driver.find_element(By.ID, "email")
        email_actual = email_input.get_attribute("value")
        self.assertEqual(TestData.EMAIL, email_actual)


        #7.hasło
        self.driver.find_element(By.XPATH, '//*[@id="passwd"]').send_keys(TestData.PASSWORD)

        #8. data urodzenia
        days = Select(self.driver.find_element(By.ID, "days"))
        days.select_by_value(TestData.BIRTH_DAY)

        months = Select(self.driver.find_element(By.ID, "months"))
        months.select_by_value(TestData.BIRTH_MONTH)

        years = Select(self.driver.find_element(By.ID, "years"))
        years.select_by_value(TestData.BIRTH_YEAR)

        #8. register button
        self.driver.find_element(By.ID, "submitAccount").click()



        ##### UWAGA, TUTAJ BĘDZIE TEST !!!!!!!
        no_of_errors_message = self.driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p[1]')

        print(no_of_errors_message.text)
        self.assertEqual("There is 1 error", no_of_errors_message.text)

        sleep(5)


    def tearDown(self):
        self.driver.quit()

