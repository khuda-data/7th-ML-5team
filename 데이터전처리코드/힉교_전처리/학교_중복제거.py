import pandas as pd

# 📂 파일 경로 설정
school_data_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\학교_행정동.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\학교_유니크.csv"

# 1️⃣ 데이터 불러오기
df_school = pd.read_csv(school_data_path, encoding="utf-8-sig")

# 2️⃣ '학교명' 컬럼에서 중복된 행 제거 (첫 번째만 남김)
df_unique_schools = df_school.drop_duplicates(subset=["학교명"], keep="first")

# 3️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
df_unique_schools.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 중복 제거 완료! Unique한 학교 리스트가 {output_file_path} 에 저장됨.")