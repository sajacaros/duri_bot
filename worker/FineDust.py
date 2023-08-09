import configparser
import json
import requests

from Speak import print_and_tts
from worker.Worker import Worker


class FineDust(Worker):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self._decoding_key = config['FINE_DUST']['key']

    def work(self, text, voice=None):
        print_and_tts(f"{text} 지역의 미세먼지를 조회합니다.")
        print_and_tts(self.find_dust_info(text))

    def find_dust_info(self, text):
        info = self.get_find_dust(text)
        if info:
            return f"{text} 지역의 미세먼지 PM25 수치는 {info['pm25Value']}이고 등급은 {info['pm25Grade']}입니다."
        else:
            return f"{text}는 지원하지 않는 지역입니다."

    def get_find_dust(self, text='동작구'):
        url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
        params = {
            'serviceKey': self._decoding_key,
            'returnType': 'json',
            'numOfRows': '100',
            'pageNo': '1',
            'sidoName': '서울',
            'ver': '1.0',
        }
        response = requests.get(url, params=params)
        data = json.loads(response.text)
        for info in data['response']['body']['items']:
            if info['stationName'] == text:
                return info
        return None
