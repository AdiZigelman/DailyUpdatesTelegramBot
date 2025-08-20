# Daily Info Agent 🤖

**Daily Info Agent** is a Telegram bot that kickstarts your day with a concise morning update, including:

- 🌤 Today's weather  
- 📰 Top news headlines from yesterday  
- 💡 A daily joke  

The bot runs automatically every morning using **GitHub Actions** and delivers the updates directly to your Telegram.

---

## Features
- Daily weather updates using **OpenWeatherMap API**  
- News headlines powered by **NewsAPI**  
- Daily jokes from the **official-joke-api**  
- Fully automated scheduling with **GitHub Actions**  
- Easy setup with environment variables for sensitive keys  

---

## Technologies
- Python  
- `requests`  
- `python-telegram-bot`  
- OpenWeatherMap API  
- NewsAPI  
- official-joke-api  

---

## Quick Start

1. **Clone the repository and install dependencies:**
```bash
git clone https://github.com/AdiZigelman/DailyUpdatesTelegramBot.git
cd DailyUpdatesTelegramBot
pip install -r requirements.txt
```

2. **Set up your API Keys** (see `SETUP.md` for detailed instructions):  
   - Telegram Bot Token  
   - OpenWeatherMap API Key  
   - NewsAPI Key  
   - Your Telegram Chat ID  

3. **Run the bot locally:**
```bash
python daily_agent.py
```

---

## GitHub Actions Automation

The bot can run automatically every day using GitHub Actions:

- Add the following **Secrets** to your repository:  
  - `TELEGRAM_TOKEN`  
  - `CHAT_ID`  
  - `WEATHER_API_KEY`  
  - `NEWS_API_KEY`  

- The workflow is scheduled to run daily at **08:00 Israel time**.  

---

## Detailed Setup

Refer to `SETUP.md` for detailed instructions on:  
- Obtaining API keys  
- Finding your Telegram Chat ID  
- Configuring environment variables  
- Troubleshooting common issues  

---

## License

MIT License © 2025 Adi Zigelman
