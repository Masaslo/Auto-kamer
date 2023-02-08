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

lichtServoPort = 12

autoslot = "autoslotaan"
autolicht = "autolichtaan"

@app.route('/lichtuit')
def LichtUit():

    return flask.redirect('/')

@app.route('/lichtaan')
def LichtAan():
    return flask.redirect('/')

@app.route('/slotopen')
def DeurOpen():
    return flask.redirect('/')

@app.route('/slotdicht')
def DeurDicht():
    return flask.redirect('/')

@app.route('/stopcontactuit')
def StopContactUit():
    return flask.redirect('/')

@app.route('/stopcontactaan')
def StopContactAan():
    return flask.redirect('/')


@app.route('/autolicht')
def autolichtToggle():
    global autolicht
    if autolicht == "autolichtaan":
        autolicht = "autolichtuit"
    elif autolicht == "autolichtuit":
        autolicht = "autolichtaan"
    print(autolicht)

    return flask.redirect('/')


@app.route('/autoslot')
def autoSlotToggle():
    global autoslot
    if autoslot == "autoslotaan":
        autoslot = "autoslotuit"
    elif autoslot == "autoslotuit":
        autoslot = "autoslotaan"
    print(autoslot)
    return flask.redirect('/')


licht = "lichtaan"
slot = "slotdicht"
temp = 31.5

@app.route('/')
def home():
    return flask.render_template('index.html',
                                  temp=temp,
                                 slot=slot,
                                 licht=licht,
                                 autolicht=autolicht,
                                 autoslot=autoslot
                                 )

def maakServer():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    maakServer()