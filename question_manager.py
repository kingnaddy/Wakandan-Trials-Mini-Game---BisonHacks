import json
import random

def generate_questions_json():
    """
    Generates a JSON file with Black Panther lore quiz questions and
    word scramble challenges
    """
    
    # Quiz Questions: Black Panther and Wakanda Lore
    quiz_questions = [
        {
            "question": "What is vibranium's key property?",
            "options": [
                "Conducts magic",
                "Absorbs sound and vibration",
                "Repels gravity",
                "Powers satellites"
            ],
            "correct_answer": 1,
            "difficulty": "easy",
            "category": "vibranium"
        },
        {
            "question": "Who was the first Black Panther?",
            "options": [
                "T'Chaka",
                "T'Challa",
                "Bashenga",
                "N'Jadaka"
            ],
            "correct_answer": 2,
            "difficulty": "medium",
            "category": "history"
        },
        {
            "question": "What is the name of the Wakandan ancestral plane?",
            "options": [
                "Djalia",
                "Necropolis",
                "Birnin Zana",
                "Niganda"
            ],
            "correct_answer": 0,
            "difficulty": "hard",
            "category": "spiritual"
        },
        {
            "question": "Which substance gives the Black Panther superhuman abilities?",
            "options": [
                "Vibranium radiation",
                "Heart-Shaped Herb",
                "Kimoyo beads",
                "Jabari wood"
            ],
            "correct_answer": 1,
            "difficulty": "easy",
            "category": "powers"
        },
        {
            "question": "What is the name of Wakanda's capital city?",
            "options": [
                "Golden City",
                "Necropolis",
                "Birnin Zana",
                "N'Jadaka Village"
            ],
            "correct_answer": 2,
            "difficulty": "medium",
            "category": "geography"
        },
        {
            "question": "What does 'Wakanda Forever' mean in Xhosa?",
            "options": [
                "Wakanda Phambili",
                "Wakanda Ngonaphakade",
                "Wakanda Yonke",
                "Wakanda Umuntu"
            ],
            "correct_answer": 1,
            "difficulty": "hard",
            "category": "language"
        },
        {
            "question": "Which Wakandan tribe uses the rhinoceros in their iconography?",
            "options": [
                "Mining Tribe",
                "Border Tribe",
                "River Tribe",
                "Jabari Tribe"
            ],
            "correct_answer": 1,
            "difficulty": "medium",
            "category": "tribes"
        },
        {
            "question": "What is the name of Shuri's AI assistant?",
            "options": [
                "FRIDAY",
                "Griot",
                "JARVIS",
                "SHURI"
            ],
            "correct_answer": 1,
            "difficulty": "easy",
            "category": "technology"
        },
        {
            "question": "What metal was used to create Captain America's shield?",
            "options": [
                "Pure vibranium",
                "Vibranium-steel alloy",
                "Adamantium",
                "Uru"
            ],
            "correct_answer": 1,
            "difficulty": "medium",
            "category": "vibranium"
        },
        {
            "question": "What animal do the Jabari Tribe worship?",
            "options": [
                "Panther",
                "Gorilla",
                "Rhino",
                "Crocodile"
            ],
            "correct_answer": 1,
            "difficulty": "easy",
            "category": "tribes"
        },
        {
            "question": "What is the name of Wakanda's all-female special forces?",
            "options": [
                "Hatut Zeraze",
                "Dora Milaje",
                "War Dogs",
                "Taifa Ngao"
            ],
            "correct_answer": 1,
            "difficulty": "easy",
            "category": "military"
        },
        {
            "question": "What is the traditional combat ritual to become Black Panther?",
            "options": [
                "Challenge Day",
                "Warrior Falls",
                "Panther Trials",
                "Wakanda Tournament"
            ],
            "correct_answer": 0,
            "difficulty": "medium",
            "category": "traditions"
        },
        {
            "question": "Who designed the advanced Kimoyo beads technology?",
            "options": [
                "T'Challa",
                "T'Chaka",
                "Shuri",
                "N'Baza"
            ],
            "correct_answer": 2,
            "difficulty": "medium",
            "category": "technology"
        },
        {
            "question": "Where is Wakanda located?",
            "options": [
                "West Africa",
                "East Africa",
                "Central Africa",
                "Southern Africa"
            ],
            "correct_answer": 1,
            "difficulty": "easy",
            "category": "geography"
        },
        {
            "question": "Which Wakandan God is associated with death and rebirth?",
            "options": [
                "Bast",
                "Sekhmet",
                "Hanuman",
                "Kokou"
            ],
            "correct_answer": 0,
            "difficulty": "hard",
            "category": "spiritual"
        }
    ]
    
    # Word Scramble: Black Panther Related Terms
    word_scramble = [
        {
            "scrambled": "GREATHURB",
            "correct": "HEART HERB",
            "hint": "Grants the Black Panther powers",
            "difficulty": "easy"
        },
        {
            "scrambled": "NAAKAWD",
            "correct": "WAKANDA",
            "hint": "Hidden African nation",
            "difficulty": "easy"
        },
        {
            "scrambled": "MIRUVABIN",
            "correct": "VIBRANIUM",
            "hint": "Precious metal from meteorite",
            "difficulty": "medium"
        },
        {
            "scrambled": "LALCATH",
            "correct": "TCHALLA",
            "hint": "King and protector",
            "difficulty": "easy"
        },
        {
            "scrambled": "SHIRUTAN",
            "correct": "SHURI",
            "hint": "Tech genius princess",
            "difficulty": "easy"
        },
        {
            "scrambled": "ROJADAMI",
            "correct": "DORA MILAJE",
            "hint": "Elite female warriors",
            "difficulty": "hard"
        },
        {
            "scrambled": "MLAKOLAB",
            "correct": "KILLMONGER",
            "hint": "Challenger to the throne",
            "difficulty": "hard"
        },
        {
            "scrambled": "OKOMYE",
            "correct": "OKOYE",
            "hint": "General of the royal guard",
            "difficulty": "medium"
        },
        {
            "scrambled": "KINOYOAM",
            "correct": "KIMOYO",
            "hint": "Advanced bead technology",
            "difficulty": "medium"
        },
        {
            "scrambled": "ASTB",
            "correct": "BAST",
            "hint": "Panther deity",
            "difficulty": "easy"
        },
        {
            "scrambled": "BARIJA",
            "correct": "JABARI",
            "hint": "Mountain tribe",
            "difficulty": "medium"
        },
        {
            "scrambled": "KAUCH",
            "correct": "TCHAKA",
            "hint": "Former king",
            "difficulty": "medium"
        },
        {
            "scrambled": "TORIG",
            "correct": "GRIOT",
            "hint": "AI assistant",
            "difficulty": "easy"
        },
        {
            "scrambled": "LABCKHERTNAP",
            "correct": "BLACK PANTHER",
            "hint": "Protector of Wakanda",
            "difficulty": "medium"
        },
        {
            "scrambled": "NIRIBNZANA",
            "correct": "BIRNIN ZANA",
            "hint": "Golden City",
            "difficulty": "hard"
        }
    ]
    
    # Combined data structure
    data = {
        "quiz_questions": quiz_questions,
        "word_scramble": word_scramble,
        "meta": {
            "version": "1.0",
            "generated": "2025-03-23",
            "description": "Black Panther lore for Wakanda: Shuri's Gauntlet game"
        }
    }
    
    # Generate more scrambled words dynamically
    more_words = [
        {"word": "MBAKU", "hint": "Jabari tribe leader"},
        {"word": "NECROPOLIS", "hint": "City of the dead"},
        {"word": "ANCESTRAL PLANE", "hint": "Spiritual realm"},
        {"word": "TALON FIGHTER", "hint": "Wakandan aircraft"},
        {"word": "HATUT ZERAZE", "hint": "War Dogs"},
        {"word": "WAKANDA FOREVER", "hint": "Battle cry"},
        {"word": "SNOW LEOPARD", "hint": "White panther goddess"},
        {"word": "BASHENGA", "hint": "First Black Panther"},
        {"word": "MINING TRIBE", "hint": "Vibranium extractors"},
        {"word": "MERCHANT TRIBE", "hint": "Trade specialists"}
    ]
    
    for item in more_words:
        word = item["word"]
        # Create a simple scramble by shuffling letters
        letters = list(word.replace(" ", ""))
        random.shuffle(letters)
        scrambled = "".join(letters)
        
        data["word_scramble"].append({
            "scrambled": scrambled,
            "correct": word,
            "hint": item["hint"],
            "difficulty": "medium" if len(word) > 7 else "easy"
        })
    
    # Write to file
    with open("data/questions.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    
    print(f"Generated questions.json with {len(quiz_questions)} quiz questions and {len(data['word_scramble'])} word scrambles")
    return data

def generate_question_loader():
    """Creates a utility module to load and manage questions"""
    code = """
import json
import random

class QuestionManager:
    def __init__(self, json_file="data/questions.json"):
        self.json_file = json_file
        self.data = self.load_json()
        self.quiz_questions = self.data.get("quiz_questions", [])
        self.word_scrambles = self.data.get("word_scramble", [])
        
        # Track used questions to avoid repetition
        self.used_quiz_ids = set()
        self.used_scramble_ids = set()
    
    def load_json(self):
        try:
            with open(self.json_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Error loading {self.json_file}. Using empty data.")
            return {"quiz_questions": [], "word_scramble": []}
    
    def get_random_quiz(self, difficulty=None, category=None, avoid_repeats=True):
        ""Get a random quiz question, optionally filtered by difficulty and category""
        filtered_questions = self.quiz_questions
        
        # Apply filters
        if difficulty:
            filtered_questions = [q for q in filtered_questions if q.get("difficulty") == difficulty]
        if category:
            filtered_questions = [q for q in filtered_questions if q.get("category") == category]
        
        # Filter out used questions if avoiding repeats and if we have enough questions left
        if avoid_repeats and len(self.used_quiz_ids) < len(filtered_questions) * 0.8:
            available_questions = [q for i, q in enumerate(filtered_questions) 
                                if i not in self.used_quiz_ids]
            if available_questions:
                filtered_questions = available_questions
            else:
                # Reset used questions if we've used almost all of them
                self.used_quiz_ids.clear()
        
        if not filtered_questions:
            return None
        
        # Select random question
        question = random.choice(filtered_questions)
        question_id = filtered_questions.index(question)
        self.used_quiz_ids.add(question_id)
        
        return question
    
    def get_random_scramble(self, difficulty=None, avoid_repeats=True):
        ""Get a random word scramble, optionally filtered by difficulty""
        filtered_scrambles = self.word_scrambles
        
        # Apply difficulty filter
        if difficulty:
            filtered_scrambles = [s for s in filtered_scrambles if s.get("difficulty") == difficulty]
        
        # Filter out used scrambles if avoiding repeats and if we have enough left
        if avoid_repeats and len(self.used_scramble_ids) < len(filtered_scrambles) * 0.8:
            available_scrambles = [s for i, s in enumerate(filtered_scrambles) 
                                  if i not in self.used_scramble_ids]
            if available_scrambles:
                filtered_scrambles = available_scrambles
            else:
                # Reset used scrambles if we've used almost all of them
                self.used_scramble_ids.clear()
        
        if not filtered_scrambles:
            return None
        
        # Select random scramble
        scramble = random.choice(filtered_scrambles)
        scramble_id = filtered_scrambles.index(scramble)
        self.used_scramble_ids.add(scramble_id)
        
        return scramble
    
    def get_questions_batch(self, count=5, difficulty=None, category=None):
        ""Get a batch of unique quiz questions""
        result = []
        for _ in range(count):
            question = self.get_random_quiz(difficulty, category)
            if question and question not in result:
                result.append(question)
        return result
    
    def get_scrambles_batch(self, count=5, difficulty=None):
        ""Get a batch of unique word scrambles""
        result = []
        for _ in range(count):
            scramble = self.get_random_scramble(difficulty)
            if scramble and scramble not in result:
                result.append(scramble)
        return result

# Example usage
if __name__ == "__main__":
    manager = QuestionManager()
    
    # Get a random quiz question
    quiz = manager.get_random_quiz()
    if quiz:
        print(f"QUIZ: {quiz['question']}")
        for i, option in enumerate(quiz['options']):
            print(f"{i}. {option}")
        print(f"Correct: {quiz['options'][quiz['correct_answer']]}")
    
    # Get a random word scramble
    scramble = manager.get_random_scramble()
    if scramble:
        print(f"\\nSCRAMBLE: {scramble['scrambled']}")
        print(f"Hint: {scramble['hint']}")
        print(f"Answer: {scramble['correct']}")
"""
    
    if not os.path.exists("data"):
        os.makedirs("data")
    os.makedirs("data", exist_ok=True)
    
    # Write to file
    with open("data/question_manager.py", "w", encoding="utf-8") as f:
        f.write(code)
    
    print("Generated question_manager.py")

if __name__ == "__main__":
    # Make sure the directory exists
    import os
    os.makedirs("data", exist_ok=True)
    
    # Generate files
    data = generate_questions_json()
    generate_question_loader()
    
    print("Generation complete!")
    
    # Display a sample of the generated data
    print("\nSample Quiz Questions:")
    for i, question in enumerate(data["quiz_questions"][:3]):
        print(f"{i+1}. {question['question']}")
        print(f"   Answer: {question['options'][question['correct_answer']]}")
    
    print("\nSample Word Scrambles:")
    for i, scramble in enumerate(data["word_scramble"][:3]):
        print(f"{i+1}. {scramble['scrambled']} -> {scramble['correct']} (Hint: {scramble['hint']})")