from flask import (Flask,request,render_template,url_for,flash,redirect)
app = Flask(__name__)
@app.route('/microdesk/', methods=['GET', 'POST'])
def main():
    return render_template('main/index.html')
@app.route('/')
def index():
    return redirect("/microdesk")


