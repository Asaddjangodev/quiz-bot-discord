import discord
from environs import Env # new

env = Env() # new
env.read_env() # new

# Создаем объект intents с настройками по умолчанию
intents = discord.Intents.default()
# Включаем доступ к содержимому сообщений
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Бот {client.user} успешно запущен!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("hello, I am a bot")


client.run(env.str("DISCORD_TOKEN"))
