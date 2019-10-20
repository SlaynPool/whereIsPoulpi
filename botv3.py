import discord
from opensky_api import OpenSkyApi, StateVector

def createhtml(lat, lon):
    #on va générer une page html, c'est laid mais 
    file = open ("whereispoulpi.html","w")
    file.write('<html><body>\n  <div id="mapdiv"></div>\n  <script src="http://www.openlayers.org/api/OpenLayers.js"></script>')
    file.write('<script>\n    map = new OpenLayers.Map("mapdiv"); \n   map.addLayer(new OpenLayers.Layer.OSM());\n' )
    file.write('var lonLat = new OpenLayers.LonLat( %r , %r )\n' %  (lat, lon))
    file.write('.transform(\n')
    file.write('        new OpenLayers.Projection("EPSG:4326"),\n')
    file.write('        map.getProjectionObject()\n')
    file.write('        );\n    var zoom=2;\n   var markers = new OpenLayers.Layer.Markers( "Markers" );\n  map.addLayer(markers);\n    markers.addMarker(new OpenLayers.Marker(lonLat));\n     map.setCenter (lonLat, zoom);\n')
    file.write('</script>\n')
    file.write('</body></html>')
    file.close()



def airplane(icao):
    api = OpenSkyApi("USERNAME","PASSWORD")
    data = api.get_states(time_secs=0,icao24=icao)
    for s in data.states:
        createhtml(s.longitude, s.latitude)
        return ("longitude:%r, latidude:%r,altitude:%r,vitesse:%r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity))


client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!whereispoulpi'):
        msg = message.content
        msg = msg.split(' ',1)[1]
        msg = airplane(msg)

        await message.channel.send(msg)
        await message.channel.send('Poulpi location :', file=discord.File('whereispoulpi.html'))
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('TOKEN')
