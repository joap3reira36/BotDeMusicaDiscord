# BotMusicDisc

A Discord music bot built with Python, wavelink and Lavalink. Plays music from YouTube, manages a queue and comes with a bit of personality.

---

## Requirements

- Python 3.10+
- A [Lavalink](https://github.com/lavalink-devs/Lavalink) server running locally or remotely
- A Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications)

---

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project folder
```
DISCORD_TOKEN=your_token_here
LAVALINK_URI=you_uri_here
LAVALINK_PASSWORD=your_password_here
```

4. Start your Lavalink server, then run the bot
```bash
python bot.py
```

---

## Commands

| Command | Description |
|---|---|
| `!play <name or URL>` | Plays a song or adds it to the queue |
| `!skip` | Skips the current song |
| `!clean_queue` | Clears the queue |
| `!sobre` | Info about the bot |
| `!ajuda` | Shows this command list |

---

## Project Structure

```
project/
├── bot.py
├── .env          ← not on GitHub
├── .gitignore
└── requirements.txt
```

---

## Built With

- [discord.py](https://github.com/Rapptz/discord.py)
- [wavelink](https://github.com/PythonistaGuild/WaveLink)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

*Made in Brazil 🇧🇷 — 2026*
