import discord
from bs4 import BeautifulSoup
from discord.ext import commands
from urllib.request import urlopen, Request
TOKEN = "XXXXXXXXXXXXX"

intents = discord.Intents.all()

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(command_prefix="!",intents=intents)

# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'{bot.user} successfully logged in!')



@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    # print(message.author)
    # print(message.channel)
    # print(message.content)
    # print("=====")
    if (message.author == bot.user) or (message.channel.name != 'holiday-of-the-dayyyyyyy'): 
        return
    
    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)



# Start each command with the @bot.command decorater
url = 'https://nationaltoday.com/today/'
@bot.command()
async def today(ctx): # The name of the function is the name of the command
    print("Running Today Command") # this is the text that follows the command
    # await ctx.send(int(arg) ** 2) # ctx.send sends text in chat
    req = Request(url)
    req.add_header('Content-Type', 'application/json')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')

    page = urlopen(req)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.get_text())
    # print("-------------------------")

    ret = ""
    for link in soup.find_all("h3", class_='holiday-title'):
        print(link.text)
        ret += (link.text)
        ret += "\n"

    ret += "COURTESY OF nationaltoday.com\n"
    await ctx.send(ret)


bot.run(TOKEN)
