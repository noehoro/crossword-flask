from generate import main
from flask import Flask, send_file, url_for, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
