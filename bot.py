import discord

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


client.run("MTM5Mjc5Mjc5MjgzMjY3NTg5MA.Gtk5ao.HVQbFg_JyRtFL3SrlJub_JlnRd7SNV6G5IyQjQ")
