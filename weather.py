import urllib.request
from urllib.parse import quote_plus
import json

def getweather(l):
    with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+l+"&APPID=c2c0c54356ddf28f62d80b7f68ae4133") as url:
        p = url.read()
        j_objs = json.loads(p)
        link = j_objs['main']['temp']
        link1 = j_objs['main']['humidity']
        link2 = j_objs['weather'][0]['description']
        print("The Temperature is  :"+ str(link-273)+" "+"C")
        print("The Humidity is  :"+ str(link1)+"%")
        print("The Report is :"+ str(link2))


