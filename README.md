# EasyJudge Server
## 프로젝트 소개
* 코드를 자동 채점하는 크롬 익스텐션인 **EasyJudge**의 동작을 위한 API서버 입니다.  
* 코드와 입력 값(stdin), 함께 동작할 파일 등을 입력으로 받아 코드의 출력 값을 반환합니다.
## 기술 스택
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"/> <img src="https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"> <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"> 
## 프로젝트 구조
```
📦codeserver
 ┣ 📂runcode
 ┃ ┗ 📜CodeRunner.py
 ┣ 📂util
 ┃ ┣ 📜ConfigParser.py
 ┃ ┣ 📜CustomException.py
 ┃ ┣ 📜ErrorHandler.py
 ┃ ┣ 📜FileUtil.py
 ┃ ┗ 📜Judge.py
 ┣ 📜Dockerfile
 ┣ 📜README.md
 ┣ 📜app.py
 ┣ 📜config.ini
 ┗ 📜requirements.txt
```
## BUILD
``` shell
$ docker build -t flask-application:latest .
```
## RUN
``` shell
$ docker run -p <host portnum>:<container portnum> --memory=<memory> flask-application
```
포트 기본 값은 `5000:5000`입니다. memory는 `1g`를 추천합니다. 더 낮은 메모리를 사용할 수 있으나, 코드 채점시 제한 메모리에 걸리지 않음에도 `MLE Error`를 발생시키는 원인이 됩니다.
## TODO
* 현재는 C언어만 컴파일 / 실행 가능하지만 추후에 C++, 자바, 파이썬등 여러 언어를 지원할 예정입니다.
* 현재는 한번에 한 테스트 케이스만 실행하지만, 한 코드에 대해 여러 테스트 케이스를 처리하는 기능도 고려하고 있습니다.