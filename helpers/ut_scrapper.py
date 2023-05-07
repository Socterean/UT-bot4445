from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

from helpers.file_manager import FileManager
from helpers.file_manager import FILE_PATH

import csv
import random

class UtScrapper():
    def __init__(self) -> None:
        self.ff_options = FirefoxOptions()
        self.ff_options.headless = True
        self.driver = webdriver.Firefox(options=self.ff_options)

        self.fm = FileManager()
        self.fm.check_file()

    async def scrape_ut(self, weburl):
        self.driver.get(weburl)

        try:
            existent_elements = list(csv.DictReader(open('./data/ut_scrapper.csv', 'r')))
            new_element_list = []

            for e in range(10, 0, -1):
                element = self.driver.find_element(By.CSS_SELECTOR, 'div.alert-sm:nth-child({})'.format(e))
                e_text = str(element.text).split(' ')
                e_title = ''
                e_date = e_text[0]
                e_link = self.driver.find_element(By.CSS_SELECTOR, 'div.alert-sm:nth-child({}) > strong > a'.format(e)).get_attribute('href')
                e_flag = False
                
                for i in range(1,len(e_text)):
                    if i == 1:
                        e_title = e_title + e_text[i]
                    else:
                        e_title = e_title + ' ' + e_text[i]
                        
                for row in existent_elements:
                    if row['title'] == e_title and row['date'] == e_date:
                        e_flag = True
                        break

                if e_flag == True:
                    print("Element already in file")
                else:
                    self.fm.write_file(title=e_title, date=e_date, link=e_link)
                    new_element = {'title': e_title, 'date': e_date, 'link': e_link}
                    new_element_list.append(new_element)
                    print("---->New element added to the file")

            print ("The file has been saved")
            sleep(random.randint(4, 13))
            self.driver.close()
            return(new_element_list)

        except:
            print ("Element not found")
            sleep(random.randint(4, 13))
            self.driver.close()