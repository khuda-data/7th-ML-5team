import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_병원추가.csv"
crime_data_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\5대범죄발생횟수.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_crime = pd.read_csv(crime_data_path, encoding="utf-8-sig")  # 5대 범죄 발생 횟수 데이터

# 2️⃣ '자치구' 컬럼에서 5대 범죄 발생 횟수 매칭
df_crime = df_crime[["자치구", "발생"]]  # 필요한 컬럼만 추출
df_crime.columns = ["구", "5대범죄발생횟수"]  # 컬럼명 변경

# 3️⃣ 최종 데이터셋에 '5대범죄발생횟수' 컬럼 추가 (구 컬럼과 매칭)
df_final = df_final.merge(df_crime, on="구", how="left")

# 4️⃣ '5대범죄발생횟수' 컬럼이 없는 경우 0으로 채우기
df_final["5대범죄발생횟수"] = df_final["5대범죄발생횟수"].fillna(0).astype(int)

# 5️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_범죄추가.csv"
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '5대범죄발생횟수' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")
