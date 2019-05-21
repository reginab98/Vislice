import bottle
import model

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.tempfile('index.tpl') 

bottle.run(reloader=True, debug=True)

#v brskalnik napisemo localhost:8080


