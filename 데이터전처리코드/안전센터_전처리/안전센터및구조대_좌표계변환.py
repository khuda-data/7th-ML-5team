import pandas as pd
from pyproj import Transformer

# 📂 파일 경로 설정
input_file_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\안전센터및구조대.csv"
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\안전센터및구조대_위경도.csv"

# 1️⃣ CSV 파일 인코딩 자동 감지 후 읽기
encodings = ["utf-8", "cp949", "euc-kr"]
for enc in encodings:
    try:
        df = pd.read_csv(input_file_path, encoding=enc)
        print(f"✅ CSV 파일을 {enc} 인코딩으로 성공적으로 불러왔습니다.")
        break
    except UnicodeDecodeError:
        print(f"❌ {enc} 인코딩으로 불러오기에 실패했습니다. 다른 인코딩을 시도합니다.")

# 2️⃣ 좌표 변환기 설정 (EPSG:5186 -> EPSG:4326)
transformer = Transformer.from_crs("EPSG:5186", "EPSG:4326", always_xy=True)

# 3️⃣ X, Y 좌표를 경도, 위도로 변환
def convert_coordinates(row):
    try:
        x, y = float(row["X좌표"]), float(row["Y좌표"])
        lon, lat = transformer.transform(x, y)  # TM 좌표 → WGS84 변환
        return pd.Series([lon, lat])  # (경도, 위도)
    except Exception as e:
        print(f"❌ 변환 오류: {e}")
        return pd.Series([None, None])  # 변환 실패 시 NaN 반환

df[["경도", "위도"]] = df.apply(convert_coordinates, axis=1)

# 4️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
df.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '경도', '위도' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")
