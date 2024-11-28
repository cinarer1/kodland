import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

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
    if message.content.startswith("doğa")
      await message.channel.send("İşte bazı İpucları: Her ay bir fidan dikebilir, yerlere çöp atanları uyarabilir, araban doğaya zarar veriyorsa bakımını yaptırabilir, sigara bağımlılığın varsa hergün azaltmayı deneyebilirsin ve daha fazlası")
  
        
intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('token')

client.run(MTI5OTA2MTMzMDYyNzUyNjc0OA.GFu6W7.zMbbXEtEZkytASMSf9TfqB3YyDC4aSAT2ahWhY)
