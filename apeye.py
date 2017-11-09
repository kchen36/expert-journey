from flask import Flask,render_template,request
import urllib2,json
app = Flask(__name__)


@app.route("/")
def root():
    u = urllib2.open("https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo")
    d = json.loads(u.read())
    return render_template("index",d)
