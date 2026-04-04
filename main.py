import discord
from discord.ext import commands
from bot_token import TOKEN

from bot_logic import detect_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def detect(ctx):
    if ctx.message.attachments:
        await ctx.send("Görsel algılandı.")
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            file_path = f"images/{filename}"
            await attachment.save(file_path)
            
            name, score = detect_class(file_path, "converted_keras-4/keras_model.h5", "converted_keras-4/labels.txt")
            await ctx.send(f"Algılanan sınıf: {name}, Güven Skoru: {score:.2f}")
            
    else:
        await ctx.send("Görsel Koy!")

bot.run(TOKEN)