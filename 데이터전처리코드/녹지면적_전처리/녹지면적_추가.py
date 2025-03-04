import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_미세먼지추가.csv"
green_space_data_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\녹지현황.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_녹지면적추가.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_green_space = pd.read_csv(green_space_data_path, encoding="utf-8-sig")  # 녹지 데이터

# 2️⃣ '자치구' 컬럼에서 녹지 면적 데이터 매칭
df_green_space = df_green_space[["자치구", "면적"]]  # 필요한 컬럼만 추출
df_green_space.columns = ["구", "녹지면적"]  # 컬럼명 변경

# 3️⃣ 최종 데이터셋에 '녹지면적(m^2)' 컬럼 추가 (구 컬럼과 매칭)
df_final = df_final.merge(df_green_space, on="구", how="left")

# 4️⃣ '녹지면적(m^2)' 컬럼이 없는 경우 0으로 채우기
df_final["녹지면적"] = df_final["녹지면적"].fillna(0)

# 5️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '녹지면적' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")
