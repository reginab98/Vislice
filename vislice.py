import bottle
import model

vislice = model.Vislice('stanje.json')

vislice = model.Vislice()
#id = vislice.nova_igra()
#igra, stanje = vislice.igre[id]
#vislice.ugibaj(id, 'A')
#vislice.ugibaj(id, 'K')
#vislice.ugibaj(id, 'U')
#vislice.ugibaj(id, 'L')


@bottle.get('/')
def index():
    return bottle.template('index.tpl') 


#@bottle.get('/igra/')
#def testigra():
#    return bottle.template('igra.html', id_igre=id, igra=igra, stanje=stanje) S TEM SMO SE NEKAJ IGRALI

#v brskalnik napisemo localhost:8080 in tam je igrica
#ta funkcija pove da na nekih rootih(/) prikaze slikico:

@bottle.get('/img/<ime>')
def slike(ime):
    return bottle.static_file(ime, root = 'img') 

@bottle.post('/nova_igra/') #delamo piškotek
def nova_igra_2():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', str(id_igre), path='/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro_2():
    id_igre = int(bottle.request.get_cookie('id_igre'))
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.html', id_igre=id_igre, igra=igra, stanje=stanje)

@bottle.post('/igra/')
def ugibaj_2():
    id_igre = int(bottle.request.get_cookie('id_igre'))
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')
    print(crka)
#post spreminja stanje, get pa ne
bottle.run(reloader=True, debug=True)





