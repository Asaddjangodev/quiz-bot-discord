# quiz-bot-discord
🎮 QuizBot - Discord Quiz Bot🤖

📝Project Description

QuizBot is an interactive Discord bot that allows you to host engaging quizzes with questions from various categories. The bot uses Django REST Framework as a backend to store questions and player statistics.


🌟Key Features

🎯Timed quiz sessions

🏆Player rating system

⚙️Admin panel for adding new questions

🔌REST API for integration with other services


💻Technologies

Backend: Django 5, Django REST Framework

Database: SQLite3

Discord bot: Discord API discord.py (version 2.0+)

Deployment: Heroku (optional)


🎮Bot Usage

🔹Basic Commands

$question - to get a question▶️

<img width="657" height="225" alt="image" src="https://github.com/user-attachments/assets/6202edc4-0c98-4af0-a209-0a1fafcf62e1" />

$score - to get a list of leaders

<img width="650" height="271" alt="image" src="https://github.com/user-attachments/assets/5dd04790-48b5-4276-a22f-52ec844334c5" />


API Endpoints

The bot uses following API endpoints:

GET /api/random/ - Get questions 🎲 

POST /api/score/update/ - Update score 💯

GET /api/score/leaderboard/ - Get leaderboard  📊 
