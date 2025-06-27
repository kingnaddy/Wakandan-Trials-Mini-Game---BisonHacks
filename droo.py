# Wakanda: Shuri's Neural Scan (Themed Match Game)
# Inspired by Wakanda Tech and Shuri's hacking system

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
WINDOW_HEIGHT = WINDOW_SIZE + 60  # Extra space for HUD
SHAPES = ['vibranium_core', 'energy_orb', 'tribal_rune', 'panther_mask', 'wakandan_chip', 'hologram_node']

# Wakandan color palette
COLORS = {
    'vibranium_core': (0, 255, 255),       # Vibranium glow blue
    'energy_orb': (255, 255, 255),          # Energy orb white
    'tribal_rune': (255, 204, 0),           # Royal gold
    'panther_mask': (102, 0, 204),          # Deep purple
    'wakandan_chip': (0, 255, 128),         # Tech green
    'hologram_node': (255, 51, 153)         # Pink hologram pulse
}

# Setup display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Shuri's Neural Scan")

# Fonts
font = pygame.font.SysFont("Orbitron", 28)
large_font = pygame.font.SysFont("Orbitron", 60)

class Shape:
    def __init__(self, shape_type):
        self.type = shape_type
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0
        self.scale = 1.0
        self.matched = False
        self.disappearing = False

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
            return

        base_x = grid_x * CELL_SIZE + CELL_SIZE // 2
        base_y = grid_y * CELL_SIZE + CELL_SIZE // 2
        center = (int(base_x + self.x), int(base_y + self.y))
        color = COLORS[self.type]

        pygame.draw.circle(screen, color, center, int(20 * self.scale))

class Game:
    def __init__(self):
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.fill_grid()
        self.selected = None
        self.animating = False
        self.disappearing = set()
        self.check_initial_matches()
        self.match_count = 0
        self.time_left = 15.0
        self.start_time = time.time()
        self.game_over = False
        self.mission_complete = False

    def fill_grid(self):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                self.grid[y][x] = Shape(random.choice(SHAPES))
                self.grid[y][x].x = 0
                self.grid[y][x].y = 0
                self.grid[y][x].target_x = 0
                self.grid[y][x].target_y = 0

    def check_initial_matches(self):
        max_retries = 10
        while self.check_matches(False) and max_retries > 0:
            for y in range(GRID_SIZE):
                for x in range(GRID_SIZE):
                    if (x, y) in self.disappearing:
                        self.grid[y][x] = Shape(random.choice(SHAPES))
            self.disappearing.clear()
            max_retries -= 1

    def draw(self):
        screen.fill((0, 0, 0))
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                pygame.draw.rect(screen, (30, 30, 30), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                if self.selected == (x, y):
                    pygame.draw.rect(screen, (255, 255, 0), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
                if (x, y) in self.disappearing:
                    if self.grid[y][x]:
                        self.grid[y][x].scale *= 0.9
                        self.grid[y][x].disappearing = True
                if self.grid[y][x] and not self.grid[y][x].matched:
                    self.grid[y][x].draw(x, y)

        pygame.draw.rect(screen, (50, 50, 50), (0, WINDOW_SIZE, WINDOW_WIDTH, 60))
        time_text = font.render(f"Time: {max(0, round(self.time_left))}s", True, (255, 255, 255))
        screen.blit(time_text, (20, WINDOW_SIZE + 15))
        match_text = font.render(f"Matches: {self.match_count}/8", True, (255, 255, 255))
        screen.blit(match_text, (200, WINDOW_SIZE + 15))

        if self.game_over:
            self.draw_overlay("SECURITY BREACH - Override Failed", (255, 0, 0))
        elif self.mission_complete:
            self.draw_overlay("ACCESS GRANTED - Neural Sync Complete", (0, 255, 0))

        if self.animating:
            all_done = True
            for y in range(GRID_SIZE):
                for x in range(GRID_SIZE):
                    if self.grid[y][x] and not self.grid[y][x].move_towards_target():
                        all_done = False
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

    def draw_overlay(self, message, color):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        message_render = large_font.render(message, True, color)
        text_rect = message_render.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40))
        screen.blit(message_render, text_rect)
        restart_text = font.render("Press R to restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
        screen.blit(restart_text, restart_rect)

    def update(self):
        if not self.game_over and not self.mission_complete:
            current_time = time.time()
            self.time_left -= current_time - self.start_time
            self.start_time = current_time
            if self.time_left <= 0:
                self.time_left = 0
                self.game_over = True

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
                    self.swap(self.selected, (x, y))
                    self.selected = None
                else:
                    self.selected = None

    def swap(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        self.grid[y1][x1], self.grid[y2][x2] = self.grid[y2][x2], self.grid[y1][x1]
        self.grid[y1][x1].x = (x2 - x1) * CELL_SIZE
        self.grid[y1][x1].y = (y2 - y1) * CELL_SIZE
        self.grid[y1][x1].target_x = 0
        self.grid[y1][x1].target_y = 0
        self.grid[y2][x2].x = (x1 - x2) * CELL_SIZE
        self.grid[y2][x2].y = (y1 - y2) * CELL_SIZE
        self.grid[y2][x2].target_x = 0
        self.grid[y2][x2].target_y = 0
        self.animating = True

    def check_matches(self, set_disappearing=True):
        matches = set()
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE - 2):
                if (self.grid[y][x] and self.grid[y][x+1] and self.grid[y][x+2] and
                    self.grid[y][x].type == self.grid[y][x+1].type == self.grid[y][x+2].type):
                    matches.update([(x+i, y) for i in range(3)])
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE - 2):
                if (self.grid[y][x] and self.grid[y+1][x] and self.grid[y+2][x] and
                    self.grid[y][x].type == self.grid[y+1][x].type == self.grid[y+2][x].type):
                    matches.update([(x, y+i) for i in range(3)])
        if matches and set_disappearing:
            self.disappearing = matches
            self.animating = True
            self.match_count += 1
            self.time_left += 1
            if self.match_count >= 8:
                self.mission_complete = True
        return bool(matches)

    def drop_tiles(self):
        for x, y in self.disappearing:
            if self.grid[y][x] and self.grid[y][x].disappearing:
                self.grid[y][x] = None
        for x in range(GRID_SIZE):
            shapes = [self.grid[y][x] for y in range(GRID_SIZE) if self.grid[y][x] is not None]
            for y in range(GRID_SIZE):
                self.grid[y][x] = None
            for i, shape in enumerate(shapes):
                new_y = GRID_SIZE - len(shapes) + i
                self.grid[new_y][x] = shape
                shape.target_y = (new_y - i) * CELL_SIZE
                shape.y = 0
            for y in range(GRID_SIZE - len(shapes)):
                new_shape = Shape(random.choice(SHAPES))
                new_shape.y = -CELL_SIZE * (y + 1)
                new_shape.target_y = 0
                self.grid[y][x] = new_shape
        self.disappearing.clear()
        self.animating = True

    def reset(self):
        self.__init__()

def main():
    clock = pygame.time.Clock()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                game.handle_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game.reset()
        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

