import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_버스정류장추가.csv"
hospital_data_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\병원_행정동.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_hospital = pd.read_csv(hospital_data_path, encoding="utf-8-sig")  # 병원 데이터

# 2️⃣ '행정동' 컬럼에서 병원 개수 집계
hospital_counts = df_hospital["행정동"].value_counts().reset_index()
hospital_counts.columns = ["행정동", "병원개수"]  # 컬럼명 변경

# 3️⃣ 최종 데이터셋에 '병원개수' 컬럼 추가 (읍면동명과 비교하여 매칭)
df_final = df_final.merge(hospital_counts, left_on="읍면동명", right_on="행정동", how="left")

# 4️⃣ '병원개수' 컬럼이 없는 경우 0으로 채우기
df_final["병원개수"] = df_final["병원개수"].fillna(0).astype(int)

# 5️⃣ 불필요한 '행정동' 컬럼 삭제
df_final.drop(columns=["행정동"], inplace=True, errors="ignore")

# 6️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_병원추가.csv"
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '병원개수' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")