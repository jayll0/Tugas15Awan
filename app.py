from flask import Flask, render_template
from database import Database
import time
import os

app = Flask(__name__)

database = Database()

@app.route('/')
def index():
    instance_id  = os.environ.get('WEBSITE_INSTANCE_ID', 'Local-Machine')

    return render_template('index.html', nama="Kelompok 5", id_mesin = instance_id)

@app.route('/db-test')
def db_test():
    hasil = database.db_test()

    return render_template('db-test.html', status=hasil)

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

if __name__ == '__main__':
    app.run(debug=True)