import datetime
import sqlite3
import requests
from flask import Flask, render_template, request
import Parking
import ParkingDatabase

app = Flask(__name__)

db_path = "../data/Parking.db"

database = ParkingDatabase.Database(db_path)
parking = Parking()

@app.route('/enter_car', methods=['POST'])
def enter_car():
    plate_number = request.form['plate_number']
    sticker = request.form['sticker']
    entry_time = request.form['entry_time']
    user = database.check_user_database(plate_number)
    database.insert_data(plate_number, entry_time, user, sticker)
    
@app.route('check_timeover')
def check_timeover():
    enter_time = database.get_enter_time()

    check_time = datetime.datetime.now() - enter_time
    if check_time >= 300:
        Parking.send_chatbot()
        return "time over"
    else:
        return "pass"
    
@app.route('check_sticker_by_plate_number')
def check_sticker_by_plate_number():
    
    if database.get_sticker():
        return "yes"
    else:
        return "no"
    




@app.route('/')
def index():
    # index.html 파일을 렌더링해서 반환합니다.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
