from flask import Flask
import random


app = Flask(__name__)

@app.route("/")
def hello_world():
    num = random.randrange(3)
    options = {0: "グー", 1: "チョキ", 2: "パー"}
    payload = options.get(num)
    return payload


if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0', port=5000)