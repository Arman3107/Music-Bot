#Codigo main de ejecucion del codigo principal
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import Musica
#Se exportan las distintas librerias utilizadas en el codigo fuente 
cogs = [Musica]

intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents = discord.Intents.all())
#Ejecucion del comando ! en discord 

for i in range(len(cogs)):
    cogs[i].setup(client)



client.run("OTEwNzIxNzkyOTA4MzQ5NDUw.YZW9ww.jsp6z_BGYWBw8mIrmvjvJoBIVkc")
#Se utiliza el token entregado por el discord developer para la ejecucion del codigo
#El token es de uso personal, si se quiere utilizar el bot debes usar un token generado
#de forma personal en el discord developer
