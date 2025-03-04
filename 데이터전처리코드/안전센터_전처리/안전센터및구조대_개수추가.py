import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_CCTV추가.csv"
safety_center_data_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\안전센터및구조대_행정동.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_safety = pd.read_csv(safety_center_data_path, encoding="utf-8-sig")  # 안전센터 및 구조대 데이터

# 2️⃣ '행정동' 컬럼에서 안전센터 및 구조대 개수 집계
safety_counts = df_safety["행정동"].value_counts().reset_index()
safety_counts.columns = ["행정동", "안전센터및구조대개수"]  # 컬럼명 변경

# 3️⃣ 최종 데이터셋에 '안전센터및구조대개수' 컬럼 추가 (읍면동명과 비교하여 매칭)
df_final = df_final.merge(safety_counts, left_on="읍면동명", right_on="행정동", how="left")

# 4️⃣ '안전센터및구조대개수' 컬럼이 없는 경우 0으로 채우기
df_final["안전센터및구조대개수"] = df_final["안전센터및구조대개수"].fillna(0).astype(int)

# 5️⃣ 불필요한 '행정동' 컬럼 삭제
df_final.drop(columns=["행정동"], inplace=True, errors="ignore")

# 6️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_안전센터추가.csv"
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '안전센터및구조대개수' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")