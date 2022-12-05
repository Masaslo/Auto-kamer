import flask
import json
import sys

app = flask.Flask('__name__')

#with open("data.json", 'r') as file:
#    p = json.load(file)

#def addToTerminal(text):
#    global p
#    with open("data.json", "rw") as f:
#        string = json.load(f)
 #       newString = text + string
 #       json.dump(newString, f)
 #       p = newString



@app.route('/LichtUit')
def LichtUit():
    return flask.redirect('/')

@app.route('/LichtAan')
def LichtAan():
    return flask.redirect('/')

@app.route('/DeurOpen')
def DeurOpen():
    return flask.redirect('/')

@app.route('/DeurDicht')
def DeurDicht():
    return flask.redirect('/')

@app.route('/StopContactUit')
def StopContactUit():
    return flask.redirect('/')

@app.route('/StopContactAan')
def StopContactAan():
    return flask.redirect('/')

@app.route('/SensorUit')
def SesnorUit():

    return flask.redirect('/')

@app.route('/SensorAan')
def SensorAan():
    #addToTerminal("<br> gay")
    return flask.redirect('/')

@app.route('/')
def home():
    return flask.render_template('index.html')

def maakServer():
    app.run(host='0.0.0.0', port=5000)
