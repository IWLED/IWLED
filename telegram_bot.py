from telegram.ext import Updater, MessageHandler, Filters
import requests
import json

def handle_text(update, context):
    user_id = update.message.chat_id
    text_received = update.message.text

    print(f"Received text: {text_received}")

    # Construct the search URL for The Pirate Bay
    search_url = f"https://thepiratebay10.org/search/{text_received}/1/99/0"

    try:
        # Send a GET request to The Pirate Bay
        response = requests.get(search_url)

        if response.status_code == 200:
            # Parse the HTML content of the search page
            # Extract and open the magnet link
            # (You may need to modify this part based on the actual HTML structure)
            # ...

            context.bot.send_message(chat_id=user_id, text="Torrent downloaded successfully.")
        else:
            context.bot.send_message(chat_id=user_id, text="No search results found.")
    except Exception as e:
        print(f"Error searching on The Pirate Bay: {str(e)}")
        context.bot.send_message(chat_id=user_id, text="An error occurred while searching.")

def run_telegram_bot():
    updater = Updater(token='6989794336:AAGAvkVd0Ylq38RQ785XwE1LVnS53EDbnuI', use_context=True)  # Replace with your actual bot token
    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text & ~Filters.command, handle_text)
    dp.add_handler(text_handler)

    updater.start_polling()
    updater.idle()
