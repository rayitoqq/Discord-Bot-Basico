import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot('!r', intents=intents)


@bot.command(aliases=["hola"])
async def olá(ctx): 
    autor = ctx.author.mention 
    await ctx.send(f'Hola, {autor}!') 

bot.run('Tu Token') 
