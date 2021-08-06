#from telethon import TelegramClient
import time
from telethon.sync import TelegramClient, events
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--payload", help = "String to be sent to the bot or channel")
parser.add_argument("-b", "--bot", help = " target @bot")
parser.add_argument("-c", "--command", help = " command to be sent to target @bot")
parser.add_argument("-t", "--timeout", help = " time to listen before send close the connection")


if not (args.payload):
    print("Please specify the payload using -p ")
    exit(1)

if not (args.bot):
    print("Please specify the bot using -p @bot  ")
    exit(1)

if not (args.command):
    print("Please specify the bot using -c command  ")
    exit(1)

command = args.command
bot = args.bot
payload = args.payload
timeout = int(args.timeout)

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')


client = TelegramClient('name', api_id, api_hash)

async def main():
    await client.send_message(bot, '/start')
    print ("Sending payload: " + command + " " + payload )
    await client.send_message(bot, command + ' ' + payload)
    print ("Dumping responses .. (if any)")

    @client.on(events.NewMessage())
    async def handler(event):
      #await event.reply('got it!')
      text = event.message.message
      print (bot + ":" + event.message.message)

    time.sleep(timeout)


with client:
    try:
        client.loop.run_until_complete(main())
    except:
        print ("Error connecting to Telegram!")
        
        
        

