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

@app.route('/image_process', methods=['POST'])
def image_process():
    pass

def plate_sticker_deeplearning():
    pass

def image_ocr():
    pass 

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8081)
