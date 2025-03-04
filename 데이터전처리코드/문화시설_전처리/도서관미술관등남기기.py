import pandas as pd

# 📂 파일 경로 설정
input_file_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\도서관공연장박물관전시시설미술관.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\문화시설_필터링.csv"

# 1️⃣ CSV 파일 인코딩 자동 감지 후 읽기
encodings = ["utf-8", "cp949", "euc-kr"]
for enc in encodings:
    try:
        df = pd.read_csv(input_file_path, encoding=enc)
        print(f"✅ CSV 파일을 {enc} 인코딩으로 성공적으로 불러왔습니다.")
        break
    except UnicodeDecodeError:
        print(f"❌ {enc} 인코딩으로 불러오기에 실패했습니다. 다른 인코딩을 시도합니다.")

# 2️⃣ 필터링할 대상 분류명 리스트
valid_categories = ["전시시설", "공연장", "박물관", "도서관", "미술관"]

# 3️⃣ '분류명' 컬럼에서 특정 값만 남기고 필터링
df_filtered = df[df["분류명"].isin(valid_categories)].copy()

# 4️⃣ 필터링된 데이터를 새로운 CSV 파일로 저장
df_filtered.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 필터링 완료! 유효한 분류명만 남은 데이터는 {output_file_path} 에 저장됨.")