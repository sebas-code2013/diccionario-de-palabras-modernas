import discord
from discord.ext import commands
from tarea2 import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="/:", intents=intents)
times_message = 0
passwordd = 0

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hola(ctx):
    global times_message
    times_message += 1
    await ctx.send("hola exitoso😉")

@bot.command()
async def chao(ctx):
    global times_message
    times_message += 1
    await ctx.send("adios we :v")

@bot.command()
async def proyectate(ctx):
    global times_message
    times_message += 1
    await ctx.send("noo me proyectoo😩")

@bot.command()
async def password(ctx):
    global passwordd, times_message
    times_message += 1
    passwordd = gen_pass(12)
    await ctx.send("tu contraseña de exitoso es: " + str(passwordd))

@bot.command()
async def mensajes(ctx):
    global times_message
    times_message += 1
    await ctx.send("me has escrito " + str(times_message) + " veces")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run("token")
