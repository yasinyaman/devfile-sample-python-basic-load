from flask import Flask
import os
from cpu_load_generator import load_all_cores

app = Flask(__name__)

@app.route('/')
def hello():
    load_all_cores(duration_s=600, target_load=0.5)
    return "Hello World!"

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT')) or 8080

    app.run(port=port,host='0.0.0.0')
