# Daily Info Agent 🤖

בוט טלגרם ששולח לך כל בוקר הודעה עם:
- מזג האוויר היום 🌤
- חדשות מאתמול 📰
- בדיחה יומית 💡

### איך זה עובד?
הפרויקט רץ אוטומטית בכל בוקר בעזרת **GitHub Actions** ושולח הודעה דרך **Telegram Bot API**.

### טכנולוגיות
- Python
- Requests
- python-telegram-bot
- OpenWeatherMap API
- NewsAPI
- official-joke-api

### התקנה מהירה
1. **התקן תלויות:**
   ```bash
   pip install -r requirements.txt
   ```

2. **הגדר API Keys** (ראה `SETUP.md` לפרטים מלאים):
   - Telegram Bot Token
   - OpenWeatherMap API Key
   - NewsAPI Key
   - Chat ID שלך

3. **הרץ את הבוט:**
   ```bash
   python daily_agent.py
   ```

### הגדרה מפורטת
ראה את הקובץ `SETUP.md` להנחיות מפורטות על:
- איך לקבל API Keys
- איך למצוא את Chat ID שלך
- איך להגדיר Environment Variables
- פתרון בעיות נפוצות

### שימוש ב-GitHub Actions
- שמרי את ה-Secrets:
  - TELEGRAM_TOKEN
  - CHAT_ID
  - WEATHER_API_KEY
  - NEWS_API_KEY
- הבוט ירוץ אוטומטית כל יום ב-08:00 שעון ישראל 🎉
