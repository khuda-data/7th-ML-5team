import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_치안센터추가.csv"
housing_data_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\주택전세가격.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_housing = pd.read_csv(housing_data_path, encoding="utf-8-sig")  # 주택 전세 가격 데이터

# 2️⃣ '자치구' 컬럼에서 평균 주택 전세가격 계산 (소수점 유지)
housing_prices = df_housing.groupby("자치구")["종합"].mean().reset_index()
housing_prices.columns = ["자치구", "주택전세가격"]  # 컬럼명 변경

# 3️⃣ 최종 데이터셋에 '주택전세가격' 컬럼 추가 (구 컬럼과 비교하여 매칭)
df_final = df_final.merge(housing_prices, left_on="구", right_on="자치구", how="left")

# 4️⃣ '주택전세가격' 컬럼이 없는 경우 NaN → 0으로 변환 (소수점 유지)
df_final["주택전세가격"] = df_final["주택전세가격"].fillna(0).round(2)  # 소수점 2자리 유지

# 5️⃣ 불필요한 '자치구' 컬럼 삭제
df_final.drop(columns=["자치구"], inplace=True, errors="ignore")

# 6️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_주택전세가격추가.csv"
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '주택전세가격' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")
