import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_범죄추가.csv"
fine_dust_data_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\미세먼지_구별평균.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_미세먼지추가.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_fine_dust = pd.read_csv(fine_dust_data_path, encoding="utf-8-sig")  # 미세먼지 데이터

# 2️⃣ '구' 컬럼에서 미세먼지 농도 매칭
df_fine_dust = df_fine_dust[["구", "미세먼지(PM10) 평균", "초미세먼지(PM25) 평균"]]  # 필요한 컬럼만 추출

# 3️⃣ 최종 데이터셋에 '미세먼지농도' 컬럼 추가 (구 컬럼과 매칭)
df_final = df_final.merge(df_fine_dust, on="구", how="left")

# 4️⃣ '미세먼지농도' 컬럼이 없는 경우 0으로 채우기
df_final["미세먼지(PM10) 평균"] = df_final["미세먼지(PM10) 평균"].fillna(0).round(2)
df_final["초미세먼지(PM25) 평균"] = df_final["초미세먼지(PM25) 평균"].fillna(0).round(2)

# 5️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '미세먼지농도' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")
