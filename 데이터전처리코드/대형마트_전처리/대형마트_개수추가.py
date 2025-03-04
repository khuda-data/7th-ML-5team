import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_공원추가.csv"
mart_data_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\대형마트_행정동.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_mart = pd.read_csv(mart_data_path, encoding="utf-8-sig")  # 대형마트 행정동 데이터

# 2️⃣ '행정동' 컬럼에서 대형마트 개수 집계
mart_counts = df_mart["행정동"].value_counts().reset_index()
mart_counts.columns = ["행정동", "대형마트개수"]  # 컬럼명 변경

# 3️⃣ 최종 데이터셋에 '대형마트개수' 컬럼 추가 (읍면동명과 비교하여 매칭)
df_final = df_final.merge(mart_counts, left_on="읍면동명", right_on="행정동", how="left")

# 4️⃣ '대형마트개수' 컬럼이 없는 경우 0으로 채우기
df_final["대형마트개수"] = df_final["대형마트개수"].fillna(0).astype(int)

# 5️⃣ 불필요한 '행정동' 컬럼 삭제
df_final.drop(columns=["행정동"], inplace=True)

# 6️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_대형마트추가.csv"
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! 업데이트된 데이터는 {output_file_path} 에 저장됨.")