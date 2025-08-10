
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "🌸 Welcome to SweetTashaBot 🌸\n\n"
        "🚀 Enjoy your *FREE trial* today!\n"
        "💼 SweetTashaBot offers 24/7 automated support, premium features, "
        "and instant replies to your questions.\n\n"
        "Type /help to see what I can do."
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🤖 *SweetTashaBot Commands:*\n\n"
        "/start - Start the bot and see welcome message\n"
        "/help - Show this help message\n"
        "/trial - Get your free trial info"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

# Trial command
async def trial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    trial_text = (
        "🎁 Your *FREE Trial* includes:\n"
        "✅ Unlimited bot usage for 7 days\n"
        "✅ Priority support\n"
        "✅ Access to premium commands\n\n"
        "To upgrade, contact us at: support@sweettasha.com"
    )
    await update.message.reply_text(trial_text, parse_mode="Markdown")

# Echo any message
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💬 You said: {update.message.text}")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        logger.error("BOT_TOKEN not found in environment variables")
        return

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("trial", trial))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("SweetTashaBot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
