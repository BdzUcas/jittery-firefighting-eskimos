def treat_trios():
    import pygame
    import random
    import sys
    pygame.init()
    WIDTH = 400
    GRID_SIZE = 8
    CELL_SIZE = WIDTH // GRID_SIZE
    class Button:
        def __init__(self, x, y, width, height, color, text):
            self.rect = pygame.Rect(x, y, width, height)
            self.color = color
            self.text = text
        def draw(self, screen, font):
            pygame.draw.rect(screen, self.color, self.rect)
            text_img = font.render(self.text, True, (0, 0, 0))
            x = self.rect.x + (self.rect.width - text_img.get_width()) // 2
            y = self.rect.y + (self.rect.height - text_img.get_height()) // 2
            screen.blit(text_img, (x, y))
        def is_clicked(self, pos):
            return self.rect.collidepoint(pos)
    def show_launcher():
        screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Treat Trios!")
        font = pygame.font.Font(None, 25)
        clock = pygame.time.Clock()
        start_btn = Button(100, 170, 200, 40, (0, 255, 0), "Start")
        quit_btn = Button(100, 230, 200, 40, (255, 0, 0), "Quit")
        while True:
            clock.tick(60)
            screen.fill((255, 255, 255))
            title = font.render("Treat Trios!", True, (0, 0, 0))
            screen.blit(title, (150, 30))
            desc1 = font.render("Swap treats to get three or more in a row.", True, (0, 0, 0))
            desc2 = font.render("Reach 15 points to get a tickets!", True, (0,0,0))
            desc1_rect = desc1.get_rect(center=(200, 100))
            desc2_rect = desc2.get_rect(center=(200, 130))
            screen.blit(desc1, desc1_rect)
            screen.blit(desc2, desc2_rect)
            start_btn.draw(screen, font)
            quit_btn.draw(screen, font)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_btn.is_clicked(event.pos):
                        run_game()
                    if quit_btn.is_clicked(event.pos):
                        pygame.quit()
    def handle_click(grid, row, col, selected_candy):
        if selected_candy is None:
            selected_candy = (row, col)
        else:
            row1, col1 = selected_candy
            grid[row][col], grid[row1][col1] = grid[row1][col1], grid[row][col]
            selected_candy = None
        return selected_candy
    def detect_match(grid):
        matches = set()
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE - 2):
                if grid[row][col] != 0 and grid[row][col] == grid[row][col + 1] == grid[row][col + 2]:
                    matches.update([(row, col), (row, col + 1), (row, col + 2)])
        for col in range(GRID_SIZE):
            for row in range(GRID_SIZE - 2):
                if grid[row][col] != 0 and grid[row][col] == grid[row + 1][col] == grid[row + 2][col]:
                    matches.update([(row, col), (row + 1, col), (row + 2, col)])
        return matches
    def fill_empty_spaces(grid):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if grid[row][col] == 0:
                    grid[row][col] = random.randint(1, 3)
    def create_grid():
        grid = []
        for row in range(GRID_SIZE):
            new_row = []
            for col in range(GRID_SIZE):
                new_row.append(random.randint(1, 3))
            grid.append(new_row)
        return grid
    def run_game():
        screen = pygame.display.get_surface()
        grid = create_grid()
        selected_candy = None
        running = True
        while running:
            screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // CELL_SIZE
                    row = event.pos[1] // CELL_SIZE
                    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                        selected_candy = handle_click(grid, row, col, selected_candy)
                        points = 0
            matches = detect_match(grid)
            if matches:
                for r, c in matches:
                    grid[r][c] = 0
                fill_empty_spaces(grid)
                try:
                    points
                except NameError:
                    pass
                else:
                    points += 1
                    if points == 15:
                        break
            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    candy_type = grid[row][col]
                    if candy_type == 1:
                        color = (255, 0, 0) # Red
                    elif candy_type == 2:
                        color = (0, 255, 0) # Green
                    elif candy_type == 3:
                        color = (0, 0, 255) # Blue
                    else:
                        color = (255, 255, 255) # White
                    pygame.draw.rect(screen, color, (col * CELL_SIZE + 1, row * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2))
                    if selected_candy == (row, col):
                        pygame.draw.rect(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)
            pygame.display.flip()
    show_launcher()