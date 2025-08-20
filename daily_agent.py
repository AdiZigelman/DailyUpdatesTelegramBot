import requests
from telegram import Bot
import os
import sys
import asyncio
import feedparser

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
CITY = "Tel Aviv"
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric&lang=he"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"{temp}° - {desc}"
    except Exception as e:
        print(f"Error getting weather: {e}")
        return "לא ניתן לקבל מידע על מזג האוויר"


def get_news(n=5):
    try:
        feed = feedparser.parse("https://www.ynet.co.il/Integration/StoryRss2.xml")
        if feed.entries:
            headlines = [entry.title for entry in feed.entries[:n]]
            return "\n".join([f"{i+1}. {title}" for i, title in enumerate(headlines)])
        return "אין חדשות זמינות"
    except Exception as e:
        print(f"Error getting news: {e}")
        return "לא ניתן לקבל חדשות"

def get_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("setup", "אין בדיחה להיום :)")
    except Exception as e:
        print(f"Error getting quote: {e}")
        return "לא ניתן לקבל ציטוט"

async def send_message():
    try:
        bot = Bot(token=TELEGRAM_TOKEN)
        weather = get_weather()
        news = get_news()
        joke = get_joke()

        message = (
        f"🌞 בוקר טוב!\n\n"
        f"🌤 מזג האוויר להיום:\n {weather}\n\n"
        f"📰 חדשות חמות:\n{news}\n\n"
        f"💡 הבדיחה היומית:\n\"{joke}\"\n\n"
        f"☕ שיהיה לך יום מדהים!"
    )

        await bot.send_message(chat_id=CHAT_ID, text=message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(send_message())
