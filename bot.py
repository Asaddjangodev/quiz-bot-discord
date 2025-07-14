import discord
from environs import Env # new
from dotenv import load_dotenv
import requests
import os
import json
import asyncio
import requests

load_dotenv()

env = Env() # new
env.read_env() # new

# Создаем объект intents с настройками по умолчанию
intents = discord.Intents.default()
# Включаем доступ к содержимому сообщений
intents.message_content = True

client = discord.Client(intents=intents)

def get_score():
    leaderboard = ''
    id = 1
    response = requests.get("http://127.0.0.1:8000/api/score/leaderboard/")
    json_data = json.loads(response.text) # Автоматически парсит JSON


    for item in json_data:
        leaderboard += str(id) + ' ' + item['name'] + '. ' + str(item['points']) + '\n'
        id += 1
    return(leaderboard)
def update_score(user, points):
    url = 'http://127.0.0.1:8000/api/score/update/'
    new_score = {'name': user, 'points': points}
    x = requests.post(url, data = new_score)

    return

def get_question():
    qs = ''
    id = 1
    answer = 0
    points = 0
    response = requests.get("http://127.0.0.1:8000/api/random/")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + '\n'

    for item in json_data[0]['answer']:
        qs += str(id) + '. ' + item['answer'] + "\n"

        if item['is_correct']:
            answer = id
        id += 1

    points = json_data[0]['points']

    return(qs, answer, points)


@client.event
async def on_ready():
    print(f"Бот {client.user} успешно запущен!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$score'):
        leaderboard = get_score()
        await message.channel.send(leaderboard)

    if message.content.startswith("$question"):

        qs, answer, points = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.content.isdigit() == True

        try:
            guess = await client.wait_for('message', check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send("Sorry, you took too long")

        if int(guess.content) == answer:
            user = guess.author
            msg = str(guess.author.name) + ' got it right! +' + str(points) + ' points'
            await message.channel.send(msg)
            update_score(user, points)
        else:
            await message.channel.send("Oops. That is not right.")

client.run(os.getenv("DISCORD_TOKEN"))
