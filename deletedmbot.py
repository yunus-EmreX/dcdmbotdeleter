import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

prefix = "?"
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} olarak giriş yaptı.")

@bot.command()
async def purge(ctx, count: int):
    await ctx.message.delete()  # ?purge komutunu çağıran mesajı sil

    # Belirtilen sayıda mesajı sil
    deleted = await ctx.channel.purge(limit=count)
    await ctx.send(f"{len(deleted)} mesaj silindi.", delete_after=5)  # Silinen mesaj sayısını gönder ve 5 saniye sonra sil

# Discord botunuzun token'ını buraya yapıştırın
bot.run("")
