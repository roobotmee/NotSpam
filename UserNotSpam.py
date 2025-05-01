from telethon import TelegramClient, events
from telethon.tl.functions.messages import HideReportSpamRequest
from telethon.tl.functions.account import UpdateProfileRequest, UpdateStatusRequest
from datetime import datetime
import time
import pytz
import asyncio

api_id = 12345
api_hash = 'api_hash_yozing'

client = TelegramClient('session', api_id, api_hash)

start_time = datetime.now()

@client.on(events.NewMessage(pattern='/info'))
async def info_handler(event):
    current_time = datetime.now(pytz.timezone('Asia/Tashkent')).strftime("%H:%M")
    uptime = datetime.now() - start_time
    hours, remainder = divmod(int(uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    status_message = f"📊 Bot holati haqida ma'lumot:\n\n"
    status_message += f"⌚️ Hozirgi vaqt: {current_time}\n"
    status_message += f"⏱ Ishlash vaqti: {hours} soat, {minutes} daqiqa\n"
    status_message += f"✅ Bot faol holatda\n"
    
    await event.respond(status_message)

async def main():
    userid = 'useridyozing'
    await client(HideReportSpamRequest(peer=userid))
    
    while True:
        tashkent_time = datetime.now(pytz.timezone('Asia/Tashkent'))
        current_time = tashkent_time.strftime("%H:%M")
        
        await client(UpdateProfileRequest(
            about=f"😎Bizda Aniq Vaqt:⌚️ {current_time}"
        ))
        
        await client(UpdateStatusRequest(offline=False))
        
        await asyncio.sleep(300)

client.start()
client.loop.create_task(main())
client.run_until_disconnected()
