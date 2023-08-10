import speech_recognition as sr
from speech_recognition import UnknownValueError, RequestError, WaitTimeoutError

from Speak import print_and_tts


def voice_input():
    r = sr.Recognizer()
    mic = sr.Microphone()

    def wrapper():
        with mic as source:  # 마이크에 담긴 소리를 토대로 아래 코드 실행
            # r.adjust_for_ambient_noise(source)  # 잡음 제거 코드 (없어도 무방)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)  # 해당 소리를 오디오 파일 형태로 변환
        try:
            text = r.recognize_google(audio, language="ko-KR").strip()  # 오디오를 토대로 음성 인식
            print_and_tts(f"입력 단어는 '{text}' 입니다.")
            return text
        except UnknownValueError:
            print_and_tts("음성 인식 실패")
        except RequestError:
            print_and_tts("서버 에러 발생")
        except WaitTimeoutError:
            print_and_tts("인식 실패")
        # None return

    return wrapper
