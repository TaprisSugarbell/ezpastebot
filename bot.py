from pyrogram import Client, idle
try:
    from config import Config
except:
    from sample_config import Config

api_id = Config.api_id
api_hash = Config.api_hash
Token = Config.Token
app = Client("paztezbot", apid_id=api_id, api_hash=api_hash, bot_token=Token)
app.start()
print('>>> BOT STARTED')
idle()
app.stop()
print('\n>>> BOT STOPPED')
