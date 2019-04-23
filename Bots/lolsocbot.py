import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        msg = "Hello {0.author.mention}".format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

client.run('NTcwMjgwMjMwMTg3NTY1MDU2.XL86Qw.GyFP-zN1cxco28qj8HexiqvU_lw')
