import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋.csv"
cinema_data_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\서울시_영화상영관_행정동추가.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_영화관추가.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_cinema = pd.read_csv(cinema_data_path, encoding="utf-8-sig")  # 영화관 데이터

# 2️⃣ '행정동' 컬럼에서 영화관 개수 집계
cinema_counts = df_cinema["행정동"].value_counts().reset_index()
cinema_counts.columns = ["행정동", "영화관개수"]  # 컬럼명 변경

# 3️⃣ 최종 데이터셋에 '영화관개수' 컬럼 추가 (읍면동명과 비교하여 매칭)
df_final = df_final.merge(cinema_counts, left_on="읍면동명", right_on="행정동", how="left")

# 4️⃣ '영화관개수' 컬럼이 없는 경우 0으로 채우기
df_final["영화관개수"] = df_final["영화관개수"].fillna(0).astype(int)

# 5️⃣ 불필요한 '행정동' 컬럼 삭제
df_final.drop(columns=["행정동"], inplace=True, errors="ignore")

# 6️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '영화관개수' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")