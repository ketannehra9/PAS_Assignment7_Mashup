# PAS_Assignment7
# YouTube Mashup Generator


This project implements a command-line Python program and a Flask web service to create a mashup of audio clips from YouTube videos.

---

## 📌 Implementation Details

As required, all core functionality is implemented using libraries from **pypi.org**:

- **Downloading:** `yt-dlp`
- **Conversion to Audio:** `moviepy`
- **Audio Cutting:** `moviepy`
- **Merging Audio Files:** `moviepy`

---

## 📁 Project Structure

```
.
├── 102303871.py  
├── app.py      
├── templates/
│   └── index.html
└── README.md       
```

---

## ⚙️ Setup

### System Requirements
- Python 3.13+
- FFmpeg  
  ```bash
  brew install ffmpeg
  ```
- Node.js or Deno (for yt-dlp YouTube access)  
  ```bash
  brew install deno
  ```

### Install Dependencies

```bash
pip3 install yt-dlp "moviepy<2.0" flask
```

---

## 🚀 Usage

### CLI

```bash
python 102303871.py "<SingerName>" <NumberOfVideos> <AudioDuration> <OutputFileName>
```

Example:

```bash
python 102303871.py "Javed Ali" 12 25 output.mp3
```

Constraints:
- `NumberOfVideos > 10`
- `AudioDuration > 20`

---

### Web Service

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

Enter singer name, video count, duration, and email.  
The mashup is processed and delivered as a ZIP file.

---

## ✅ Features

- Input validation (`N > 10`, `Duration > 20`)
- Error handling for invalid inputs and network issues
- Automatic processing and file delivery
- Clean CLI + Web interface support

---

## 🛠 Tech Stack

Python • Flask • yt-dlp • MoviePy • FFmpeg

---

## Demo of web app
<img width="413" height="367" alt="demo-web-app" src="https://github.com/user-attachments/assets/00f11451-4ee8-4b1a-98fe-02b11d826a4d" />


