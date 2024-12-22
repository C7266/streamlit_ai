# README: 대구 집가격 예측 프로그램

## 프로젝트 개요
⦁프로젝트 이름: 대구 집값 예측 프로그램
⦁설명: 이 프로젝트는 대구광역시의 다양한 데이터를 기반으로 미래 집값을 예측합니다. 사용자는 여러 입력 값을 설정하여 특정 지역과 날짜의 집값을 예측할 수 있습니다.

---

## 기능 요약
1. 지역별 집값 예측
2. 대구의 지역 정보 및 지도 시각화
3. 사용자 친화적인 데이터 입력 UI
4. 예측 결과를 직관적으로 제공

---

## 설치 및 실행 방법
### 필수 환경
- **Python** 3.8 이상

### 의존성 설치
```bash
pip install streamlit numpy pandas tensorflow matplotlib scikit-learn
```

### 모델 파일 준비
- `LSTM.keras` 파일을 프로젝트 디렉토리에 배치.

### 실행 방법
⦁Streamlit 실행:
```bash
streamlit run app.py
```
⦁브라우저에서 [http://localhost:8501](http://localhost:8501)을 열어서 통신.
+ streamlit cloud app 서비스를 통해 https://daeguhouseprice.streamlit.app/ 상시 접속 가능하게 변경.

---

## 사용법
![image](https://github.com/user-attachments/assets/a343babe-170a-47a4-b30f-e758a538a061)

1. 왼쪽 슬라이더와 드롭다운 메뉴에서 집값 예측에 필요한 데이터를 입력합니다.
   - 예시: 전용면적, 층수, 건축년도, 지역 등.

![image](https://github.com/user-attachments/assets/27925f7a-fe23-4af0-9a78-447d604a40b9)

2. 원하는 날짜를 선택한 후 "예측하기" 버튼을 클릭합니다.

![image](https://github.com/user-attachments/assets/c15d85d2-a89a-4814-83d2-8690994f5cfe)

3. 화면에 예측된 집값이 표시되며, 지도에서 선택한 지역을 확인할 수 있습니다.

---

## 프로젝트 파일 구성
```
─ app.py                # Streamlit 코드
─ LSTM.keras            # 학습된 LSTM 모델
─ README.md             # 사용 설명서
─ requirements.txt      # 필수한 Python 라이브러리 목록
```

---

## 기술 스택
- **프론트엔드:** Streamlit
- **백엔드:** Python (TensorFlow, NumPy, Pandas)
- **시각화 도구:** Streamlit 지도 모듈

---

## 예시 화면
![image](https://github.com/user-attachments/assets/7f6697ac-19ff-425c-a66d-dd1704bb7070)
![image](https://github.com/user-attachments/assets/b7eeb3a3-d604-4085-8087-b9cc4b1050e5)
![image](https://github.com/user-attachments/assets/d5fa8fc8-aee1-4427-9be6-6d03d0f68127)


---
