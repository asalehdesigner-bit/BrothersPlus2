import os
import json
from flask import Flask
from threading import Thread
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# إعداد سيرفر خفيف عشان يفضل البوت شغال 24 ساعة
app = Flask('')
@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# كود البوت الأساسي
def start(update, context):
    update.message.reply_text('أهلاً بك في BrothersPlus! كيف يمكنني مساعدتك اليوم؟')

def main():
    # بنجيب التوكن من الإعدادات اللي هنحطها في Render
    TOKEN = os.environ.get('BOT_TOKEN')
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if name == 'main':
    keep_alive()
    main()
