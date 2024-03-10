import webbrowser

import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, MessageHandler, Filters

def search_and_download_torrent(search_name):
    # Construct the search URL
    search_url = f"https://thepiratebay10.org/search/{search_name}/1/99/0"

    # Send a GET request to the search URL
    response = requests.get(search_url)

    # Parse the HTML content of the search page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the search results
    search_results = soup.select('div#main-content')

    if search_results:
        for result in search_results:
            magnet_link = result.select_one('a[href^=magnet]')

            if magnet_link:
                magnet_link = magnet_link['href']

                # Open the magnet link in the default torrent client
                webbrowser.open(magnet_link)
                print("Torrent downloaded successfully.")
                break
        else:
            print("No magnet link found in the search results.")
    else:
        print("No search results found.")

def handle_text(update, context):
    user_id = update.message.chat_id
    text_received = update.message.text

    print(f"Received text: {text_received}")

    # Call the function to search and download the torrent
    search_and_download_torrent(text_received)

def run_telegram_bot():
    updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)  # Replace with your actual bot token
    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text & ~Filters.command, handle_text)
    dp.add_handler(text_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    run_telegram_bot()
