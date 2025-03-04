import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_주택전세가격추가.csv"
cctv_data_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\CCTV개수.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_cctv = pd.read_csv(cctv_data_path, encoding="utf-8-sig")  # CCTV 개수 데이터

# 2️⃣ 'CCTV개수' 값이 쉼표(,) 포함된 문자열일 경우 처리
df_cctv["CCTV개수"] = df_cctv["CCTV개수"].astype(str).str.replace(",", "").astype(float)

# 3️⃣ '자치구' 컬럼에서 CCTV 개수 집계
cctv_counts = df_cctv.groupby("자치구")["CCTV개수"].sum().reset_index()
cctv_counts.columns = ["자치구", "CCTV개수"]  # 컬럼명 변경

# 4️⃣ 최종 데이터셋에 'CCTV개수' 컬럼 추가 (구 컬럼과 비교하여 매칭)
df_final = df_final.merge(cctv_counts, left_on="구", right_on="자치구", how="left")

# 5️⃣ 'CCTV개수' 컬럼이 없는 경우 NaN → 0으로 변환
df_final["CCTV개수"] = df_final["CCTV개수"].fillna(0).astype(int)

# 6️⃣ 불필요한 '자치구' 컬럼 삭제
df_final.drop(columns=["자치구"], inplace=True, errors="ignore")

# 7️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_CCTV추가.csv"
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! 'CCTV개수' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")
