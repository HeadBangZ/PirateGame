from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def ShowIndexPage():
    my_file_path = os.path.join('static/image/mydrawing.png')
    return render_template('index.html', user_image = my_file_path)

if __name__ == "__main__":
    app.run('localhost', 4449)
