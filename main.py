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


def duri_utility(voice):
    print_and_tts('검색 및 게임 기능을 활성화 합니다.')
    text = None
    while not text:
        text = voice()
    if text[-2:] == '검색':
        naver_search.work(text[0:-2].strip())
    elif text[-2:] == '날씨':
        whether.work(text[0:-2].strip())
    elif text[-4:] == '미세먼지':
        fine_dust.work(text[0:-4].strip())
    elif text[-2:] == '게임':
        word_chain.work(voice=voice)
    else:
        print_and_tts(f'{text}는 지원하지 않는 기능입니다.')

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
