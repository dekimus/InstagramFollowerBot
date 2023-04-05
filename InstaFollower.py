from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

import time


class InstaFollower:
    def __init__(self) -> None:
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.option, service=Service(executable_path="c:\webdriver\chromedriver.exe", log_path="NUL"))

    def login(self, user, paswwd):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text()='Permitir solo cookies necesarias']").click()
        time.sleep(1)
        user_text = self.driver.find_element(By.NAME, "username")
        user_text.send_keys(user)
        passw = self.driver.find_element(By.NAME, "password")
        passw.send_keys(paswwd)
        passw.send_keys(Keys.ENTER)
        time.sleep(5)
        

    def find_followers(self,sm):
        self.driver.get(f"https://www.instagram.com/{sm}/")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(5)
        scrollable_popup = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(2)
    def follow(self):
        buttons = self.driver.find_elements(By.XPATH, "//*[text()='Seguir']")
        print(buttons)
        for b in buttons:
           try:
                b.click()
           except ElementClickInterceptedException:
               self.driver.find_element(By.XPATH, "//*[text()='Cancel']").click()
           time.sleep(1)
        time.sleep(10)