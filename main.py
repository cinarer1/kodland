import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

foto = mem1.jpg
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content) 

@client.event
async def on message
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

@client.event
async def on_message(message):
    if message.aauthor == client.user:
        return
    if message.content.startswitch("$mem"):
        await message.channel.send(foto)

        
intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('token')

client.run(MTI5OTA2MTMzMDYyNzUyNjc0OA.GFu6W7.zMbbXEtEZkytASMSf9TfqB3YyDC4aSAT2ahWhY)
