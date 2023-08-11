from speech_recognition import WaitTimeoutError
from communication.Speak import print_and_tts
from communication.Input import voice_input
from worker.FineDust import FineDust
from worker.NaverSearch import NaverSearch
from worker.Whether import Whether
from worker.WordChainGame import WordChainGame


whether = Whether()
naver_search = NaverSearch()
fine_dust = FineDust()
word_chain = WordChainGame()

action_phrase = {
    '검색': naver_search,
    '날씨': whether,
    '먼지': fine_dust,
    '게임': word_chain,
}


def duri_utility(voice):
    print_and_tts('검색 및 게임 기능을 활성화 합니다.')
    text = None
    while not text:
        text = voice()
    worker = action_phrase[text[-2:]]
    if worker:
        worker.work(text[:2].strip() if text[:2] is not None else None, voice)
    else:
        print_and_tts(f'{text[-2:]}는 지원하지 않는 기능입니다.')

    print_and_tts('검색 및 게임 기능을 종료합니다.')


def main():
    bot_names = ['두리야', '두리', '둘이', '둘리']
    voice = voice_input()
    while True:
        print_and_tts('이름을 불러 주세요.')

        try:
            text = voice()
        except WaitTimeoutError:
            print_and_tts('speech recognition wait time error, restart..')
            continue
        if text in bot_names:
            duri_utility(voice)
        if text == '종료':
            print_and_tts('프로그램을 종료합니다.')
            break


if __name__ == '__main__':
    main()
