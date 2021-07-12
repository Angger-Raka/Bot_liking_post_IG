from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome("C:/Users/HOME/Documents/chromedriver/chromedriver.exe")

        self.username = username
        self.password = password

        self.browser.delete_all_cookies()
        self.browser.maximize_window()

    def wait_for_object(self, type, string):
        return WebDriverWait(self.browser, 3).until(ec.presence_of_element_located((type, string)))

    def wait_for_objects(self, type, string):
        return WebDriverWait(self.browser, 3).until(ec.presence_of_all_elements_located((type, string)))

    def login(self):
        self.browser.get("https://www.instagram.com")


        inputs = self.wait_for_objects(By.CSS_SELECTOR, '._2hvTZ.pexuQ.zyHYP')
        inputs[0].send_keys(self.username)
        inputs[1].send_keys(self.password)

        time.sleep(1)

        inputs[1].send_keys(Keys.ENTER)

        time.sleep(2)

    def like_hashtag(self, hashtag, number_of_likes):
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{hashtag}/")

        pictures = self.wait_for_objects(By.CSS_SELECTOR, '._9AhH0')
        pictures[0].click()

        ulang = 300

        for a in range(ulang):
            next_window = self.wait_for_object(By.CSS_SELECTOR, '._65Bje.coreSpriteRightPaginationArrow')
            next_window.click()
            time.sleep(1)
            

        for i in range(0, number_of_likes):
            likes = self.wait_for_objects(By.CSS_SELECTOR, 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
            likes[0].click()

            time.sleep(2)

            next_window = self.wait_for_object(By.CSS_SELECTOR, '._65Bje.coreSpriteRightPaginationArrow')
            next_window.click()

            time.sleep(random.randint(3, 13))
        self.browser.get("https://www.instagram.com")        
    

bot = InstagramBot(username="username", password="password")
bot.login()
bot.like_hashtag('gameconsign', 10)
