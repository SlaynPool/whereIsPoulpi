import discord
from opensky_api import OpenSkyApi, StateVector

def airplane(icao):
    api = OpenSkyApi("USERNAME","PASSWORD")
    data = api.get_states(time_secs=0,icao24=icao)
    for s in data.states:
        return ("longitude:%r, latidude%r,altitude:%r,vitesse:%r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity))



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

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('TOKEN')
