import pandas as pd

# 📂 파일 경로 설정
input_file_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\서울시_영화상영관_유니크.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\서울시_영화상영관_좌표유니크.csv"

# 1️⃣ CSV 파일 인코딩 자동 감지 후 읽기
encodings = ["utf-8", "cp949", "euc-kr"]
for enc in encodings:
    try:
        df = pd.read_csv(input_file_path, encoding=enc)
        print(f"✅ CSV 파일을 {enc} 인코딩으로 성공적으로 불러왔습니다.")
        break
    except UnicodeDecodeError:
        print(f"❌ {enc} 인코딩으로 불러오기에 실패했습니다. 다른 인코딩을 시도합니다.")

# 2️⃣ '좌표정보(X)', '좌표정보(Y)' 기준으로 중복 제거 (첫 번째 값만 유지)
df_unique = df.drop_duplicates(subset=["좌표정보(X)", "좌표정보(Y)"], keep="first").copy()

# 3️⃣ 필터링된 데이터를 새로운 CSV 파일로 저장
df_unique.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 중복 제거 완료! Unique한 '좌표정보(X)', '좌표정보(Y)' 데이터는 {output_file_path} 에 저장됨.")
