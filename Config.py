#rename to Config.py this congfig is for force subscribe module
import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "").split()))
    SUDO_USERS.append(1084619043)
    SUDO_USERS = set(SUDO_USERS)
  else:
    BOT_TOKEN = "1484701846:AAFBP9KkqJwhtfRgvssr4_LB-8CP9567FFQ"
    DATABASE_URL = "postgres://sbugawjkpjgivk:ba116845f2f78162850601e28b29ea3970cb5d7f25037ffe9369e7bc3afbddc7@ec2-54-85-13-135.compute-1.amazonaws.com:5432/d3foq17p28s9e9"
    APP_ID = "1822414"
    API_HASH = "46f1888d3f68396bad08c92ac4d7f00a"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(1084619043)
    SUDO_USERS = list(set(SUDO_USERS))
    
    
    
class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @sushantgirdhar **"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /forcehelp__"
