from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome = webdriver.Chrome()





class Login(unittest.TestCase):


    def login(self, user, parola):
        chrome.find_element(By.ID, "username").send_keys("user")
        chrome.find_element(By.NAME, "password").send_keys("parola")
        chrome.find_element(By.CLASS_NAME, "radius").click()

    def setUp(self):
        chrome.get("https://the-internet.herokuapp.com/login")



    def tearDown(self):
        chrome.quit()

### Test_1
    def test_new_url_is_correct(self):
        actual_url = chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        self.assertEqual(expected_url, actual_url, "URL is incorrect")


### Test_2
    def test_page_tile_corect(self):
        actual = chrome.find_element(By.XPATH, '//*[@id="content"]/div/h2').text
        expected = "Login Page"

        self.assertEqual(actual, expected, "testul nu trece")

### Test_3
    def test_text_corect(self):
        text = chrome.find_element(By.XPATH, "//h2[text()='Login Page']")

### Test_4
    def test_login_displayed(self):
        actual = chrome.find_element(By.CLASS_NAME, "radius").text
        expected = "Login"

        self.assertEqual(actual, expected, "testul nu trece")

### Test_5
    def test_elemental_selenium(self):
        actual = chrome.find_element(By.LINK_TEXT, "Elemental Selenium").get_attribute("href")
        expected = "http://elementalselenium.com/"
        self.assertEqual(actual, expected, "nu se potrivesc")

### Test_6
    def test_login_eroare(self):
        chrome.find_element(By.ID, "username").send_keys()
        chrome.find_element(By.ID, "password").send_keys()
        chrome.find_element(By.CLASS_NAME, "radius").click()
        assert "Your username is invalid!" in chrome.page_source

### Test_7
    def test_login_invalide(self):
        chrome.find_element(By.ID, "username").send_keys("alabala")
        chrome.find_element(By.ID, "password").send_keys("alabala")
        chrome.find_element(By.CLASS_NAME, "radius").click()
        actual = chrome.find_element(By.ID, "flash").text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

### Test_8
    def test_login_x_eroare(self):
        chrome.set_window_size(1920,1080)
        chrome.find_element(By.ID, "username").send_keys()
        chrome.find_element(By.ID, "password").send_keys()
        chrome.find_element(By.CLASS_NAME, "radius").click()
        chrome.find_element(By.CLASS_NAME, "close").click()
        assert "Your username is invalid!" in chrome.page_source

### Test_9 ???????????????????????????????????????????????????
    def test_lista_label(self):
        labels = ['username', 'password']
        actual = chrome.find_element(By.CSS_SELECTOR, 'div label[for*="username"]').text
        expected = "Username"
        self.assertEqual(actual, expected, "nu se potrivesc")
        actual = chrome.find_element(By.CSS_SELECTOR, 'div label[for*="password"]').text
        expected = "Password"
        self.assertEqual(actual, expected, "nu se potrivesc")
        sleep(4)



### Test_10
    def test_login_corecte(self):
        chrome.find_element(By.ID, "username").send_keys("tomsmith")
        chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        chrome.find_element(By.CLASS_NAME, "radius").click()
        assert "secure" in chrome.page_source
        flash = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "flash success")))
        element = chrome.find_element(By.CLASS_NAME, "flash success").is_displayed()
        actual = chrome.find_element(By.ID, "flash").text
        expected = "secure area!"
        self.assertEqual(actual, expected, "nu se potrivesc")

### Test_11
    def test_log_out(self):
        chrome.find_element(By.ID, "username").send_keys("tomsmith")
        chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        chrome.find_element(By.CLASS_NAME, "radius").click()
        chrome.find_element(By.LINK_TEXT, "Logout").click()
        actual = chrome.current_url
        expected = "https://the-internet.herokuapp.com/login"
        self.assertEqual(expected, actual, "URL is incorrect")











