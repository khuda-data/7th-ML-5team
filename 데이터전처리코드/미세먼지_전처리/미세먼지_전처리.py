import pandas as pd

# 📂 파일 경로 설정
fine_dust_data_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\미세먼지.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\미세먼지_구별평균.csv"

# 1️⃣ CSV 파일 인코딩 자동 감지 후 읽기
encodings = ["utf-8", "cp949", "euc-kr"]
for enc in encodings:
    try:
        df = pd.read_csv(fine_dust_data_path, encoding=enc)
        print(f"✅ CSV 파일을 {enc} 인코딩으로 성공적으로 불러왔습니다.")
        break
    except UnicodeDecodeError:
        print(f"❌ {enc} 인코딩으로 불러오기에 실패했습니다. 다른 인코딩을 시도합니다.")

# 2️⃣ '일시' 컬럼을 datetime 형식으로 변환
df["일시"] = pd.to_datetime(df["일시"], format="%Y-%m-%d %H:%M", errors="coerce")

# 3️⃣ 2024년 데이터만 필터링
df_2024 = df[df["일시"].dt.year == 2024].copy()

# 4️⃣ '구분'이 "평균"인 행 제거 (각 구별 데이터만 유지)
df_2024 = df_2024[df_2024["구분"] != "평균"]

# 5️⃣ 미세먼지(PM10) & 초미세먼지(PM25) 평균 계산 (구별)
df_avg = df_2024.groupby("구분")[["미세먼지(PM10)", "초미세먼지(PM25)"]].mean().reset_index()

# 6️⃣ 컬럼명 변경
df_avg.columns = ["구", "미세먼지(PM10) 평균", "초미세먼지(PM25) 평균"]

# 7️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
df_avg.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '구'별 미세먼지 평균 데이터는 {output_file_path} 에 저장됨.")
