import pygame
import time
import json
import random
import os
from pygame import mixer

class StoryIntro:
    def __init__(self, screen, skip_intro=False):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.skip_intro = skip_intro
        
        # Initialize colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.PURPLE = (128, 0, 128)
        self.VIBRANIUM_BLUE = (0, 191, 255)
        self.ALERT_RED = (255, 0, 0)
        
        # Load fonts
        pygame.font.init()
        try:
            self.title_font = pygame.font.Font("assets/fonts/wakanda_forever.ttf", 48)
            self.text_font = pygame.font.Font("assets/fonts/wakanda_forever.ttf", 24)
        except FileNotFoundError:
            # Fallback fonts if custom fonts not available
            self.title_font = pygame.font.SysFont("arial", 48)
            self.text_font = pygame.font.SysFont("arial", 24)
        
        # Initialize sounds
        mixer.init()
        self.load_sounds()
        
        # Intro text dialogue
        self.intro_text = [
            "Initializing Neural Defense Interface...",
            "Good day, Shuri. The lab is operational.",
            "Vibranium levels are stable.",
            "Systems are functioning at optimal capacity.",
            "Wait... anomaly detected...",
            "WARNING: Intrusion detected in Sector 4.",
            "Unauthorized scans targeting vibranium vault.",
            "Security protocols activated.",
            "You have 3 minutes to protect Wakanda's vibranium vault.",
            "Begin training. Choose your companion."
        ]
        
        # Text animation variables
        self.current_text_index = 0
        self.display_text = ""
        self.text_animation_speed = 0.03  # seconds per character
        self.last_char_time = 0
        self.text_animation_complete = False
        
        # Alert system variables
        self.alert_active = False
        self.alert_start_time = 0
        self.alert_duration = 0.5  # seconds
        self.alert_frequency = 1.0  # seconds (full on/off cycle)
        
    def load_sounds(self):
        """Load sound effects"""
        self.sounds = {}
        try:
            self.sounds["typing"] = mixer.Sound("assets/sounds/typing.wav")
            self.sounds["alert"] = mixer.Sound("assets/sounds/alert.wav")
            self.sounds["startup"] = mixer.Sound("assets/sounds/startup.wav")
        except FileNotFoundError:
            print("Warning: Some sound files could not be loaded")
    
    def play_sound(self, sound_name):
        """Play a sound if it exists"""
        if sound_name in self.sounds:
            self.sounds[sound_name].play()
    
    def trigger_alert(self):
        """Activate the alert system"""
        self.alert_active = True
        self.alert_start_time = time.time()
        self.play_sound("alert")
    
    def update_text_animation(self):
        """Update the text animation frame"""
        if self.current_text_index >= len(self.intro_text):
            self.text_animation_complete = True
            return
        
        current_line = self.intro_text[self.current_text_index]
        current_time = time.time()
        
        # Calculate how many characters should be displayed
        if self.last_char_time == 0:
            self.last_char_time = current_time
            self.play_sound("typing")
        
        chars_to_display = int((current_time - self.last_char_time) / self.text_animation_speed)
        
        if chars_to_display >= len(current_line):
            # Move to next line
            self.display_text = current_line
            self.current_text_index += 1
            self.last_char_time = 0
            
            # Trigger alert when warning text appears
            if "WARNING" in current_line:
                self.trigger_alert()
        else:
            self.display_text = current_line[:chars_to_display]
    
    def draw(self):
        """Draw the intro sequence"""
        # Fill background
        self.screen.fill(self.BLACK)
        
        # Handle alert flashing effect
        if self.alert_active:
            current_time = time.time()
            time_in_cycle = (current_time - self.alert_start_time) % self.alert_frequency
            if time_in_cycle < self.alert_duration:
                # Draw red overlay during alert
                alert_surface = pygame.Surface((self.screen_width, self.screen_height))
                alert_surface.fill(self.ALERT_RED)
                alert_surface.set_alpha(30)  # Set transparency
                self.screen.blit(alert_surface, (0, 0))
        
        # Draw Wakanda title
        if self.current_text_index > 0:
            title_text = self.title_font.render("WAKANDA: RISE OF SHURI", True, self.VIBRANIUM_BLUE)
            title_rect = title_text.get_rect(center=(self.screen_width // 2, 80))
            self.screen.blit(title_text, title_rect)
        
        # Draw current text
        if not self.text_animation_complete:
            # Determine text color based on content
            text_color = self.WHITE
            if "WARNING" in self.display_text:
                text_color = self.ALERT_RED
            elif "vibranium" in self.display_text:
                text_color = self.VIBRANIUM_BLUE
            
            text_surface = self.text_font.render(self.display_text, True, text_color)
            text_rect = text_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(text_surface, text_rect)
    
    def update(self):
        """Update intro state"""
        if not self.text_animation_complete:
            self.update_text_animation()
        
        # Skip intro functionality
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_RETURN] or self.skip_intro:
            self.text_animation_complete = True
            return True  # Signal to move to next screen
        
        return self.text_animation_complete
    
    def run(self):
        """Run the intro sequence"""
        self.play_sound("startup")
        
        running = True
        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
            
            # Update and draw
            completed = self.update()
            self.draw()
            pygame.display.flip()
            
            if completed:
                # Add small delay before moving on
                time.sleep(1)
                running = False
            
            clock.tick(60)
        
        return True

def main():
    """Test function to run intro standalone"""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Wakanda: Shuri's Gauntlet")
    
    intro = StoryIntro(screen)
    intro.run()
    
    pygame.quit()

if __name__ == "__main__":
    main()