import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

ALLOWED_CHANNEL_ID = 1354809111484698804  # Replace with the desired channel ID

@bot.event
async def on_ready():
    activity = discord.Game(name="Watching Anime 🎥")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"Logged in as {bot.user}")

@bot.command()
async def watching(ctx, *, anime_name: str):
    if ctx.channel.id == ALLOWED_CHANNEL_ID:
        await ctx.channel.send(f"{ctx.author.mention} is now watching: {anime_name}!")
        activity = discord.Activity(type=discord.ActivityType.watching, name=anime_name)
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await ctx.send(f"Status updated and message sent to channel.")
    else:
        await ctx.send(f"This command can only be used in <#{ALLOWED_CHANNEL_ID}>.")

bot.run(os.environ["MTM1NDU2MDM1MzY5ODA1NDMzNA.G40cVM.OyPk4zzKF_w4ZMkU3njU8w3KN3z6FXc9B6UJcU"])

