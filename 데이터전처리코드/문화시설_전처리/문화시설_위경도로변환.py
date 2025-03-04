import requests
import pandas as pd
import time

# 네이버 API 키 설정
CLIENT_ID = "63g1yjybk8"  # 네이버 API ID 입력
CLIENT_SECRET = "Dflv2Buf5iqrra4dG0TZ8GJ7gC6DD1AWtwfkEmEp"  # 네이버 API Secret 입력

# 1️⃣ 주소 → 위경도 변환 함수
def get_coordinates(address):
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": CLIENT_ID,
        "X-NCP-APIGW-API-KEY": CLIENT_SECRET
    }
    params = {"query": address}

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if "addresses" in data and len(data["addresses"]) > 0:
                x = data["addresses"][0]["x"]  # 경도
                y = data["addresses"][0]["y"]  # 위도
                print(f"✅ [주소 변환 성공] {address} → (경도: {x}, 위도: {y})")
                return x, y
            else:
                print(f"❌ [주소 변환 실패] {address} → 결과 없음")
        else:
            print(f"❌ [API 응답 오류] 주소 변환 실패 (HTTP {response.status_code})")
    except Exception as e:
        print(f"❌ [예외 발생] 주소 변환 오류 ({address}): {e}")
    
    return None, None

# 2️⃣ CSV 파일 로드
file_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\도서관공연장박물관전시시설미술관_필터링.csv"

# CSV 파일 인코딩 자동 감지
try:
    df = pd.read_csv(file_path, encoding="utf-8")  
except UnicodeDecodeError:
    try:
        df = pd.read_csv(file_path, encoding="cp949")
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding="euc-kr")

# 변환 결과 저장할 컬럼 추가
df["경도"] = None
df["위도"] = None

# 3️⃣ 주소 → 좌표 변환 실행
for index, row in df.iterrows():
    address = row["주소"]

    if pd.isna(address):
        print(f"❌ [오류] 주소 없음, 변환 불가 (Index: {index})")
        continue

    x, y = get_coordinates(address)

    # 변환 결과를 DataFrame에 저장
    df.at[index, "경도"] = x
    df.at[index, "위도"] = y

    time.sleep(0.1)  # API 요청 속도 제한

# 4️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\문화시설_좌표.csv"
df.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 1단계 완료! 좌표 변환된 데이터는 {output_file_path} 에 저장됨.")
