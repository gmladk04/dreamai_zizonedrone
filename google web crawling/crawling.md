# 구글 웹 크롤링 코드 실행 방법
## 1. 본인 크롬 버전 확인(버전 확인 필수)
![KakaoTalk_20201228_174755128](https://user-images.githubusercontent.com/48545220/103202225-2c48e080-4935-11eb-86a0-b55adc3e10ab.png)

   
## 2. chrome driver에서 자기 크롬 버전이랑 맞는거 다운로드

    [Downloads - ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/downloads)
![KakaoTalk_20201228_175144115](https://user-images.githubusercontent.com/48545220/103202307-631ef680-4935-11eb-97fa-e7a9982228e6.png)

    나는 86이라서 86 다운받았음!

## 3. 다운받은거 zip 파일 압축해제 한 다음에 파일 경로 확인
## 4. 일단 난,,, `pycharm`에서 실행함


> #1

- 아까 확인했던 경로 `driver=webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")`

    주황글씨 있는 부분에 갖다 붙이기

- 그냥 경로 복붙하면 경로 폴더구분자가 백슬래시('\')인데 이거를 그냥 슬래시(/)로 바꿔줘야함

> #2

- pycharmproject 폴더 안에 download 폴더 만들어줘야함 → 여기에 크롤링한 거 저장됨
- 소스코드가 있는 프로젝트에다가 이렇게 만들어야 한다는 뜻


> TIP

- keyword 입력 귀찮고 url 갖고 있으면 그냥 url 부분에 크롤링할 주소 붙여서 실행해도됨

> 실행

1. 실행 후 keyword 입력
   ![KakaoTalk_20201228_175457778](https://user-images.githubusercontent.com/48545220/103202498-f1937800-4935-11eb-899e-6408fd8310ea.png)

3. 자동으로 크롬창 제어되면서 크롤링 시작됨(사진 참고)
   ![KakaoTalk_20201228_175526151](https://user-images.githubusercontent.com/48545220/103202512-fa844980-4935-11eb-92a3-7eb7b7a253f0.png)


4. download 폴더 확인
5. 필터링
6. 공유드라이브에 올리기
