import pygame
import sys
import os
import json
import random
import time

# Add the parent directory to the path so we can import from data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from question_manager import QuestionManager

class WordScrambleGame:
    def __init__(self, screen, difficulty=None, time_limit=60):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.difficulty = difficulty
        self.time_limit = time_limit
        self.time_remaining = time_limit
        self.game_active = True
        self.score = 0
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.PURPLE = (128, 0, 128)
        self.VIBRANIUM_BLUE = (0, 191, 255)
        self.ALERT_RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        
        # Load fonts
        pygame.font.init()
        try:
            self.title_font = pygame.font.Font("assets/fonts/wakanda_forever.ttf", 36)
            self.text_font = pygame.font.Font("assets/fonts/wakanda_forever.ttf", 24)
            self.input_font = pygame.font.Font("assets/fonts/wakanda_forever.ttf", 28)
        except FileNotFoundError:
            # Fallback fonts
            self.title_font = pygame.font.SysFont("arial", 36)
            self.text_font = pygame.font.SysFont("arial", 24)
            self.input_font = pygame.font.SysFont("arial", 28)
        
        # Load sounds
        pygame.mixer.init()
        self.load_sounds()
        
        # Initialize question manager
        self.question_manager = QuestionManager()
        
        # Current scramble and user input
        self.current_scramble = None
        self.user_input = ""
        self.feedback_message = ""
        self.feedback_color = self.WHITE
        self.feedback_time = 0
        
        # Get first scramble
        self.get_new_scramble()
        
        # Game timing
        self.start_time = time.time()
        self.last_time_check = self.start_time
    
    def load_sounds(self):
        """Load sound effects"""
        self.sounds = {}
        try:
            self.sounds["correct"] = pygame.mixer.Sound("assets/sounds/correct.wav")
            self.sounds["wrong"] = pygame.mixer.Sound("assets/sounds/wrong.wav")
            self.sounds["typing"] = pygame.mixer.Sound("assets/sounds/typing.wav")
            self.sounds["countdown"] = pygame.mixer.Sound("assets/sounds/countdown.wav")
            self.sounds["win"] = pygame.mixer.Sound("assets/sounds/win.wav")
            self.sounds["lose"] = pygame.mixer.Sound("assets/sounds/lose.wav")
        except FileNotFoundError:
            print("Warning: Some sound files could not be loaded")
    
    def play_sound(self, sound_name):
        """Play a sound if it exists"""
        if sound_name in self.sounds:
            self.sounds[sound_name].play()
    
    def get_new_scramble(self):
        """Get a new word scramble from the question manager"""
        self.current_scramble = self.question_manager.get_random_scramble(self.difficulty)
        if not self.current_scramble:
            # Fallback if no matching scrambles found
            self.current_scramble = {
                "scrambled": "NAAKAWD",
                "correct": "WAKANDA",
                "hint": "Hidden African nation",
                "difficulty": "easy"
            }
        self.user_input = ""
    
    def handle_input(self, event):
        """Handle keyboard input"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.check_answer()
            elif event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
                self.play_sound("typing")
            elif event.unicode.isalpha() or event.unicode.isspace():
                self.user_input += event.unicode.upper()
                self.play_sound("typing")
    
    def check_answer(self):
        """Check if the user's answer is correct"""
        if not self.user_input:
            return
        
        # Compare with correct answer (case insensitive)
        correct_answer = self.current_scramble["correct"].upper()
        user_answer = self.user_input.upper()
        
        if user_answer == correct_answer:
            self.score += 100
            self.feedback_message = "Correct!"
            self.feedback_color = self.GREEN
            self.play_sound("correct")
            self.get_new_scramble()
        else:
            self.feedback_message = "Try again!"
            self.feedback_color = self.ALERT_RED
            self.play_sound("wrong")
        
        self.feedback_time = time.time()
    
    def update(self):
        """Update game state"""
        current_time = time.time()
        
        # Update time remaining
        self.time_remaining = max(0, self.time_limit - (current_time - self.start_time))
        
        # Clear feedback message after 2 seconds
        if self.feedback_time > 0 and current_time - self.feedback_time > 2:
            self.feedback_message = ""
            self.feedback_time = 0
        
        # Play countdown sound when time is running low
        if self.time_remaining <= 10 and current_time - self.last_time_check >= 1:
            self.last_time_check = current_time
            self.play_sound("countdown")
        
        # Check if game is over
        if self.time_remaining <= 0 and self.game_active:
            self.game_active = False
            self.play_sound("lose")
    
    def draw(self):
        """Draw the game screen"""
        # Fill background
        self.screen.fill(self.BLACK)
        
        # Draw title
        title_text = self.title_font.render("CODE DECRYPTION", True, self.VIBRANIUM_BLUE)
        title_rect = title_text.get_rect(center=(self.width // 2, 60))
        self.screen.blit(title_text, title_rect)
        
        # Draw vibranium-style frame
        frame_rect = pygame.Rect(self.width * 0.1, self.height * 0.2, 
                                self.width * 0.8, self.height * 0.6)
        pygame.draw.rect(self.screen, self.VIBRANIUM_BLUE, frame_rect, 3, border_radius=15)
        
        # Draw timer
        timer_text = self.text_font.render(f"Time: {int(self.time_remaining)}s", True, 
                                         self.WHITE if self.time_remaining > 10 else self.ALERT_RED)
        self.screen.blit(timer_text, (50, 30))
        
        # Draw score
        score_text = self.text_font.render(f"Score: {self.score}", True, self.WHITE)
        score_rect = score_text.get_rect(right=self.width - 50, top=30)
        self.screen.blit(score_text, score_rect)
        
        if self.game_active:
            # Draw scrambled word
            scrambled_text = self.title_font.render(self.current_scramble["scrambled"], True, self.WHITE)
            scrambled_rect = scrambled_text.get_rect(center=(self.width // 2, self.height * 0.3))
            self.screen.blit(scrambled_text, scrambled_rect)
            
            # Draw hint
            hint_text = self.text_font.render(f"Hint: {self.current_scramble['hint']}", True, self.PURPLE)
            hint_rect = hint_text.get_rect(center=(self.width // 2, self.height * 0.4))
            self.screen.blit(hint_text, hint_rect)
            
            # Draw input field
            input_bg = pygame.Rect(self.width * 0.2, self.height * 0.5, 
                                  self.width * 0.6, 50)
            pygame.draw.rect(self.screen, self.WHITE, input_bg, 0, border_radius=10)
            
            if self.user_input:
                input_text = self.input_font.render(self.user_input, True, self.BLACK)
                input_rect = input_text.get_rect(center=(self.width // 2, self.height * 0.5 + 25))
                self.screen.blit(input_text, input_rect)
            
            # Draw instructions
            instruct_text = self.text_font.render("Type the correct answer and press Enter", True, self.WHITE)
            instruct_rect = instruct_text.get_rect(center=(self.width // 2, self.height * 0.65))
            self.screen.blit(instruct_text, instruct_rect)
            
            # Draw feedback message
            if self.feedback_message:
                feedback_text = self.text_font.render(self.feedback_message, True, self.feedback_color)
                feedback_rect = feedback_text.get_rect(center=(self.width // 2, self.height * 0.75))
                self.screen.blit(feedback_text, feedback_rect)
        else:
            # Game over screen
            game_over_text = self.title_font.render("DECRYPTION COMPLETE", True, self.VIBRANIUM_BLUE)
            game_over_rect = game_over_text.get_rect(center=(self.width // 2, self.height * 0.4))
            self.screen.blit(game_over_text, game_over_rect)
            
            final_score_text = self.text_font.render(f"Final Score: {self.score}", True, self.WHITE)
            final_score_rect = final_score_text.get_rect(center=(self.width // 2, self.height * 0.5))
            self.screen.blit(final_score_text, final_score_rect)
            
            continue_text = self.text_font.render("Press SPACE to continue", True, self.WHITE)
            continue_rect = continue_text.get_rect(center=(self.width // 2, self.height * 0.6))
            self.screen.blit(continue_text, continue_rect)
    
    def run(self):
        """Run the word scramble game"""
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return {"status": "quit", "score": self.score}
                
                if self.game_active:
                    self.handle_input(event)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return {"status": "complete", "score": self.score}
            
            # Update game state
            self.update()
            
            # Draw everything
            self.draw()
            
            # Update display
            pygame.display.flip()
            clock.tick(60)
        
        return {"status": "complete", "score": self.score}

def main():
    """Test function to run the word scramble game standalone"""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Wakanda: Word Scramble")
    
    game = WordScrambleGame(screen, time_limit=60)
    result = game.run()
    
    print(f"Game ended with status: {result['status']}, score: {result['score']}")
    pygame.quit()

if __name__ == "__main__":
    main()