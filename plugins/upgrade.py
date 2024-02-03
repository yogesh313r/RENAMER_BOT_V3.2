"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 45  🇮🇳/🌎 0.5$  per Month 📅 
	
	**VIP 2 **
	Daily Upload limit Unlimited 
	Price Rs  85  🇮🇳/🌎 1$  per Month 📅
	
	
	Pay Using Upi I'd ```yogeshfamily01@okaxis```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "http://t.me/Yogi_YogiBot")])
        			InlineKeyboardButton("Google Pay",url = "yogeshfamily01@okaxis")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 45  🇮🇳/🌎 0.5$  per Month 📅
	
	**VIP 2 **
	Daily Upload limit Unlimited
	Price Rs  85  🇮🇳/🌎 1$  per Month 📅
	
	
	Pay Using Upi I'd ```9480251952@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mrlokaman")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/lokamanchendekar"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/los89jy0")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
