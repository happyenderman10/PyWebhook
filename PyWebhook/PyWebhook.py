import requests 
from requests import delete 
from datetime import date
import random,string
def dele(webhook):
    delete(webhook)
def send(webhook,msg):
    data = {
        "content" : msg
    }
    requests.post(webhook,json=data)
def info(webhook):
    wh = requests.get(webhook).json()
    use = wh['name']
    id = wh['id']
    ch = wh['channel_id']
    guild = wh['guild_id']
    token = wh['token']
    print(f"""
    Username : {use}
    Id :{id}
    Channel id : {ch}
    Guild id : {guild}
    Token : {token}
    """)
    ask = input('Do you want to save this on a txt file (yes/no) ? ')
    if ask == 'yes':
        today = date.today()
        log = f"""
    Username : {use}
    Id :{id}
    Channel id : {ch}
    Guild id : {guild}
    Token : {token}
    """
        txt = ('').join(random.choices(string.ascii_letters, k=4))
        f = open(f'wh_info_{today}_{txt}.txt', "a+")
        f.write(log)
        f.close()
    if ask == 'no':
        print(' ')
def help():
    print("""
    === ʜᴇʟᴘ ===
    1 => send 
    Usage : PyWebhook.send('webhook url','message')  
    What it do : Send a message with webhook 
    2 => dele
    Usage : PyWebhook.dele('webhook url')
    What it do : Delete a webhook without any Permsions Or even Begin on the guild 
    3 => info
    Usage : PyWebhook.info('Webhook url')
    What it do : Give info Of a webhook 
    4 =>  Help
    Usage : PyWebhook.help()
    What it do : Give Module Features
    === ʜᴇʟᴘ ===
    """)
