import pandas as pd

# 📂 파일 경로 설정
daycare_data_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\어린이집.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\어린이집_수정.csv"

# ✅ 1️⃣ CSV 파일 불러오기 (인코딩 자동 감지)
encoding_list = ["utf-8-sig", "cp949", "euc-kr"]
for enc in encoding_list:
    try:
        df_daycare = pd.read_csv(daycare_data_path, encoding=enc)
        print(f"✅ 파일을 성공적으로 불러왔습니다! 사용된 인코딩: {enc}")
        break  # 성공하면 반복문 탈출
    except UnicodeDecodeError:
        print(f"⚠ 인코딩 오류 발생: {enc} → 다른 인코딩 시도...")

# ✅ 2️⃣ '제공서비스' 컬럼이 비어있는 경우 '일반'으로 채우기
df_daycare["제공서비스"] = df_daycare["제공서비스"].fillna("일반")

# ✅ 3️⃣ 수정된 데이터를 새로운 CSV 파일로 저장
df_daycare.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 수정 완료! '제공서비스' 컬럼이 보완된 파일이 {output_file_path} 에 저장됨.")