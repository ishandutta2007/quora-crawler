from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys

import unittest, time, re

#reload(sys)
#sys.setdefaultencoding('utf-8')

class Sel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.quora.com/topic/Equity"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        driver = self.driver
        delay = 3
        driver.get(self.base_url)
        for i in range(1,300):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
            time.sleep(4)
        html_source = driver.page_source
        data = html_source.encode('utf-8')

        try:
            from BeautifulSoup import BeautifulSoup
        except ImportError:
            from bs4 import BeautifulSoup
        parsed_html = BeautifulSoup(data)

        try:
            question_list = parsed_html.body.findAll('span', attrs={'class':'rendered_qtext'})
            # talked_questionanies = dict()
            for i in range(1,len(question_list)):
              try:
                question = question_list[i].text
                if (question.strip()[-1:] == '?'):
                  print(question)
              except ImportError:
                  print("You are textless")
        except ImportError:
            print("You are exceptional")
        # print(question_list)

if __name__ == "__main__":
    unittest.main()
