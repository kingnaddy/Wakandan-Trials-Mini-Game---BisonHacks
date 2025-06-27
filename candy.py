import pygame
import random
import sys
import time




# Initialize Pygame
pygame.init()




# Constants
GRID_SIZE = 6
CELL_SIZE = 80
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
WINDOW_WIDTH = WINDOW_SIZE
WINDOW_HEIGHT = WINDOW_SIZE + 60  # Extra space for timer and score
# Replace shapes with crystal types
CRYSTALS = ['heart', 'round', 'triangle', 'raw', 'royal', 'star']
# Vibranium-inspired color palette
COLORS = {
    'heart': (147, 0, 211),  # Purple
    'round': (180, 180, 255),  # Light blue-white
    'triangle': (255, 50, 150),  # Magenta
    'raw': (0, 255, 180),  # Cyan-green
    'royal': (0, 191, 255),  # Deep Sky Blue
    'star': (255, 0, 127)  # Pink
}




# Setup display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wakanda Crystal Match")




# Setup font
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 60)




# Background color - dark purple/blue for Wakandan tech feel
BG_COLOR = (25, 20, 40)
GRID_COLOR = (40, 35, 60)
HIGHLIGHT_COLOR = (255, 215, 0)  # Gold highlight for selection




class Crystal:
    def __init__(self, crystal_type):
        self.type = crystal_type
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0
        self.scale = 1.0
        self.matched = False
        self.disappearing = False
        self.rotation = random.randint(0, 30)  # Random slight rotation for variety
       
    def move_towards_target(self):
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        if abs(dx) < 0.5 and abs(dy) < 0.5:
            self.x, self.y = self.target_x, self.target_y
            return True
        self.x += dx * 0.2
        self.y += dy * 0.2
        return False
       
    def draw(self, grid_x, grid_y):
        if self.matched:
            return  # Don't draw matched crystals
           
        base_x = grid_x * CELL_SIZE + CELL_SIZE // 2
        base_y = grid_y * CELL_SIZE + CELL_SIZE // 2
        center = (int(base_x + self.x), int(base_y + self.y))
        color = COLORS[self.type]
       
        # Add a glow effect
        glow_radius = int(30 * self.scale)
        glow_surface = pygame.Surface((glow_radius*2, glow_radius*2), pygame.SRCALPHA)
       
        # Create gradient glow
        for r in range(glow_radius, 0, -1):
            alpha = 100 * (r / glow_radius) if not self.disappearing else 100 * (r / glow_radius) * self.scale
            pygame.draw.circle(
                glow_surface,
                (*color, int(alpha)),
                (glow_radius, glow_radius),
                r
            )
       
        # Position and draw the glow
        screen.blit(
            glow_surface,
            (center[0] - glow_radius, center[1] - glow_radius)
        )
       
        # Draw the crystal shape
        if self.type == 'heart':
            # Heart-shaped vibranium crystal
            size = int(22 * self.scale)
            # Draw heart shape using bezier curves approximation
            points = []
            # Top of heart
            points.append((center[0], center[1] - size//2))
            # Right curve
            points.append((center[0] + size//2, center[1] - size//4))
            points.append((center[0] + size//2, center[1] + size//4))
            # Bottom point
            points.append((center[0], center[1] + size//2))
            # Left curve
            points.append((center[0] - size//2, center[1] + size//4))
            points.append((center[0] - size//2, center[1] - size//4))
            # Close the shape
            points.append((center[0], center[1] - size//2))
           
            pygame.draw.polygon(screen, color, points)
            # Add facet lines
            pygame.draw.line(screen, (255, 255, 255, 100),
                            (center[0], center[1] - size//2),
                            (center[0], center[1] + size//2), 1)
           
        elif self.type == 'round':
            # Round vibranium crystal with facets
            size = int(20 * self.scale)
            pygame.draw.circle(screen, color, center, size)
            # Add facet lines
            for angle in range(0, 360, 45):
                rad = angle * 3.14159 / 180
                end_x = center[0] + int(size * 0.8 * pygame.math.Vector2(1, 0).rotate(angle)[0])
                end_y = center[1] + int(size * 0.8 * pygame.math.Vector2(1, 0).rotate(angle)[1])
                pygame.draw.line(screen, (255, 255, 255, 80), center, (end_x, end_y), 1)
           
        elif self.type == 'triangle':
            # Triangular vibranium crystal
            size = int(24 * self.scale)
            points = [
                (center[0], center[1] - size),
                (center[0] + size//1.2, center[1] + size//2),
                (center[0] - size//1.2, center[1] + size//2)
            ]
            pygame.draw.polygon(screen, color, points)
            # Add facet lines
            pygame.draw.line(screen, (255, 255, 255, 100),
                            (center[0], center[1] - size),
                            (center[0], center[1] + size//3), 1)
           
        elif self.type == 'raw':
            # Raw uncut vibranium crystal
            size = int(22 * self.scale)
            # Create irregular polygon for raw crystal look
            points = []
            for i in range(6):
                angle = 2 * 3.14159 * i / 6 + self.rotation / 20
                dist = size * (0.8 + random.random() * 0.4)
                points.append((
                    center[0] + int(dist * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[0]),
                    center[1] + int(dist * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[1])
                ))
            pygame.draw.polygon(screen, color, points)
           
        elif self.type == 'royal':
            # Royal vibranium - hexagonal crystal with intricate cut
            size = int(20 * self.scale)
            points = []
            for i in range(6):
                angle = 2 * 3.14159 * i / 6 + self.rotation / 30
                points.append((
                    center[0] + int(size * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[0]),
                    center[1] + int(size * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[1])
                ))
            pygame.draw.polygon(screen, color, points)
           
            # Inner facets
            inner_points = []
            for i in range(6):
                angle = 2 * 3.14159 * i / 6 + self.rotation / 30 + 3.14159/6
                inner_points.append((
                    center[0] + int(size * 0.5 * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[0]),
                    center[1] + int(size * 0.5 * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[1])
                ))
            pygame.draw.polygon(screen, (*color, 180), inner_points)
           
        elif self.type == 'star':
            # Star-shaped vibranium crystal
            size = int(22 * self.scale)
            points = []
            for i in range(5):
                # Outer point
                angle = 2 * 3.14159 * i / 5 - 3.14159 / 2 + self.rotation / 30
                points.append((
                    center[0] + int(size * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[0]),
                    center[1] + int(size * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[1])
                ))
                # Inner point
                angle = 2 * 3.14159 * (i + 0.5) / 5 - 3.14159 / 2 + self.rotation / 30
                points.append((
                    center[0] + int(size * 0.4 * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[0]),
                    center[1] + int(size * 0.4 * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[1])
                ))
            pygame.draw.polygon(screen, color, points)




class Game:
    def __init__(self):
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.fill_grid()
        self.selected = None
        self.animating = False
        self.disappearing = set()
        self.check_initial_matches()
        self.match_count = 0
        self.time_left = 20.0  # Starting with 45 seconds
        self.start_time = time.time()
        self.game_over = False
        self.mission_complete = False
       
    def fill_grid(self):
        # Initialize the grid with crystals, properly positioned
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                self.grid[y][x] = Crystal(random.choice(CRYSTALS))
                self.grid[y][x].x = 0
                self.grid[y][x].y = 0
                self.grid[y][x].target_x = 0
                self.grid[y][x].target_y = 0
       
    def check_initial_matches(self):
        # Make sure we don't start with any matches
        max_retries = 10
        while self.check_matches(False) and max_retries > 0:
            for y in range(GRID_SIZE):
                for x in range(GRID_SIZE):
                    if (x, y) in self.disappearing:
                        self.grid[y][x] = Crystal(random.choice(CRYSTALS))
            self.disappearing.clear()
            max_retries -= 1
           
    def draw(self):
        # Fill background with Wakandan tech pattern
        screen.fill(BG_COLOR)
       
        # Draw subtle grid pattern
        for y in range(GRID_SIZE + 1):
            pygame.draw.line(screen, GRID_COLOR,
                           (0, y * CELL_SIZE),
                           (WINDOW_WIDTH, y * CELL_SIZE), 1)
        for x in range(GRID_SIZE + 1):
            pygame.draw.line(screen, GRID_COLOR,
                           (x * CELL_SIZE, 0),
                           (x * CELL_SIZE, WINDOW_SIZE), 1)
       
        # Draw grid cells and crystals
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                # Draw cell background with subtle pattern
                cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRID_COLOR, cell_rect)
               
                # Draw diagonal line pattern in cells
                if (x + y) % 2 == 0:
                    pygame.draw.line(screen, (50, 45, 70),
                                   (x * CELL_SIZE, y * CELL_SIZE),
                                   ((x+1) * CELL_SIZE, (y+1) * CELL_SIZE), 1)
               
                # Draw selection highlight with Wakandan-style pattern
                if self.selected == (x, y):
                    # Golden highlight border
                    pygame.draw.rect(screen, HIGHLIGHT_COLOR,
                                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
                    # Add decorative corner marks
                    corner_size = 10
                    # Top-left
                    pygame.draw.line(screen, HIGHLIGHT_COLOR,
                                   (x * CELL_SIZE, y * CELL_SIZE + corner_size),
                                   (x * CELL_SIZE + corner_size, y * CELL_SIZE), 2)
                    # Top-right
                    pygame.draw.line(screen, HIGHLIGHT_COLOR,
                                   ((x+1) * CELL_SIZE, y * CELL_SIZE + corner_size),
                                   ((x+1) * CELL_SIZE - corner_size, y * CELL_SIZE), 2)
                    # Bottom-left
                    pygame.draw.line(screen, HIGHLIGHT_COLOR,
                                   (x * CELL_SIZE, (y+1) * CELL_SIZE - corner_size),
                                   (x * CELL_SIZE + corner_size, (y+1) * CELL_SIZE), 2)
                    # Bottom-right
                    pygame.draw.line(screen, HIGHLIGHT_COLOR,
                                   ((x+1) * CELL_SIZE, (y+1) * CELL_SIZE - corner_size),
                                   ((x+1) * CELL_SIZE - corner_size, (y+1) * CELL_SIZE), 2)
               
                # Update disappearing crystals
                if (x, y) in self.disappearing:
                    if self.grid[y][x]:
                        self.grid[y][x].scale *= 0.9
                        self.grid[y][x].disappearing = True
               
                # Draw crystal if it exists and isn't matched
                if self.grid[y][x] and not self.grid[y][x].matched:
                    self.grid[y][x].draw(x, y)
               
        # Draw UI elements with Wakandan-style border
        ui_rect = pygame.Rect(0, WINDOW_SIZE, WINDOW_WIDTH, 60)
        pygame.draw.rect(screen, (40, 35, 60), ui_rect)
       
        # Add decorative border to UI panel
        pygame.draw.line(screen, HIGHLIGHT_COLOR, (0, WINDOW_SIZE), (WINDOW_WIDTH, WINDOW_SIZE), 2)
       
        # Draw zigzag pattern in status bar
        for x in range(0, WINDOW_WIDTH, 20):
            pygame.draw.line(screen, (60, 55, 80),
                           (x, WINDOW_SIZE + 10),
                           (x + 10, WINDOW_SIZE + 20), 1)
       
        # Draw timer with vibranium glow effect
        time_color = (0, 255, 180) if self.time_left > 10 else (255, 50, 50)
        time_text = font.render(f"Time: {max(0, round(self.time_left))}s", True, time_color)
        screen.blit(time_text, (20, WINDOW_SIZE + 15))
       
        # Draw match count with vibranium glow
        match_text = font.render(f"Vibranium: {self.match_count}/8", True, (180, 180, 255))
        screen.blit(match_text, (200, WINDOW_SIZE + 15))
       
        # Show game over or mission complete message
        if self.game_over:
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
           
            message = large_font.render("MISSION FAILED", True, (255, 0, 0))
            text_rect = message.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40))
            screen.blit(message, text_rect)
           
            restart_text = font.render("Press R to try again", True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
            screen.blit(restart_text, restart_rect)
           
        elif self.mission_complete:
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
           
            message = large_font.render("WAKANDA FOREVER!", True, (0, 255, 180))
            text_rect = message.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40))
            screen.blit(message, text_rect)
           
            restart_text = font.render("Press R for new mission", True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
            screen.blit(restart_text, restart_rect)
       
        # Handle animations
        if self.animating:
            all_done = True
            for y in range(GRID_SIZE):
                for x in range(GRID_SIZE):
                    if self.grid[y][x] and not self.grid[y][x].move_towards_target():
                        all_done = False
           
            # Check if disappearing animations are complete
            for x, y in self.disappearing:
                if self.grid[y][x] and self.grid[y][x].scale > 0.1:
                    all_done = False
                elif self.grid[y][x]:
                    self.grid[y][x].matched = True
           
            if all_done:
                self.animating = False
                if self.disappearing:
                    self.drop_tiles()
                else:
                    self.check_matches()
               
    def swap(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
       
        # Swap grid positions
        self.grid[y1][x1], self.grid[y2][x2] = self.grid[y2][x2], self.grid[y1][x1]
       
        # Set animation targets
        if self.grid[y1][x1]:
            self.grid[y1][x1].target_x = 0
            self.grid[y1][x1].target_y = 0
            self.grid[y1][x1].x = (x2 - x1) * CELL_SIZE
            self.grid[y1][x1].y = (y2 - y1) * CELL_SIZE
           
        if self.grid[y2][x2]:
            self.grid[y2][x2].target_x = 0
            self.grid[y2][x2].target_y = 0
            self.grid[y2][x2].x = (x1 - x2) * CELL_SIZE
            self.grid[y2][x2].y = (y1 - y2) * CELL_SIZE
       
        self.animating = True
       
    def check_matches(self, set_disappearing=True):
        matches = set()
       
        # Horizontal matches
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE - 2):
                if (self.grid[y][x] and self.grid[y][x+1] and self.grid[y][x+2] and
                    not self.grid[y][x].matched and not self.grid[y][x+1].matched and
                    not self.grid[y][x+2].matched and
                    self.grid[y][x].type == self.grid[y][x+1].type == self.grid[y][x+2].type):
                    matches.update([(x+i, y) for i in range(3)])
                   
        # Vertical matches
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE - 2):
                if (self.grid[y][x] and self.grid[y+1][x] and self.grid[y+2][x] and
                    not self.grid[y][x].matched and not self.grid[y+1][x].matched and
                    not self.grid[y+2][x].matched and
                    self.grid[y][x].type == self.grid[y+1][x].type == self.grid[y+2][x].type):
                    matches.update([(x, y+i) for i in range(3)])
                   
        if matches and set_disappearing:
            self.disappearing = matches
            self.animating = True
            self.match_count += 1
            self.time_left += 2  # Add 5 seconds for each match
           
            # Check if mission is complete
            if self.match_count >= 8:
                self.mission_complete = True
           
        return bool(matches)
       
    def handle_click(self, pos):
        if self.animating or self.game_over or self.mission_complete:
            return
           
        x, y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            if self.selected is None:
                self.selected = (x, y)
            else:
                old_x, old_y = self.selected
                if ((abs(old_x - x) == 1 and old_y == y) or
                    (abs(old_y - y) == 1 and old_x == x)):
                   
                    # Store current state
                    original_grid = self.copy_grid()
                   
                    # Try the swap
                    self.swap(self.selected, (x, y))
                    self.selected = None
                   
                    # We'll check if it was a valid move after the animation
                    def after_animation():
                        if not self.check_matches():
                            # No matches found, swap back
                            self.grid = original_grid
                            self.swap(pos2=(old_x, old_y), pos1=(x, y))
                   
                    # Schedule check after animation
                    pygame.time.set_timer(pygame.USEREVENT, 300)  # 300ms delay
                else:
                    self.selected = None
               
    def copy_grid(self):
        # Make a deep copy of the grid for potential swap back
        new_grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if self.grid[y][x]:
                    new_crystal = Crystal(self.grid[y][x].type)
                    new_crystal.x = self.grid[y][x].x
                    new_crystal.y = self.grid[y][x].y
                    new_crystal.target_x = self.grid[y][x].target_x
                    new_crystal.target_y = self.grid[y][x].target_y
                    new_crystal.scale = self.grid[y][x].scale
                    new_crystal.matched = self.grid[y][x].matched
                    new_crystal.rotation = self.grid[y][x].rotation
                    new_grid[y][x] = new_crystal
        return new_grid
       
    def drop_tiles(self):
        # Mark matched tiles as None
        for x, y in self.disappearing:
            if self.grid[y][x] and self.grid[y][x].disappearing:
                self.grid[y][x] = None
               
        # Properly implement gravity - collect all crystals and reposition them
        for x in range(GRID_SIZE):
            # Collect all non-null crystals in this column
            crystals = []
            for y in range(GRID_SIZE):
                if self.grid[y][x] is not None:
                    crystals.append(self.grid[y][x])
                    self.grid[y][x] = None
           
            # Place crystals at the bottom of the column
            for i, crystal in enumerate(crystals):
                new_y = GRID_SIZE - len(crystals) + i
                self.grid[new_y][x] = crystal
                crystal.target_y = (new_y - (GRID_SIZE - len(crystals) + i)) * CELL_SIZE
                crystal.y = 0
           
            # Fill empty spaces at the top
            for y in range(GRID_SIZE - len(crystals)):
                new_crystal = Crystal(random.choice(CRYSTALS))
                new_crystal.y = -CELL_SIZE * (y + 1)
                new_crystal.target_y = 0
                self.grid[y][x] = new_crystal
                   
        self.disappearing.clear()
        self.animating = True
       
    def update(self):
        # Update timer
        if not self.game_over and not self.mission_complete:
            current_time = time.time()
            self.time_left -= current_time - self.start_time
            self.start_time = current_time
           
            # Check if time is up
            if self.time_left <= 0:
                self.time_left = 0
                self.game_over = True
               
    def reset(self):
        self.__init__()




def main():
    clock = pygame.time.Clock()
    game = Game()
   
    # Custom event for checking matches after animation
    CHECK_MATCH_EVENT = pygame.USEREVENT + 1
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    game.handle_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Press R to restart
                    game.reset()
            elif event.type == CHECK_MATCH_EVENT:
                if not game.animating and not game.check_matches():
                    # No matches found, revert the swap
                    pygame.time.set_timer(CHECK_MATCH_EVENT, 0)  # Cancel the timer
               
        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(60)




if __name__ == "__main__":
    main()



