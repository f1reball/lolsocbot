from discord.ext import commands

TOKEN =
bot = commands.Bot(command_prefix = "!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello {}".format(ctx.author.mention))

@bot.command()
async def FF(ctx, week):
    if "Executive" in (role.name for role in ctx.author.roles):
        await ctx.send("Welcome to UNSW LoLSoc's Week {} Friendly Friday, an event PROUDLY sponsored by Arc Clubs".format(week))
    elif "Subcommittee" in (role.name for role in ctx.author.roles):
        await ctx.send("Welcome to UNSW LoLSoc's Week {} Friendly Friday, an event PROUDLY sponsored by Arc Clubs".format(week))
    else:
        pass


bot.run(TOKEN)
