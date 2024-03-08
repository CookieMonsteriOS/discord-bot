import discord
from discord.ext import commands

# Define the bot's command prefix
bot = commands.Bot(command_prefix='!')

# Event that occurs when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Command to greet users
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Command to display information about the bot
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Bot Information", description="This is a Discord bot coded in Python!", color=0x00ff00)
    embed.add_field(name="Creator", value="Your Name", inline=False)
    embed.add_field(name="Library", value="discord.py", inline=False)
    embed.set_footer(text="Bot Tutorial")
    await ctx.send(embed=embed)

# Run the bot with your bot token
bot.run('your_bot_token_here')
