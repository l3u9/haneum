import sqlite3
import random
import string
from datetime import datetime

# SQLite DB 파일 경로
db_path = 'mydatabase.db'

# 데이터베이스 연결
conn = sqlite3.connect(db_path)

# 커서 생성
c = conn.cursor()

# PARKING 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS PARKING(
                PLATE_NUMBER TEXT,
                ENTRY_TIME INTEGER,
                NAME TEXT,
                STICKER BOOLEAN);''')

# 랜덤 데이터 생성 및 삽입
for i in range(100):
    # 임의의 랜덤 데이터 생성
    plate_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    entry_time = int(datetime.timestamp(datetime.now()))
    name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    sticker = random.choice([True, False])
    # INSERT 문 실행
    c.execute("INSERT INTO PARKING VALUES (?, ?, ?, ?)", (plate_number, entry_time, name, sticker))

# 데이터베이스 저장
conn.commit()

# 커서와 데이터베이스 연결 해제
c.close()
conn.close()
