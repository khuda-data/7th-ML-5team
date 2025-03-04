import pandas as pd

# 📂 파일 경로 설정
school_data_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\학교_행정동.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\학교_유니크_정제.csv"

# 1️⃣ 데이터 불러오기
df_school = pd.read_csv(school_data_path, encoding="utf-8-sig")

# 2️⃣ '학교명' 컬럼에서 중복된 행 제거 (첫 번째만 남김)
df_school = df_school.drop_duplicates(subset=["학교명"], keep="first")

# 3️⃣ '학교종류명' 수정
def classify_school_type(school_type):
    if pd.isna(school_type):  # NaN 값 처리
        return None
    if "초" in school_type:
        return "초등학교"
    elif "중" in school_type:
        return "중학교"
    elif "고" in school_type:
        return "고등학교"
    return None  # 초·중·고가 포함되지 않은 경우 삭제 대상

df_school["학교종류명"] = df_school["학교종류명"].apply(classify_school_type)

# 4️⃣ 초·중·고가 아닌 행 삭제
df_school = df_school.dropna(subset=["학교종류명"])

# 5️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
df_school.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '학교종류명' 정제 및 중복 제거된 데이터가 {output_file_path} 에 저장됨.")