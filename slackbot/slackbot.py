from slack import WebClient
import os
import time

# Create a slack client
slack_bot = WebClient(token='xoxb-1905444677763-1912131503796-EoUjInoPDje7c4fc5thIp1Bm')



slack_bot.chat_postMessage(channel = '#test', text = f"Hello")



