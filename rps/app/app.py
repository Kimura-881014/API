from flask import Flask
from flask import jsonify
import random
import time
import hashlib
import os
from dotenv import load_dotenv


app = Flask(__name__)


load_dotenv()
key = os.environ['MY_SECRET_KEY']

@app.route("/")
def hello_world():
    num = random.randrange(3)
    options = {0: "Rock", 1: "Paper", 2: "Scissors"}
    payload = options.get(num)
    _time = str(int(time.time()))
    hash_obj = hashlib.sha256((_time + payload + key).encode())
    signature = hash_obj.hexdigest()
    return jsonify({"time": _time, "payload":payload, "signature":signature})


if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0', port=5000)