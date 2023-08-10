import json

import requests

from communication.Speak import print_and_tts
from worker.Worker import Worker


class Whether(Worker):
    def __init__(self):
        self.cities = {
            '서울': {'latitude': 37.566, 'longitude': 126.9784},
            '런던': {'latitude': 51.5085, 'longitude': -0.1257},
            '뉴욕': {'latitude': 40.7143, 'longitude': -74.006}
        }

    def work(self, text, voice=None):
        print_and_tts(f"{text} 지역의 날씨를 조회합니다.")
        print_and_tts(self.whether_info(text))

    def whether_info(self, city) -> str:
        if city in self.cities:
            return f"{city}의 날씨는 {self.get_whether(self.cities[city])}도 입니다."
        else:
            return f'{city}는 지원하지 않는 지역입니다.'

    def get_whether(self, location) -> str:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={location['latitude']}&longitude={location['longitude']}&current_weather=true"
        response = requests.get(url)
        data = json.loads(response.text)
        return data['current_weather']['temperature']
