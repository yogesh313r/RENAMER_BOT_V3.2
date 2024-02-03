import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6475149749:AAEQt9M91pjiNCBF_lkxgVEXdq77S1lT_n0")

API_ID = int(os.environ.get("API_ID", "25393663"))

API_HASH = os.environ.get("API_HASH", "46fb840e6cb4b84d582c44ebbf703251")

STRING = os.environ.get("STRING", "Hi Bro")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
