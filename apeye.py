from flask import Flask,render_template
import urllib2,json
app = Flask(__name__)


@app.route("/")
def root():
    
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo")
    d = json.loads(u.read())
    return render_template("index.html",date = d["date"],image=d["url"], copyr=d["copyright"],exp=d["explanation"])
if __name__ == "__main__":
    app.debug = True
    app.run()

