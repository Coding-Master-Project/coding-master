# coding-master

웹페이지 로컬 실행 방법

vscode 터미널에서 아래 명령어로 서버 실행

```
pip install -r requirements.txt // django 등을 포함한 필요한 라이브러리 설치
```

secrets.json 파일 따로 생성(최상위 폴더 아래)
시크릿키 내용 보내준 거 복사해서 붙이기

```
python manage.py runserver
```
서버 실행한 뒤, localhost:8000으로 접속

