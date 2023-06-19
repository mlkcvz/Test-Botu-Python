from selenium import webdriver
from user import email,password
from selenium.webdriver.common.keys import Keys
import time


class TrendyolKullaniciKayitGiris:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def negatifLogin(self):
        self.browser.get("https://www.trendyol.com/butik/liste/1/kadin")  
        time.sleep(3)
        self.browser.find_element_by_class_name("link-text").click()
        time.sleep(2)
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='login-register']/div[3]/div[1]/form/button").click()  
        time.sleep(2)  


    def positiveLogin(self,email,password):
        while True:
          if self.browser.find_element_by_class_name("message").text=="Lütfen geçerli bir e-posta adresi giriniz.":

            girisEmail = self.browser.find_element_by_id("login-email")
            girisEmail.click()
            time.sleep(2)
            girisEmail.send_keys(email)
            time.sleep(2)
            girisSifre = self.browser.find_element_by_name("login-password")
            girisSifre.click()
            time.sleep(2)
            girisSifre.send_keys(password)
            time.sleep(2)
            self.browser.find_element_by_xpath("//*[@id='login-register']/div[3]/div[1]/form/button").click()  
            time.sleep(2)
          else:
              break



    def negatifUserRegistration(self):
        
        self.browser.find_element_by_xpath("//*[@id='login-register']/div[2]/div/button[2]/span").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='login-register']/div[3]/div[1]/form/button").click()
        time.sleep(2)

  
    def positiveUserRegistration(self,email,password):
        email_ = self.browser.find_element_by_id("register-email")
        email_.click()
        time.sleep(2)
        email_.send_keys(email)
        time.sleep(2)
        sifre = self.browser.find_element_by_name("register-password")
        sifre.click()
        sifre.send_keys(password)
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='login-register']/div[3]/div[1]/form/div[3]/div/button[1]/span").click()
        time.sleep(2)
        action = webdriver.ActionChains(self.browser) ##ActionChains-browsera space tuşu vermek için 
        self.browser.find_element_by_id("container").click()
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(2)
        self.browser.find_element_by_class_name("special-text").click()
        time.sleep(2)
        self.browser.find_element_by_id("contracts").click()
        time.sleep(2)
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        self.browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/i").click()
        time.sleep(2)
        self.browser.find_element_by_name("personal-data-error").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='login-register']/div[3]/div[1]/form/button").click()
        time.sleep(2)


    def search(self):
        time.sleep(2)
        searchCurser=self.browser.find_element_by_class_name("search-box")
        time.sleep(1)
        searchCurser.click()
        time.sleep(2)
        searchCurser.send_keys("Topuklu ayakkabı")
        time.sleep(2)
        searchCurser.send_keys(Keys.ENTER)
        time.sleep(2) 
    
    def sepet(self):
      self.browser.get("https://www.trendyol.com/sr?mid=2520")
      time.sleep(2)
      self.browser.find_element_by_xpath("//*[@id='account-navigation-container']/div/div[1]/div[1]/div").click()
      self.browser.back()
      """action = webdriver.ActionChains(self.browser)
      tik = self.browser.find_element_by_id("container")
      tik.click()
      time.sleep(2)
      action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()"""
      time.sleep(2)
      self.browser.find_element_by_xpath("//*[@id='browsing-gw-homepage']/div/div[2]/div[2]/article[13]/a/span/img").click()
      time.sleep(2)
              
trendyol = TrendyolKullaniciKayitGiris()
trendyol.negatifLogin()
trendyol.positiveLogin(email,password)
trendyol.sepet()
##trendyol.negatifUserRegistration()
##trendyol.positiveUserRegistration(email,password) 
##trendyol.search()
