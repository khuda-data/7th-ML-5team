import pandas as pd

# 📂 파일 경로 설정
final_dataset_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_야간어린이집추가.csv"
school_data_path = r"C:\Users\82102\Desktop\토이프로젝트\데이터 전처리\학교_유니크_정제.csv"

# 1️⃣ 데이터 불러오기
df_final = pd.read_csv(final_dataset_path, encoding="utf-8-sig")  # 최종 데이터셋
df_school = pd.read_csv(school_data_path, encoding="utf-8-sig")  # 정제된 학교 데이터

# 2️⃣ 학교 종류별 개수 집계 (한 번에 처리)
school_counts = df_school.groupby(["행정동", "학교종류명"]).size().unstack(fill_value=0)

# 3️⃣ 컬럼명 변경 (초등학교, 중학교, 고등학교 개수)
school_counts = school_counts.rename(columns={"초등학교": "초등학교개수", "중학교": "중학교개수", "고등학교": "고등학교개수"}).reset_index()

# 4️⃣ 최종 데이터셋에 병합 (읍면동명과 행정동 매칭)
df_final = df_final.merge(school_counts, left_on="읍면동명", right_on="행정동", how="left")

# 5️⃣ '학교 개수' 컬럼이 없는 경우 0으로 채우기
df_final["초등학교개수"] = df_final["초등학교개수"].fillna(0).astype(int)
df_final["중학교개수"] = df_final["중학교개수"].fillna(0).astype(int)
df_final["고등학교개수"] = df_final["고등학교개수"].fillna(0).astype(int)

# 6️⃣ 불필요한 '행정동' 컬럼 삭제
df_final.drop(columns=["행정동"], inplace=True, errors="ignore")

# 7️⃣ 변환된 데이터를 새로운 CSV 파일로 저장
output_file_path = r"C:\Users\82102\Desktop\토이프로젝트\최종데이터셋_학교추가.csv"
df_final.to_csv(output_file_path, index=False, encoding="utf-8-sig")

print(f"🎉 변환 완료! '초등학교개수', '중학교개수', '고등학교개수' 컬럼이 추가된 데이터는 {output_file_path} 에 저장됨.")
