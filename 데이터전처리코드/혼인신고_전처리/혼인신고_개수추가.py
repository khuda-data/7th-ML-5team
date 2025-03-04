import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터셋.csv"
marriage_data_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\혼인.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_혼인추가.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_marriage = pd.read_csv(marriage_data_path, encoding="utf-8-sig")  # 혼인 데이터

# 2️⃣ '행정동' 컬럼에서 혼인 건수 집계
marriage_counts = df_marriage.groupby("행정동")["2021~2023혼인"].sum().reset_index()

# 3️⃣ 최종 데이터셋에 '2021~2023혼인' 컬럼 추가 (읍면동명과 비교하여 매칭)
df_final = df_final.merge(marriage_counts, left_on="읍면동명", right_on="행정동", how="left")

# 4️⃣ '2021~2023혼인' 컬럼이 없는 경우 0으로 채우기
df_final["2021~2023혼인"] = df_final["2021~2023혼인"].fillna(0).astype(int)

# 5️⃣ 불필요한 '행정동' 컬럼 삭제
df_final.drop(columns=["행정동"], inplace=True, errors="ignore")

# 6️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '2021~2023혼인' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")
