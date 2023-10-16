# 환영합니다
gs25 편의점 포스기의 상품 판매, 시재점검 기능을 구현하였습니다.<br/>
<br/>
<br/>
사용한 개발환경 및 도구 : Anaconda prompt(pyuic5), Pycharm(Python IDE), Oracle SQL Developer(데이터베이스 IDE), DroidCam Client(컴퓨터, 스마트폰 연동 카메라)<br/>
<br/>
사용한 프레임워크 및 라이브러리 : pyqt(ui 디자인), pyzbar(바코드), opencv(카메라), oracle db(데이터베이스)<br/>
<br/>
사용한 언어 : Python, SQL, CSS<br/>
<br/>
<br/>
판매 화면에서 바코드 스캔이 가능한 상태일 때 p버튼을 누르면 바코드가 스캔됩니다.<br/>
<br/>
시재 점검 화면에서 텍스트에 엔터키를 눌러야 적용됩니다.
# 동작 영상
[유튜브 링크](https://youtu.be/kVJpqkf7Mw8)

# UI
## 메인 화면
![image](https://github.com/dontoong/gs25/assets/106039761/fbccb64b-6e57-4fc1-ad26-ecc7226a5b65)
<br/><br/>
## 상품 판매 화면
![image](https://github.com/dontoong/gs25/assets/106039761/9bd9db6d-f414-413a-9090-b4b511f98029)
<br/><br/>
## 판매 완료 화면
![image](https://github.com/dontoong/gs25/assets/106039761/136a1ce5-d9d6-4186-8f2c-9c9a7e026f30)
<br/><br/>
## 상품 판매 화면(금액 입력)
![image](https://github.com/dontoong/gs25/assets/106039761/eff37c1f-e703-471c-9413-853c14653384)
<br/><br/>
## 판매 완료 화면(금액 입력)
![image](https://github.com/dontoong/gs25/assets/106039761/57ffe8c0-a781-49cd-8740-22e4e69fc12c)
<br/><br/>
## 시재 점검 화면(시재 입력)
![image](https://github.com/dontoong/gs25/assets/106039761/dc3f1b6c-0a53-4ce0-9ee6-1fe1c5a6eefc)
<br/><br/>
## 시재 점검 화면(시재 입력)
![image](https://github.com/dontoong/gs25/assets/106039761/bb9fed69-1e93-4f1c-aa67-35801eb04596)
<br/><br/>
## 시재 결과 화면
![image](https://github.com/dontoong/gs25/assets/106039761/8a37fa90-e1a8-4746-883d-1b9ab6fca7ea)
<br/><br/>

# 개발 환경
![image](https://github.com/dontoong/gs25/assets/106039761/6179d73c-edb2-4a17-aa33-adaaf54adef2)

# 인터페이스 설계 및 구조
![1](https://github.com/dontoong/gs25/assets/106039761/35ea4781-3e5e-4f65-a78f-49b37e7c452a)

# 데이터베이스 구조
![2](https://github.com/dontoong/gs25/assets/106039761/dea7d223-9e2b-4009-8628-ae09c6d72ac3)

# 기타 주의사항
## security.py
security.py는 db의 개인정보라 코드 수정했습니다.<br/>
oracleDB의 계정과 포트번호를 연결하신 후 각 테이블 생성하신 후 원하시는 상품의 이름, 바코드, 가격 데이터를 추가하시면 사용하실 수 있습니다.
