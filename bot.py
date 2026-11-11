import os
from datetime import time
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
APP_URL = "https://aganva03.github.io/planner/"
CHAT_ID = int(os.environ.get("CHAT_ID", "0"))

def open_button():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("Открыть планер", web_app=WebAppInfo(url=APP_URL))
    ]])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ваш планер:", reply_markup=open_button())

async def daily_reminder(context: ContextTypes.DEFAULT_TYPE):
    if CHAT_ID:
        await context.bot.send_message(CHAT_ID, "Отметьте привычки на сегодня ✓", reply_markup=open_button())

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    # 21:00 по Минску = 18:00 UTC
    app.job_queue.run_daily(daily_reminder, time=time(hour=18, minute=0))
    app.run_polling()

if __name__ == "__main__":
    main()
