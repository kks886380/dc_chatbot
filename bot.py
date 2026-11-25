import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)


@bot.listen("ready")
async def on_ready():
    print(f"已登入：{bot.user}")


if token:
    bot.run(token)
else:
    print("找不到 DISCORD_TOKEN，請檢查 .env 檔案。")