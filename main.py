import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# سيرفر وهمي لإبقاء البوت مستيقظاً 24 ساعة على Render
app = Flask('')
@app.route('/')
def home():
    return "البوت يعمل بنجاح 24/7!"

def run():
    app.run(host='0.0.0.0', port=8080)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"تم تشغيل {bot.user} بنجاح!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

Thread(target=run).start()
bot.run(os.environ.get('DISCORD_TOKEN'))
