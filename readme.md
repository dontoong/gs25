# 환영합니다
gs25 편의점 포스기의 상품 판매, 시재점검 기능을 구현하였습니다.<br/>
<br/>
사용한 개발환경 및 도구 : anaconda prompt(pyuic5), pycharm(Python IDE), oracle sql developer(데이터베이스 IDE), droidcam(컴퓨터, 스마트폰 연동 카메라)<br/>
사용한 프레임워크 및 라이브러리 : pyqt(ui 디자인), pyzbar(바코드), opencv(카메라), oracle db(데이터베이스)<br/>
사용한 언어 : python, sql, css<br/>
<br/>
판매 화면에서 바코드 스캔이 가능한 상태일 때 p버튼을 누르면 바코드가 스캔됩니다.<br/>
시재 점검 화면에서 텍스트에 엔터키를 눌러야 적용됩니다.

# 인터페이스 설계
![1](https://github.com/dontoong/gs25/assets/106039761/35ea4781-3e5e-4f65-a78f-49b37e7c452a)

# ERD
![2](https://github.com/dontoong/gs25/assets/106039761/dea7d223-9e2b-4009-8628-ae09c6d72ac3)

# UI
미리보기 파일에 프로그램의 UI 이미지 있습니다.

# 기타 주의사항
security.py는 db의 개인정보라 코드 수정했습니다.<br/>
oracleDB의 계정으로 각 테이블 생성하신 후 원하시는 상품의 이름, 바코드, 가격 추가하시면 사용하실 수 있습니다.
