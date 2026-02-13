# Mashup Assignment

A Python-based mashup generator that downloads YouTube videos of a specified singer, extracts audio, trims clips, and merges them into a single MP3 file.  
Includes both a CLI tool and a Flask web interface.

---

## 📁 Project Structure

```
Mashup-Assignment/
├── 102303871.py      # CLI script
├── app.py            # Flask web app
├── templates/
│   └── index.html    # Frontend
└── README.md
```

---

## ⚙️ Requirements

- Python 3.x  
- FFmpeg (audio processing)  
  - Mac: `brew install ffmpeg`  
  - Windows: Install and add to PATH  
- Node.js (required for yt-dlp YouTube access)  
  - Mac: `brew install node`

Install Python dependencies:

```bash
pip install flask yt-dlp pydub
```

---

## 🚀 Usage

### 1️⃣ CLI

```bash
python3 102303871.py "<SingerName>" <NumberOfVideos> <Duration> <OutputFileName>
```

Example:

```bash
python3 102303871.py "Sidhu Moose Wala" 20 30 mashup.mp3
```

**Parameters:**
- `SingerName` – Artist name  
- `NumberOfVideos` – Must be > 10  
- `Duration` – Clip duration in seconds (Must be > 20)  
- `OutputFileName` – Final MP3 file name  

---

### 2️⃣ Web App

Start server:

```bash
python3 app.py
```

Open:

```
http://127.0.0.1:5000/
```

Fill the form (Singer, Count, Duration, Email) and submit.  
Mashup is processed and delivered automatically.

---

## 📝 Notes

- Stable internet required.
- Node.js handles YouTube JS challenges.
- Temporary files are auto-deleted (`temp_downloads/`).

---

## 🛠 Tech Stack

Python • Flask • yt-dlp • pydub • FFmpeg • HTML

---

**Author:** 102303871
