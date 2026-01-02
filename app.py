from flask import Flask, render_template
from database import Database
import time

app = Flask(__name__)

database = Database()

@app.route('/')
def index():
    return render_template('index.html', nama="Mahasiswa Telkom")

@app.route('/about')
def about():
    return "Ini halaman About (Flask sederhana)"

# ENDPOINT BARU (bukan /stress)
@app.route('/cpu-test')
def cpu_test():
    start_time = time.time()
    duration = 300  # 5 menit (300 detik)
    n = 500         # nilai n untuk loop n^3

    while time.time() - start_time < duration:
        # Perulangan bersarang n^3 (Cubic Complexity)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    _ = i * j * k  # Beban CPU

    return render_template('cpu_test.html')

if __name__ == '_main_':
    app.run(debug=True)