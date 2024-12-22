# README: 대구 집가격 예측 프로그램

## 프로젝트 개요
프로젝트의 본적은 대구광역시의 단위적인 데이터를 기능해 미래의 집가격을 예측합니다. 사용자는 여러 입력값을 설정하여 특정 지역과 날짜의 집가격을 예측할 수 있습니다.

---

## 기능 요약
1. 지역별 집가격 예측
2. 대구 지역 정보 및 지도 시각화
3. 사용자 흥정 데이터 입력 UI
4. 예측 결과를 집중되게 제공

---

## 설치 및 실행 방법
### 필수 환경
- **Python** 3.8 이상

### 의원성 설치
```bash
pip install streamlit numpy pandas tensorflow matplotlib scikit-learn
```

### 모델 파일 준비
- `LSTM.keras` 파일을 프로젝트 디렉토리에 및침.

### 실행 방법
```bash
streamlit run app.py
```
컴퓨터의 브라우저에서 [http://localhost:8501](http://localhost:8501)을 열어서 통신.
+ streamlit cloud app 서비스를 통해 https://daeguhouseprice.streamlit.app/ 상시 접속 가능하게 변경.

---

## 사용법
1. 여름 슬라이더와 드롭다운 메뉴를 사용하여 입력데이터를 입력합니다.
   - 예시: 전용면적, 층수, 건축년도, 지역 등.
2. 원하는 날짜를 선호한 후 "예측하기" 버튼을 클릭합니다.
3. 화면에 예측된 집가격이 표시되면서, 지도에서 선호한 지역을 확인할 수 있습니다.

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
값을 설정한 후의 화면 및 예측된 집가격 결과를 선발한 화면을 클릭하여 통합.

---

## 무단 해결
- **모델 로드 오류:** `LSTM.keras` 파일의 경로를 확인해주세요.
- **패키지 미설치:** `pip install -r requirements.txt` 명령을 실행.

---
