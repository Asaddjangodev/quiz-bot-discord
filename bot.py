import discord
from environs import Env # new
from dotenv import load_dotenv
import requests
import os
import json
import asyncio

load_dotenv()

env = Env() # new
env.read_env() # new

# Создаем объект intents с настройками по умолчанию
intents = discord.Intents.default()
# Включаем доступ к содержимому сообщений
intents.message_content = True

client = discord.Client(intents=intents)

def get_question():
    qs = ''
    id = 1
    answer = 0
    response = requests.get("https://aqueous-thicket-58289-3c131321ece5.herokuapp.com/api/random/")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + '\n'

    for item in json_data[0]['answer']:
        qs += str(id) + '. ' + item['answer'] + "\n"

        if item['is_correct']:
            answer = id
        id += 1

    return(qs, answer)


@client.event
async def on_ready():
    print(f"Бот {client.user} успешно запущен!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$question"):
        qs, answer = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit()

        try:
            guess = await client.wait_for('message', check=check, timeout=2.0)
        except asyncio.TimeoutError:
            return await message.channel.send("Sorry, you took too long")

        if int(guess.content) == answer:
            await message.channel.send("You are right!")
        else:
            await message.channel.send("Oops. That is not right.")

client.run(os.getenv("DISCORD_TOKEN"))
