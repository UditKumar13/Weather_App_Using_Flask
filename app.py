import requests
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['DEBUG']=True
@app.route('/', methods=['GET','POST'])
def index():
    url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=532c9007b961c01a0ab55a56f575b8fe'
    return render_templates('weather.html')


if __name__=="__main__":
    app.run(debug=True)
