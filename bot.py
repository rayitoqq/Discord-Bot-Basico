import discord
from discord import app_commands
import random

id_del_servidor =  # ID de tu servidor

class Cliente(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.sincronizado = False  # Usamos esto para evitar que el bot sincronice los comandos más de una vez

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.sincronizado:  # Verificar si los comandos slash han sido sincronizados
            await arbol.sincronizar(guild=discord.Object(id=id_del_servidor))  # También puedes dejar en blanco el ID del servidor para aplicarlo a todos los servidores, pero esto tomará entre 1 y 24 horas para que funcione.
            self.sincronizado = True
        print(f"Conectado como {self.user}.")

cliente_discord = Cliente()
arbol = app_commands.CommandTree(cliente_discord)

@arbol.comando(guild=discord.Object(id=id_del_servidor), nombre='github', descripción='Perfil de GitHub')  # Comando específico para tu servidor
async def slash2(interacción: discord.Interacción):
    await interacción.respuesta.enviar_mensaje(f"https://github.com/rayitoqq", efímero=False)

@arbol.comando(guild=discord.Object(id=id_del_servidor), nombre='hola', descripción='Un lindo mensaje solo para ti')  # Comando específico para tu servidor
async def slash4(interacción: discord.Interacción):
    await interacción.respuesta.enviar_mensaje(f"¡Hola, bienvenido/a a mi servidor de pruebas! :)", efímero=True)

@arbol.comando(guild=discord.Object(id=id_del_servidor), nombre='dado', descripción='Tira un dado de 6 caras')  # Comando específico para tu servidor
async def slash3(interacción: discord.Interacción):
    número = random.randint(1, 6)
    await interacción.respuesta.enviar_mensaje(f"Número {número}", efímero=False)

cliente_discord.run('pon aquí tu token')
