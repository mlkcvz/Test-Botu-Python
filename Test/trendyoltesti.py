from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from userLogin import email,password
import time
class TrendyolAramaSepetFavoriİslemleri:
    def __init__(self):
        self.browser = webdriver.Chrome()
    def search(self):
        self.browser.get("https://www.trendyol.com/butik/liste/1/kadin")
        time.sleep(2)
        self.browser.maximize_window()
        searchCurser=self.browser.find_element_by_class_name("search-box")
        time.sleep(1)
        searchCurser.click()
        time.sleep(2)
        searchCurser.send_keys("Topuklu ayakkabı")
        time.sleep(2)
        searchCurser.send_keys(Keys.ENTER)
        self.browser.save_screenshot("topukluayakkabilar.png")
        time.sleep(2) 
    
    def sepeteEkle(self):
      
      self.browser.back()
      action = webdriver.ActionChains(self.browser)
      tik = self.browser.find_element_by_id("container")##ilkine tıklıyor
      tik.click()
      time.sleep(2)
      action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
      time.sleep(2)
      ##sayi =len(self.browser.find_element_by_css_selector
      ##print(sayi)
      urunler= self.browser.find_element_by_xpath("//*[@id='seller-store']/div/div[2]/div/div[3]/div[2]/div/div/div/div/div[1]/div/div/a/div[1]/img")
      action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
      time.sleep(2)
      urunler.click()
      time.sleep(2)
      self.browser.find_element_by_class_name("add-to-basket").click()
      time.sleep(3)
      self.browser.back()   
      
      """while True:
        for urun in urunler:
            if(self.browser.find_element_by_class_name("basket-item-count-container visible").text==0 ):
                urun.click()
                time.sleep(2)
                self.browser.find_element_by_class_name("add-to-basket").click()
                time.sleep(2)
                self.browser.back()
            else:
                break    """

    def sepettenCikar(self):
        time.sleep(2)
        self.browser.get("https://www.trendyol.com/sepet") 
        time.sleep(2)
        self.browser.find_element_by_css_selector("button i").click() 
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='pb-container']/div/div[3]/div[3]/div/div[3]/div/button[2]").click()
        time.sleep(2)

    def favorilereEkle(self):
        self.browser.get("https://www.trendyol.com/butik/liste/1/kadin")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='browsing-gw-homepage']/div/div/div/article[2]/a/span/img").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='boutique-detail-app']/div/div[2]/div/div[8]/a/div[1]/img").click()
        time.sleep(2)
        self.browser.find_element_by_class_name("fv").click()
        time.sleep(2)
        trendyol_.giris(email,password)
        time.sleep(2)
        self.browser.get("https://www.trendyol.com/butik/liste/1/kadin")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='browsing-gw-homepage']/div/div/div/article[6]/a/span/img").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='seller-store']/div/div[2]/div/div[5]/div[2]/div/div/div/div/div[2]/div/div/a/div[1]/img").click()
        time.sleep(2)
        self.browser.find_element_by_class_name("fv").click()
        time.sleep(2)
        self.browser.back()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='seller-store']/div/div[2]/div/div[6]/div[2]/div/div/div/div/div[3]/div/div/a/div[1]/img").click()
        time.sleep(2)
        self.browser.find_element_by_class_name("fv").click()
        time.sleep(2)
        self.browser.back()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='seller-store']/div/div[2]/div/div[6]/div[2]/div/div/div/div/div[4]/div/div/a/div[1]/img").click()
        time.sleep(2)
        self.browser.find_element_by_class_name("fv").click()
        time.sleep(2)
    def giris(self,email,password):
            time.sleep(2)
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
    def favorilerdeGezin(self):
        self.browser.get("https://www.trendyol.com/Hesabim/Favoriler")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='account-gw-favorites']/div/div[2]/div/div[1]").click()
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='account-gw-favorites']/div/div[2]/div/div[2]").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='account-gw-favorites']/div/div[2]/div/div[3]").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='account-gw-favorites']/div/div[2]/div/div[4]").click()

        

    ##def favorilerdenCikar(self):            

             


     
              
trendyol_ = TrendyolAramaSepetFavoriİslemleri()
trendyol_.search()
trendyol_.sepeteEkle()
trendyol_.sepettenCikar()
trendyol_.favorilereEkle()
trendyol_.favorilerdeGezin()

