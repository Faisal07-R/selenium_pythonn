import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestTextBox(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    def testTexBoxInput(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://demoqa.com/text-box") # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "userName").send_keys("bahar") # isi username
        time.sleep(4)
        browser.find_element(By.ID,"userEmail").send_keys("rat@mail.com") #isi email
        time.sleep(1)
        browser.find_element(By.ID,"currentAddress").send_keys("Bandung") # isi current address
        time.sleep(2)
        browser.find_element(By.ID,"permanentAddress").send_keys("New Zeland") # isi permanent address
        time.sleep(1)
        browser.find_element(By.ID,"submit").click() # klik tombol submit
        time.sleep(1)

        response_data = browser.find_element(By.ID,"output").text
        
        self.assertIn("",response_data)

    def testTexBoxNoInputUsername(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://demoqa.com/text-box") # buka situs
        time.sleep(3)
        # browser.find_element(By.ID, "userName").send_keys("bahar") # isi username
        time.sleep(4)
        browser.find_element(By.ID,"userEmail").send_keys("rat@mail.com") #isi email
        time.sleep(1)
        browser.find_element(By.ID,"currentAddress").send_keys("Bandung") # isi current address
        time.sleep(2)
        browser.find_element(By.ID,"permanentAddress").send_keys("New Zeland") # isi permanent address
        time.sleep(1)
        browser.find_element(By.ID,"submit").click() # klik tombol submit
        time.sleep(1)

        response_data = browser.find_element(By.ID,"output").text
        
        self.assertIn("",response_data)

    def testTexBoxNoInputUseremail(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://demoqa.com/text-box") # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "userName").send_keys("bahar") # isi username
        time.sleep(4)
        # browser.find_element(By.ID,"userEmail").send_keys("rat@mail.com") #isi email
        time.sleep(1)
        browser.find_element(By.ID,"currentAddress").send_keys("Bandung") # isi current address
        time.sleep(2)
        browser.find_element(By.ID,"permanentAddress").send_keys("New Zeland") # isi permanent address
        time.sleep(1)
        browser.find_element(By.ID,"submit").click() # klik tombol submit
        time.sleep(1)

        response_data = browser.find_element(By.ID,"output").text
        
        self.assertIn("",response_data)
        

        def tearDown(self): 
            self.browser.close() 

if __name__ == "__main__": 
    unittest.main()