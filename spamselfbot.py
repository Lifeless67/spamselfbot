import discord
from discord.ext import commands
prefix = ('ADD YOUR PREFIX HERE!!')

client = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)
token = "ADD YOUR TOKEN HERE!!"
 
@client.event
async def on_ready():
    print("Selfbot Online!")

@client.command()
async def TEST(ctx):
    await ctx. message.delete()
    await ctx.send("Hello!")

@client.command()
async def LOLG(ctx):
    await ctx. message.delete()
    await ctx.send("MEN")

@client.command()
async def pingspam(ctx):
    await ctx. message.delete()
    for f in range(50): await ctx.send("@everyone")

@client.command()
async def help(ctx):
    await ctx. message.delete()
    await ctx.send("**Liquify Selfbot** \n `1: .help (brings up this menu)` \n `2: .pingspam (spams @everyone 50 times)` \n `3: .spam [message] (spams the message 100 times)`  ")
    
@client.command()
async def spam(ctx, arg1):
    await ctx. message.delete()
    for f in range(100): await ctx.send(arg1)

client.run(token, bot=False)