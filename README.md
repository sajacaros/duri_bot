# duri_bot

## 프로젝트 최상위 폴더에 'config.ini' 파일을 만들고 아래 규격에 맞혀서 설정값 입력
```
[FINE_DUST]
key=공공데이터포털KEY

[WORD_CHAIN]
key=우리말샘KEY

[NAVER_SEARCH]
path=C:\tools\Webdriver\chromedriver-win64\chromedriver.exe
```

## 크롬 driver 다운로드
* 셀레니움 크롬 드라이버가 최신 버전의 크롬을 자동으로 지원하지 않음 
* 크롬 드라이버를 수동으로 다운로드
  * [최신 크롬 드라이버 다운로드](https://googlechromelabs.github.io/chrome-for-testing/)
* 향후 크롬 드라이버 지원시 자동 다운로드를 통해 실행 가능

## 시작 모드
* `두리야, 두리, 둘이, 둘리` 중 한 단어를 말하면 `작업 모드`로 넘어감
* 시작 모드에서 `종료`를 말하면 종료
* `작업 모드`가 종료 되면 다시 `시작 모드`로 돌아옴

## 작업 모드
* `서울 날씨` 를 말하면 기온을 알려줌
  * 서울 및 런던, 뉴욕을 지원
* `동작구 먼지` 를 말하면 미세먼지 수치를 알려줌
  * 동작구 대신 `서울의 다른 구` 지원
* `주식 검색` 을 말하면 네이버에서 주식을 검색
  * 주식 대신 검색하고 싶은 문자열을 추가해도 됨
* `게임` 을 말하면 끝말잇기 게임 시작

## 실행 방법
``` 
python main.py
```

## 클래스 다이어그램
*![클래스 다이어그램](클래스.PNG)

## 참고
* gtts사용시 임의 파일을 만들고 삭제하는 부분에서 가끔 에러가 발생하여 pyttsx3 모듈로 교체함
``` 
pip install pyttsx3
```