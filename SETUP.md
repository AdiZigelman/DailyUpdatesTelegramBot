# Setup Guide for Daily Info Agent

## Project Overview
This is a Telegram bot that sends daily morning messages with:
- Weather information 🌤
- Yesterday's news 📰
- Daily quote or joke 💡

## Prerequisites
- Python 3.8 or higher
- A Telegram account
- Internet connection

## Step 1: Get API Keys

### 1.1 Telegram Bot Token
1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the token (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 1.2 OpenWeatherMap API Key
1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Go to "My API Keys" section
4. Copy your API key

### 1.3 NewsAPI Key
1. Go to [NewsAPI](https://newsapi.org/)
2. Sign up for a free account
3. Copy your API key from the dashboard

## Step 2: Get Your Chat ID

### Option A: Using the Bot (Recommended)
1. Start a chat with your bot
2. Send any message to the bot
3. Run this command in your browser:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
4. Look for the "chat" section and find your "id" number

### Option B: Using @userinfobot
1. Search for `@userinfobot` in Telegram
2. Send `/start` to get your Chat ID

## Step 3: Configure Environment Variables

### For Local Development
1. Copy `.env.example` to `.env`
2. Fill in your actual values:
   ```bash
   TELEGRAM_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
   CHAT_ID=123456789
   WEATHER_API_KEY=your_openweathermap_key_here
   NEWS_API_KEY=your_newsapi_key_here
   ```

### For GitHub Actions (Automated Daily Runs)
1. Go to your GitHub repository
2. Click "Settings" → "Secrets and variables" → "Actions"
3. Add these repository secrets:
   - `TELEGRAM_TOKEN`
   - `CHAT_ID`
   - `WEATHER_API_KEY`
   - `NEWS_API_KEY`

## Step 4: Test Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables (Windows PowerShell):
   ```powershell
   $env:TELEGRAM_TOKEN="your_token_here"
   $env:CHAT_ID="your_chat_id_here"
   $env:WEATHER_API_KEY="your_weather_key_here"
   $env:NEWS_API_KEY="your_news_key_here"
   ```

3. Run the bot:
   ```bash
   python daily_agent.py
   ```

## Step 5: Deploy to GitHub Actions

The bot will automatically run every day at 8:00 AM Israel time (5:00 AM UTC) using GitHub Actions.

## Troubleshooting

### Common Issues:
1. **"Missing required environment variables"** - Make sure all environment variables are set
2. **"ModuleNotFoundError: No module named 'telegram'"** - Run `pip install -r requirements.txt`
3. **"Chat not found"** - Make sure you've started a conversation with your bot
4. **API errors** - Check if your API keys are valid and have sufficient quota

### Testing Individual APIs:
- Weather: Check if your OpenWeatherMap key works
- News: Verify your NewsAPI key is active
- Telegram: Test bot token with a simple message

## Support
If you encounter issues:
1. Check the error messages in the console
2. Verify all API keys are correct
3. Ensure your bot has permission to send messages
4. Check if the APIs are working (try the URLs in a browser)

## Notes
- The bot sends messages in Hebrew
- Weather is set to Tel Aviv by default (change CITY variable to customize)
- Free API tiers have rate limits - the bot is designed to run once daily
- GitHub Actions will run automatically every day at 8:00 AM Israel time 