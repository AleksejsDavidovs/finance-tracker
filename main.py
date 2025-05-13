from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime
import os

app = Flask(__name__)

DATA_FILE = 'data.json'


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    data = load_data()
    ienakumi = sum(item['summa'] for item in data if item['tips'] == 'Ienākumi')
    izdevumi = sum(item['summa'] for item in data if item['tips'] == 'Izdevumi')
    balanss = ienakumi - izdevumi
    return render_template("index.html", ieraksti=data[::-1], ienakumi=ienakumi, izdevumi=izdevumi, balanss=balanss)

@app.route('/add', methods=['POST'])
def add():
    data = load_data()
    tips = request.form['tips']
    kategorija = request.form['kategorija']
    summa = float(request.form['summa'])
    ieraksts = {
        "datums": datetime.now().strftime('%Y-%m-%d'),
        "tips": tips,
        "kategorija": kategorija,
        "summa": summa
    }
    data.append(ieraksts)
    save_data(data)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    data = load_data()
    if 0 <= id < len(data):
        del data[-1 - id]  
        save_data(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
