import discord
TOKEN = "NTcwMjgwMjMwMTg3NTY1MDU2.XL86Qw.GyFP-zN1cxco28qj8HexiqvU_lw"

client = discord.Client()

@client.event
async def on_message(message):
    #hello
    if message.content.startswith("!hello"):
        msg = "Hello {0.author.mention}".format(message)
        if "Exec" or "Subcom" in (role.name for role in message.author.roles):
            print("Yay")
        await message.channel.send(msg)

    #FF
    if message.content == "!FF":
        msg = "Welcome to UNSW LoLSoc's Week {} Friendly Friday, an event PROUDLY sponsored by Arc Clubs"




client.run(TOKEN)
