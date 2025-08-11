# BisonHacks Mini‑Game Collection (Python • HTML/CSS/Flask • Pygame)

A small collection of game prototypes and mini experiences built for a hackathon. The repo includes both **web-based Flask games** and a **local Pygame mini‑game**, all themed around a Wakanda/Shuri arcade concept.

---

## 🎮 What’s inside

**Playable demos:**

1) **Wakanda: Word Scramble** (Pygame) — `mini.py`  
   Scramble/unscramble mini‑game powered by a `QuestionManager` that serves Wakanda/Black Panther themed words and hints.

2) **Wakanda: Rise of Shuri** (Flask) — `vamp.py`  
   A browser‑based arcade prototype (single‑file Flask app) that renders the UI and game logic into one page.

3) **Story + AI Companions + Shop (Flask)** — `hackey/app.py`  
   A more complete Flask web app with routes, save/load (`data/player_save.json`), AI companion selection (`data/ai_companions.json`), and gadgets/shop (`data/gadgets.json`).

There are additional experiments and older iterations under `hack_pro/` and `shuri_vampgame.py/`.

---

## 🛠️ Requirements

You can install dependencies per‑demo:

- **Pygame mini‑game**
  ```bash
  pip install pygame
  ```

- **Flask web apps**
  ```bash
  pip install flask
  ```

> Python 3.10+ recommended.

---

## ▶️ How to run

### 1) Word Scramble (Pygame)
```bash
python mini.py
```
- Window size: 800 × 600 (default inside code).  
- Uses `QuestionManager` (from `question_manager.py`) for themed word scrambles and hints.  
- Looks for optional sound assets in `assets/sounds/` (code will warn if they’re missing).

### 2) Wakanda: Rise of Shuri (Flask)
```bash
python vamp.py
```
- Starts a dev server at `http://127.0.0.1:5000/` (Flask debug mode).  
- Single‑file app that renders HTML/CSS/JS via `render_template_string`.

### 3) Story + AI Companions + Shop (Flask)
```bash
cd hackey
python app.py
```
- Uses templates in `hackey/templates/` and static assets under `hackey/static/`.  
- Reads/writes JSON in the top‑level `data/` folder (`player_save.json`, `ai_companions.json`, `gadgets.json`).  
- If data files don’t exist, the app will populate sensible defaults on first run.

---

## 📦 Project structure (high‑level)

```
BisonHacks-Minigame/
├─ mini.py                     # Pygame word scramble game (standalone)
├─ vamp.py                     # Single-file Flask web shooter prototype
├─ question_manager.py         # Quiz/word scramble data + helper class
├─ data/                       # Game data (AI companions, gadgets, save)
│  ├─ ai_companions.json
│  ├─ gadgets.json
│  └─ player_save.json
├─ templates/                  # Simple story templates (intro/mission/win/lose)
│  ├─ intro.html
│  ├─ mission1.html
│  ├─ win.html
│  └─ lose.html
├─ hackey/                     # Full Flask app (routes, templates, static)
│  ├─ app.py
│  ├─ templates/
│  └─ static/
├─ hack_pro/                   # Earlier experiments
│  └─ main.py
└─ shuri_vampgame.py/          # Alternate Flask prototype
   ├─ app.py
   └─ templates/static
```

---

## 🧠 Notes & tips

- If Pygame audio files are missing, the mini‑game will still run and print a warning.  
- Flask demos default to `debug=True` — change that before deploying.  
- You can safely delete or ignore experimental folders if you only want to demo one experience.

---

## 📜 License

MIT License (add or update the LICENSE file as needed).
