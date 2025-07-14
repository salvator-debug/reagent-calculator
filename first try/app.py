
from flask import Flask
fake_db = []
app = Flask(__name__)
@app.route('/')
def home():

    return 'text'
if __name__ == "__main__":
    app.run()