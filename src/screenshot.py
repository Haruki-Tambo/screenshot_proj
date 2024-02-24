from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import queue
import logging
import time

class screenshot:
    def __init__(self, driver_path, url, save_folder, max_save=30) -> None:
        options = Options()
        options.add_argument('--headless')
        self.driver_path = driver_path
        self.driver = webdriver.Chrome(executable_path=self.driver_path, options=options)
        self.q = queue.Queue()
        self.first_url = url
        self.urls_set = set()
        self.save_folder = save_folder
        self.max_save = max_save

        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def get_png(self, url, cnt):
        self.driver.get(url)
        # time.sleep(0.5)
        width = self.driver.execute_script("return document.body.scrollWidth;")
        height = self.driver.execute_script("return document.body.scrollHeight;")
        self.driver.set_window_size(width,height)
        self.driver.get_screenshot_as_file(f'{self.save_folder}/{cnt}.png')
        logging.info(f'{self.save_folder}/{cnt}.png')
    
    def get_url(self):
        links = self.driver.find_elements(By.TAG_NAME, "a") 
        for link in links:
            url = link.get_attribute("href")
            if not url in self.urls_set:
                self.q.put(url)
                self.urls_set.add(url)

    def run(self):
        self.q.put(self.first_url)
        self.urls_set.add(self.first_url)
        cnt = 1
        while not self.q.empty():
            url = self.q.get()
            self.get_png(url, cnt)
            self.get_url()
            cnt += 1
            if self.max_save <= cnt-1:
                break


def main():
    driver_path = "./webdriver/chromedriver-win64/chromedriver.exe"
    url = "https://qiita.com/"
    save_folder = "./screenshot"
    sc = screenshot(driver_path, url, save_folder)
    sc.run()

if __name__ == "__main__":
    main()