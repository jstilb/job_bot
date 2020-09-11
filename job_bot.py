from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import numpy as np




class JobBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('headless')
        chrome_options.add_argument('incognito')
        self.driver = webdriver.Chrome(executable_path='/Users/jmsitunes/Desktop/projects/auto_grocery/chromedriver',
                                       options=chrome_options)
        self.driver.delete_all_cookies()

    def get_website(self):
        sleep(5)
        self.driver.get('https://www.linkedin.com/jobs')
        sleep(5)



    def search(self):
        sleep(1)
        job_title_input = self.driver.find_element_by_xpath('//*[@id="JOBS"]/section[1]/input')
        location_input = self.driver.find_element_by_xpath('//*[@id="JOBS"]/section[2]/input')
        exit_autocomplete = self.driver.find_element_by_xpath('/html/body/main/section[1]')
        search_btn = self.driver.find_element_by_xpath('/html/body/main/section[1]/section/div[2]/button[2]')

        job_title_input.send_keys('Business Intelligence Analyst')
        sleep(3)
        location_input.clear()
        location_input.send_keys('Denver, Colorado')
        sleep(2)
        exit_autocomplete.click()
        sleep(2)
        search_btn.click()

    def scrape_web_links(self):
        SCROLL_PAUSE_TIME = 3

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        links = self.driver.find_elements_by_xpath("//*[@href]")
        clean_links = [x for x in links if "jobs/view" in x.get_attribute('href')]
        jobs_info = []

        for link in clean_links:
            # pull up webpage & full job description
            self.driver.get(str(link)) # problem here. evidently this isn't a string and it needs to be and str() isn't working
            show_more_btn = self.driver.find_element_by_xpath('/html/body/main/section[1]/section[3]/div[1]/section/button[1]')
            show_more_btn.click()
            sleep(1)

            # scrape job info
            job_title = self.driver.find_element_by_class_name('topcard_title')
            data = self.driver.find_element_by_class_name('description')
            items = data.find_elements_by_tag_name('li')
            items.insert(0, job_title.text)
            jobs_info.append(items.text)
            break
        for job in jobs_info:
            print(job)







bot = JobBot()
bot.get_website()
bot.search()
bot.scrape_web_links()