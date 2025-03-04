import requests
import pandas as pd
import time

# 네이버 API 키 설정
CLIENT_ID = "63g1yjybk8"  # 네이버 API ID 입력
CLIENT_SECRET = "Dflv2Buf5iqrra4dG0TZ8GJ7gC6DD1AWtwfkEmEp"  # 네이버 API Secret 입력

# 1️⃣ 위경도 → 행정동(A) 변환 함수
def get_administrative_dong(x, y):
    url = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": CLIENT_ID,
        "X-NCP-APIGW-API-KEY": CLIENT_SECRET
    }
    params = {
        "coords": f"{x},{y}",
        "output": "json",
        "orders": "admcode"  # 행정동(A) 정보만 반환
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if "results" in data and len(data["results"]) > 0:
                for result in data["results"]:
                    if result["name"] == "admcode":
                        dong = result["region"]["area3"]["name"]
                        print(f"✅ [행정동 변환 성공] (경도: {x}, 위도: {y}) → {dong}")
                        return dong
            print(f"❌ [행정동 변환 실패] (경도: {x}, 위도: {y}) → 결과 없음")
        else:
            print(f"❌ [API 응답 오류] 행정동 변환 실패 (HTTP {response.status_code})")
    except Exception as e:
        print(f"❌ [예외 발생] 행정동 변환 오류 ({x}, {y}): {e}")

    return None

# 2️⃣ CSV 파일 로드
file_path = r"C:\Users\82102\Desktop\토이프로젝트\raw data\안전센터및구조대.csv"

# CSV 파일 인코딩 자동 감지
try:
    df = pd.read_csv(file_path, encoding="utf-8")  
except UnicodeDecodeError:
    try:
        df = pd.read_csv(file_path, encoding="cp949")
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding="euc-kr")

# 변환 결과 저장할 컬럼 추가
df["행정동"] = None

# 3️⃣ 좌표 → 행정동 변환 실행
for index, row in df.iterrows():
    x, y = row["경도"], row["위도"]
    
    if pd.isna(x) or pd.isna(y):
        print(f"❌ [오류] 좌표 없음, 변환 불가 (Index: {index})")
        continue

    admin_dong = get_administrative_dong(x, y)

    # 변환 결과를 DataFrame에 저장
    df.at[index, "행정동"] = admin_dong

    time.sleep(0.1)  # API 요청 속도 제한

# 4️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\안전센터및구조대_행정동.csv"
df.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! 행정동 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")
