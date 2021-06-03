from discord.ext import commands
import random

# bot init
bot = commands.Bot(command_prefix = '!')

# idea bot code
@bot.command(name = "idea", help = "get a project idea")
async def idea(ctx):
    await ctx.send("ideas are hard")
    await ctx.send("but it's okay :D i think you should. . .")

    topics = ['chat bot', 'cli', 'game', 'web bot', 'browser extension', 'api', 'web interface']
    areas = ['note taking', 'social life', 'physical fitness', 'mental health', 'pet care']

    idea = f'create a new {random.choice(topics)} that helps with {random.choice(areas)} :slight_smile:'
    await ctx.send(idea)

# basic calculator bot code
@bot.command(name = "calc", help = "perform a basic calculation of +, -, *, or /")
async def calc(ctx, x: float, fn: str, y: float):
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)
    else:
        await ctx.send("sorry i can only do 4 basic functions :disappointed:")

# token handling
with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("token file read :D")
    bot.run(TOKEN)