import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from keep_alive import keep_alive
import os

TOKEN = os.getenv('DISCORD_TOKEN')  # ซ่อนไม่ให้ใส่ token ตรงๆ
CHANNEL_ID = '1228571438701875202'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_reminder():
    print("Sending reminder...")
    channel = client.get_channel(int(CHANNEL_ID))
    if channel:
        await channel.send('อย่าลืม! เช็คอิน Cardekho')

scheduler = AsyncIOScheduler()
scheduler.add_job(send_reminder, 'cron', day_of_week='mon-fri', hour=2, minute=0)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    scheduler.start()

keep_alive()  # สำคัญ! เพื่อให้ Render มีหน้าเว็บไว้สำหรับ UptimeRobot ping
client.run(TOKEN)
