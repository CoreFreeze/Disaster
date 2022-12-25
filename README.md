# 재난취합프로그램

* **refacter.py** : 재난취합서버 GUI

* **refacter client.py** : 재난취합클라이언트 GUI

* **communication.py** : 통신 서버

* **communicationClient.py** : 통신 클라이언트

* **DBHandler.py** : DB 처리

* **HCHandler.py** : 한글파일 처리

* **settingHandler.py** : json파일 처리

# 사용된 파이썬 버전

* **python 3.9**

# 파이썬 설치 후 실행 시 해야할 것

* 가상환경 구축을 추천합니다.

깃에서 파일을 내려받은 후 vs code 터미널에서 아래 명령어 입력 
```
$python -m venv [임의의 가상환경명]
```
가상환경으로 추가하시겠습니까? 
알림창에 예를 클릭하여 가상환경으로 추가

가상환경 실행
```
$cd ./[생성한 가상환경명]
$cd ./Script
$activate
(생성한 가상환경명)$cd ..
(생성한 가상환경명)$cd ..
```
혹은 f5를 눌러 디버깅을 한 번 실행하면 가상환경이 실행됩니다.

* 가상환경에 빌드에 필요한 라이브러리를 추가

pyside2 설치(GUI 라이브러리)
```
(생성된 가상환경명)$pip install pyside2
```

openpyxl 설치(excel 라이브러리)
```
(생성된 가상환경명)$pip install openpyxl
```

pywin32 설치(한컴 제어용 라이브러리)
```
(생성된 가상환경명)$pip install pywin32
```

pyinstaller(패키지 배포 지원 라이브러리)
```
(생성된 가상환경명)$pip install pyinstaller
```

# 바이너리 파일로 빌드방법

```
(생성된 가상환경명)$pyinstaller --noconsole --icon=disaster.ico [배포할 python 스크립트 파일]
```






