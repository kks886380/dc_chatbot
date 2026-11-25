import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)


@bot.listen("on_ready")
async def on_ready():
    print(f"已登入：{bot.user}")


@bot.slash_command(name="hi", description="say hi")
async def hi(ctx):
    await ctx.respond("hi")

if token:
    bot.run(token)
else:
    print("找不到 DISCORD_TOKEN，請檢查 .env 檔案。")