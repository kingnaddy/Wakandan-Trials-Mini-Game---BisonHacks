from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Game Configuration
GAME_CONFIG = {
    "title": "Wakanda: Rise of Shuri",
    "screen_width": 800,
    "screen_height": 600,
    "fps": 60,
}


@app.route('/')
def index():
    return render_template('index.html', config=GAME_CONFIG)


@app.route('/api/generate_level')
def generate_level():
    level = {
        "arena": random.choice(["Royal Palace", "Vibranium Lab", "Border Tribe"]),
        "enemies": [{"type": random.choice(["Drone", "Mercenary", "Cyborg"]),
                     "x": random.randint(50, 750),
                     "y": random.randint(-300, -50),
                     "speed": random.uniform(1.5, 3)} for _ in range(15)],
        "obstacles": [{"x": random.randint(50, 750),
                       "y": random.randint(50, 550)} for _ in range(10)]
    }
    return jsonify(level)


if __name__ == "__main__":
    app.run(debug=True)
