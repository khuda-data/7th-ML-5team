import pandas as pd

# 📂 파일 경로 설정
input_file_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\병원.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\병원_필터링.csv"

# 1️⃣ CSV 파일 인코딩 자동 감지 후 읽기
encodings = ["utf-8", "cp949", "euc-kr"]
for enc in encodings:
    try:
        df = pd.read_csv(input_file_path, encoding=enc)
        print(f"✅ CSV 파일을 {enc} 인코딩으로 성공적으로 불러왔습니다.")
        break
    except UnicodeDecodeError:
        print(f"❌ {enc} 인코딩으로 불러오기에 실패했습니다. 다른 인코딩을 시도합니다.")

# 2️⃣ '상세영업상태명'이 "영업중"인 행만 필터링
df = df[df["상세영업상태명"] == "영업중"].copy()

# 3️⃣ '업태구분명'에서 "요양병원"이 포함된 행 삭제
df = df[~df["업태구분명"].str.contains("요양병원", na=False)].copy()

# 4️⃣ 필터링된 데이터를 새로운 CSV 파일로 저장
df.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 필터링 완료! 영업 중이며 요양병원이 아닌 병원 데이터는 {output_file_path} 에 저장됨.")
