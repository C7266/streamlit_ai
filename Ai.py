import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import matplotlib as mpl

# 한글 폰트 설정
mpl.rc('font', family='Malgun Gothic')
mpl.rc('axes', unicode_minus=False)

# 1. 모델 로드
model_path = 'LSTM.keras'  # 학습된 모델 경로
try:
    lstm_model = load_model(model_path)
    st.success("모델이 성공적으로 로드되었습니다.")
except Exception as e:
    st.error(f"모델 로드 중 오류 발생: {e}")

# 2. Min/Max 값 설정 (73개의 피처에 맞게 수정)
min_values = np.array([10, 1, 1950, 0, 0, 0, 0, 0, 0.0, 200001, 1] + [0] * 8 + [0] * (73 - 19))
max_values = np.array([300, 50, 2023, 10, 20, 20, 10, 50, 10.0, 202412, 31] + [1] * 8 + [1] * (73 - 19))

# 3. 지역 정보 설정
region_names = ['중구', '동구', '서구', '남구', '북구', '수성구', '달서구', '달성군']
region_coordinates = {
    "중구": [35.8667, 128.5943],
    "동구": [35.8869, 128.6354],
    "서구": [35.8711, 128.5593],
    "남구": [35.8457, 128.6015],
    "북구": [35.8848, 128.5814],
    "수성구": [35.8588, 128.6302],
    "달서구": [35.8294, 128.5322],
    "달성군": [35.7749, 128.4317],
}

# 4. 사용자 입력
area = st.slider("전용면적 (㎡)", 10.0, 300.0, 85.0)
floor = st.slider("층수", 1, 50, 10)
built_year = st.slider("건축년도", 1950, 2023, 2000)
market = st.slider("대규모 점포 개수", 0, 10, 2)
park = st.slider("공원 개수", 0, 20, 5)
hospital = st.slider("병원 개수", 0, 20, 3)
school = st.slider("학교 개수", 0, 10, 4)
transport = st.slider("대중교통 수단 수", 0, 50, 20)
interest_rate = st.slider("금리 (%)", 0.0, 10.0, 3.25)

region = st.selectbox("지역 선택", region_names)
contract_date = st.date_input("계약 날짜")
contract_year = int(contract_date.strftime("%Y%m"))
contract_day = contract_date.day

# 지역 원-핫 인코딩
region_encoded = np.zeros(len(region_names))
region_encoded[region_names.index(region)] = 1

# 입력 데이터 배열 생성
input_data = np.array([[area, floor, built_year, market, park, hospital, school, transport, interest_rate, contract_year, contract_day]])
input_data = np.concatenate([input_data, region_encoded.reshape(1, -1)], axis=1)

# 학습에 사용된 73개의 피처로 확장
input_data_expanded = np.concatenate([input_data, np.zeros((1, 73 - input_data.shape[1]))], axis=1)

# 데이터 스케일링
scaled_input = (input_data_expanded - min_values) / (max_values - min_values)
scaled_input = np.repeat(scaled_input, 10, axis=0)  # LSTM 입력 형태로 확장
scaled_input = np.expand_dims(scaled_input, axis=0)

# 예측
if st.button("예측하기"):
    try:
        prediction_scaled = lstm_model.predict(scaled_input)[0][0]

        # 스케일 복원 (실제 금액으로 변환)
        predicted_price = prediction_scaled * (max_values[8] - min_values[8]) + min_values[8]
        prediction_krw = f"{round(predicted_price * 10000, -1):,.0f}만원"

        st.subheader(f"예측된 집값: {prediction_krw}")
    except Exception as e:
        st.error(f"예측 중 오류 발생: {e}")

# 5. 선택한 지역 지도 표시
if region in region_coordinates:
    st.subheader(f"선택한 지역: {region}")
    map_data = pd.DataFrame([{"lat": region_coordinates[region][0], "lon": region_coordinates[region][1]}])
    st.map(map_data)