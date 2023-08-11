import configparser
import json
import random
import re

import requests

from communication.Speak import print_and_tts
from worker.Worker import Worker


def extract_korean(word):
    return re.sub(r"[^가-힣]", "", word)


class WordChainGame(Worker):
    def __init__(self, threshold_count=3):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self._key = config['WORD_CHAIN']['key']
        self._threshold_count = threshold_count

    def work(self, _=None, voice=None):
        print_and_tts('게임을 시작합니다.')
        r_word = None
        fail_count = 0
        while True:
            print_and_tts('단어를 입력하세요.')
            word = voice()
            try:
                if not self.check_word(word):
                    print_and_tts(f"{word} 단어가 존재하지 않습니다.")
                    if fail_count >= self._threshold_count-1:  # 3번째는 패배
                        print_and_tts('존재하지 않는 단어를 3회 말하셨습니다. 당신은 패배하셨습니다.')
                        break
                    fail_count += 1
                    continue
                else:
                    fail_count = 0
                if r_word and r_word[-1] != word[0]:
                    print_and_tts(f"{r_word}의 끝 단어와 {word} 단어의 첫 단어가 같지 않습니다. 당신은 패배하셨습니다.")
                    break
            except AssertionError:
                print_and_tts('단어의 길이가 짧습니다. 2단어 이상 입력하세요.')
                continue
            except ConnectionError | requests.exceptions.ConnectionError:
                print_and_tts('서버와의 연결이 원할하지 않습니다.')
                break
            r_word = self.recommend_word(word[-1])
            if r_word is None:
                print_and_tts('끝말잇기 게임에 승리하셨습니다.')
                break
            print_and_tts(f"컴퓨터가 선택한 단어는 '{r_word}'입니다.")

    def search_word(self, text: str, method='exact'):
        url = 'http://opendict.korean.go.kr/api/search'
        params = {
            'key': self._key,
            'q': text.strip(),
            'req_type': 'json',
            'part': 'word',
            'advanced': 'y',  # 옵션 적용 여부
            'target': 1,  # 어휘
            'method': method,
            'type1': 'word',  # 단어
            'type3': 'general',  # 일반어
            'pos': 1,  # 명사
            'letter_s': 2,  # 음절수 시작
            'letter_e': 4
        }

        res = requests.get(url, params)

        if res.status_code == 200:
            return json.loads(res.text)
        else:
            print_and_tts(f"서버 연결에 실패했습니다. code : {res.status_code}")
            raise ConnectionError

    def check_word(self, text: str):
        if text is None or len(text.strip()) < 2:
            raise AssertionError('입력된 문자열의 길이가 너무 짧습니다.')
        return self.search_word(text)['channel']['total'] > 0

    def recommend_word(self, start_word):
        try:
            words = self.search_word(start_word, 'start')
        except ConnectionError:
            print_and_tts('서버와의 통신의 원할하지 않습니다. 다시 입력해 주세요.')
            return None
        if words['channel']['total'] == 0:
            return None
        current_num = words['channel']['num']
        n = random.randint(0, current_num - 1)
        return extract_korean(words['channel']['item'][n]['word'])


if __name__ == '__main__':
    g = WordChainGame()
    # pprint.pprint(g.search_word('소', 'start'))
    # pprint.pprint(g.search_word('선풍기'))
    print(g.recommend_word('선풍기'))
