import requests
from flask import Flask,render_template,json
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['DEBUG']=True
@app.route('/weather_info', methods=['GET','POST'])
def weather_info():
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=532c9007b961c01a0ab55a56f575b8fe'
    city='germany'
    r=requests.get(url.format(city)).json()


    weather={
       'city': city,
       'temperature':r["main"]['temp'],
       'humidity':r['main']['humidity'],
       'description':r['weather'][0]['description'],
       'icon':r['weather'][0]['icon'],

    }
    print(weather)
    return render_template('weather.html',weather=weather)



if __name__=="__main__":
    app.debug =True
    app.run()
