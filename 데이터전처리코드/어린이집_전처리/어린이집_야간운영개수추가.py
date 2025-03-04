import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_어린이집추가.csv"
daycare_data_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\어린이집_행정동.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_daycare = pd.read_csv(daycare_data_path, encoding="utf-8-sig")  # 어린이집 데이터

# 2️⃣ '제공서비스' 컬럼에서 '야간' 포함 여부 확인 후 개수 카운트
df_night_daycare = df_daycare[df_daycare["제공서비스"].str.contains("야간", na=False)]

# 3️⃣ 행정동별 '야간운영어린이집개수' 카운트
night_daycare_counts = df_night_daycare["행정동"].value_counts().reset_index()
night_daycare_counts.columns = ["행정동", "야간운영어린이집개수"]

# 4️⃣ 최종 데이터셋에 '야간운영어린이집개수' 컬럼 추가 (읍면동명과 비교하여 매칭)
df_final = df_final.merge(night_daycare_counts, left_on="읍면동명", right_on="행정동", how="left")

# 5️⃣ '야간운영어린이집개수' 컬럼이 없는 경우 0으로 채우기
df_final["야간운영어린이집개수"] = df_final["야간운영어린이집개수"].fillna(0).astype(int)

# 6️⃣ 불필요한 '행정동' 컬럼 삭제
df_final.drop(columns=["행정동"], inplace=True)

# 7️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_야간어린이집추가.csv"
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '야간운영어린이집개수' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")