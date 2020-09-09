from selenium import webdriver
from time import sleep




class JobBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('headless')
        chrome_options.add_argument('incognito')
        self.driver = webdriver.Chrome(executable_path='/Users/jmsitunes/Desktop/projects/auto_grocery/chromedriver',
                                       options=chrome_options)
        self.driver.delete_all_cookies()

    def login(self):
        sleep(10)
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
        links = self.driver.find_elements_by_xpath("//*[@href]")
        clean_links = [x for x in links if "jobs/view" in x.get_attribute('href')]
        for link in clean_links:
            print(link.get_attribute("href"))
        #need to scroll down. Look up instabot tutorial



bot = JobBot()
bot.login()
bot.search()
bot.scrape_web_links()