from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def helloWorld():
    # counter belongs to the global scope
    global counter
    counter += 1
    return "Hello world" + " the counter is: " + str(counter)

@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d, %B, %Y at %X")
    html_content = "<html><head><title>Hello Flask</title></head><body>"
    html_content += "<strong>Hello Flask World!</strong> on " + formatted_now
    html_content += "</body></html>"
    return html_content

@app.route('/template')
def template():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d, %B, %Y at %X")
    return render_template("index.html", title = "Hello Template", message = "Hello mate", content = "on " + formatted_now)

counter = 0

if __name__ == '__main__':
    app.run('localhost', 4449)