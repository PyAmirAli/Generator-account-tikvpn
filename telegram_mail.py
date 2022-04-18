from telethon import TelegramClient , events , sync , connection
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)
import time
# API variables
api_id = API_ID
api_hash = "API_HASH"
client = TelegramClient(
    'session_name', api_id, api_hash)

#text 
error = "An error occured please try /generate again."
message = '/generate'
#get email fake


def mail():
    client.start()
    client.send_message("@fakemailbot",'/generate')
    time.sleep(1.5)
    for message in client.get_messages("@fakemailbot", limit=1):
        msg = message.message
        if msg == error:
            return "error"
        else:
            
            mail = msg[25:].split()
            return mail[0]

def code():
    client.start()
    for message in client.get_messages("fakemailbot", limit=1):
        msg = message.message.find("TikVPN")
        if msg == -1:
            find=("not")
        else:
            find=("find")
            msg_text = message.message.split()[43]
            
            a = msg_text.replace('[', '')
            text = a.replace(']', '')

            return text


