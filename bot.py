# Importações
import discord
from discord.ext import commands

# Intents e criação do bot
intents = discord.Intents.all() # Ativa todas as intents
bot = commands.Bot('!r', intents=intents)


#Comando "!rhola"
@bot.command(aliases=["hola"])
async def olá(ctx): # Crear la función asincrónica
    autor = ctx.author.mention # Mencion a ti
    await ctx.send(f'Hola, {autor}!') # Envia uma mensage

bot.run('Tu Token') # bot
