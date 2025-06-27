from flask import Flask, render_template, redirect, url_for, session, request
import json
import os
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Helper functions
def load_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def get_player_save():
    save_path = 'data/player_save.json'
    save_data = load_json(save_path)
    
    if save_data is None:
        # Initialize with default values
        save_data = {
            "vibranium": 0,
            "unlocked_ai": ["auto_turret"],
            "last_scene": "story_intro",
            "gadgets": [],
            "shield_level": 1,
            "tutorial_completed": False
        }
        save_json(save_path, save_data)
    
    return save_data

def save_player_data(data):
    save_path = 'data/player_save.json'
    save_json(save_path, data)

def load_ai_data():
    return load_json('data/ai_companions.json')

def load_gadgets_data():
    return load_json('data/gadgets.json')

# Routes
@app.route('/')
def home():
    player_data = get_player_save()
    vibranium = player_data.get('vibranium', 0)
    has_save = player_data.get('tutorial_completed', False)
    
    return render_template('home.html', vibranium=vibranium, has_save=has_save)

@app.route('/start')
def start_training():
    # Reset save data for a new game
    player_data = get_player_save()
    if not player_data.get('tutorial_completed', False):
        # Only reset if this is the first time playing
        player_data = {
            "vibranium": 0,
            "unlocked_ai": ["auto_turret"],
            "last_scene": "story_intro",
            "gadgets": [],
            "shield_level": 1,
            "tutorial_completed": False
        }
        save_player_data(player_data)
    
    return redirect(url_for('story_intro'))

@app.route('/continue')
def continue_game():
    player_data = get_player_save()
    
    if not player_data.get('tutorial_completed', False):
        # No save exists, redirect to start
        return redirect(url_for('start_training'))
    
    last_scene = player_data.get('last_scene', 'story_intro')
    return redirect(url_for(last_scene))

@app.route('/vault')
def vault():
    player_data = get_player_save()
    ai_data = load_ai_data()
    gadgets_data = load_gadgets_data()
    
    # Filter unlocked items
    unlocked_ai = [ai for ai in ai_data if ai['id'] in player_data.get('unlocked_ai', [])]
    unlocked_gadgets = [gadget for gadget in gadgets_data if gadget['id'] in player_data.get('gadgets', [])]
    
    return render_template('vault.html', 
                          vibranium=player_data.get('vibranium', 0),
                          unlocked_ai=unlocked_ai,
                          locked_ai=[ai for ai in ai_data if ai['id'] not in player_data.get('unlocked_ai', [])],
                          unlocked_gadgets=unlocked_gadgets,
                          shield_level=player_data.get('shield_level', 1))

@app.route('/settings')
def settings():
    # Load current settings
    settings_data = load_json('data/settings.json')
    if settings_data is None:
        settings_data = {
            "audio_volume": 70,
            "sfx_volume": 80,
            "text_speed": "medium",
            "difficulty": "normal",
            "subtitles": True
        }
        save_json('data/settings.json', settings_data)
    
    return render_template('settings.html', settings=settings_data)

@app.route('/save_settings', methods=['POST'])
def save_settings():
    settings_data = {
        "audio_volume": int(request.form.get('audio_volume', 70)),
        "sfx_volume": int(request.form.get('sfx_volume', 80)),
        "text_speed": request.form.get('text_speed', 'medium'),
        "difficulty": request.form.get('difficulty', 'normal'),
        "subtitles": request.form.get('subtitles') == 'on'
    }
    
    save_json('data/settings.json', settings_data)
    return redirect(url_for('settings'))

@app.route('/story_intro')
def story_intro():
    # Update last scene in player save
    player_data = get_player_save()
    player_data['last_scene'] = 'story_intro'
    save_player_data(player_data)
    
    return render_template('story_intro.html')

@app.route('/ai_selection')
def ai_selection():
    # Update last scene in player save
    player_data = get_player_save()
    player_data['last_scene'] = 'ai_selection'
    save_player_data(player_data)
    
    ai_data = load_ai_data()
    unlocked_ai = [ai for ai in ai_data if ai['id'] in player_data.get('unlocked_ai', [])]
    
    return render_template('ai_selection.html', 
                          available_ai=unlocked_ai,
                          vibranium=player_data.get('vibranium', 0))

@app.route('/select_ai/<ai_id>')
def select_ai(ai_id):
    # Store selected AI in session
    session['selected_ai'] = ai_id
    
    # Randomly choose a game type
    game_types = ['quiz', 'combat', 'matcher']
    selected_game = random.choice(game_types)
    
    if selected_game == 'quiz':
        return redirect(url_for('quiz_game'))
    elif selected_game == 'combat':
        return redirect(url_for('combat_game'))
    else:
        return redirect(url_for('matcher_game'))

@app.route('/quiz')
def quiz_game():
    # Update last scene in player save
    player_data = get_player_save()
    player_data['last_scene'] = 'quiz_game'
    save_player_data(player_data)
    
    # Load questions
    quiz_data = load_json('data/quiz_questions.json')
    selected_questions = random.sample(quiz_data, 5)  # Pick 5 random questions
    
    return render_template('quiz.html', 
                          questions=selected_questions,
                          ai_id=session.get('selected_ai', 'auto_turret'))

@app.route('/combat')
def combat_game():
    # Update last scene in player save
    player_data = get_player_save()
    player_data['last_scene'] = 'combat_game'
    save_player_data(player_data)
    
    return render_template('combat_game.html', 
                          ai_id=session.get('selected_ai', 'auto_turret'),
                          difficulty=load_json('data/settings.json').get('difficulty', 'normal'))

@app.route('/matcher')
def matcher_game():
    # Update last scene in player save
    player_data = get_player_save()
    player_data['last_scene'] = 'matcher_game'
    save_player_data(player_data)
    
    # Load matcher items
    matcher_data = load_json('data/matcher_items.json')
    
    return render_template('matcher.html', 
                          items=matcher_data,
                          ai_id=session.get('selected_ai', 'auto_turret'))

@app.route('/reward/<int:amount>')
def reward(amount):
    # Add vibranium to player's account
    player_data = get_player_save()
    player_data['vibranium'] += amount
    save_player_data(player_data)
    
    return redirect(url_for('home'))

# Initialize the application
if __name__ == '__main__':
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Create default files if they don't exist
    if not os.path.exists('data/player_save.json'):
        default_save = {
            "vibranium": 0,
            "unlocked_ai": ["auto_turret"],
            "last_scene": "story_intro",
            "gadgets": [],
            "shield_level": 1,
            "tutorial_completed": False
        }
        save_json('data/player_save.json', default_save)
    
    if not os.path.exists('data/ai_companions.json'):
        default_ai = [
            {
                "id": "auto_turret",
                "name": "Auto-Turret",
                "description": "Basic defense system with limited intelligence.",
                "abilities": ["Basic targeting", "Low-power energy blasts"],
                "image": "auto_turret.png"
            },
            {
                "id": "shield_drone",
                "name": "Shield Drone",
                "description": "Defensive AI that creates energy barriers.",
                "abilities": ["Energy shield", "Basic threat assessment"],
                "image": "shield_drone.png"
            },
            {
                "id": "panther_scout",
                "name": "Panther Scout",
                "description": "Stealthy reconnaissance AI with enhanced sensors.",
                "abilities": ["Invisibility cloak", "Advanced scanning"],
                "image": "panther_scout.png"
            }
        ]
        save_json('data/ai_companions.json', default_ai)
    
    if not os.path.exists('data/gadgets.json'):
        default_gadgets = [
            {
                "id": "vibranium_claws",
                "name": "Vibranium Claws",
                "description": "Enhanced combat capability with cutting-edge vibranium.",
                "cost": 100,
                "image": "vibranium_claws.png"
            },
            {
                "id": "energy_shield",
                "name": "Energy Shield",
                "description": "Protective barrier that absorbs incoming attacks.",
                "cost": 150,
                "image": "energy_shield.png"
            },
            {
                "id": "sonic_disruptor",
                "name": "Sonic Disruptor",
                "description": "Emits targeted sound waves that can disable tech.",
                "cost": 200,
                "image": "sonic_disruptor.png"
            }
        ]
        save_json('data/gadgets.json', default_gadgets)
    
    app.run(debug=True)