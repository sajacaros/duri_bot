import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Speak import print_and_tts
from worker.Worker import Worker


class NaverSearch(Worker):
    def __init__(self):
        self._driver = webdriver.Chrome(
            service=Service(executable_path=r'C:\tools\Webdriver\chromedriver-win64\chromedriver.exe')
        )

    def work(self, text, voice=None):
        print_and_tts(f"{text}를 검색합니다.")
        self.get_naver_search(text)

    def get_naver_search(self, search_test: str) -> str:
        self._driver.get('https://naver.com')
        time.sleep(3)
        search_input = self._driver.find_element(By.CSS_SELECTOR, '#query')
        search_input.send_keys(search_test)
        search_button = self._driver.find_element(By.CSS_SELECTOR, '.btn_search')
        search_button.click()
