import pygame, pygame.freetype, os; import random; import subprocess, sys; pygame.init(); pygame.freetype.init(); DIR_PROPS = os.path.join(os.path.dirname(__file__), "Props"); DIR_BRANDING = os.path.join(os.path.dirname(__file__), "Branding"); DIR_DATA = os.path.join(os.path.dirname(__file__), "Data")
WINDOW = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.FULLSCREEN | pygame.SRCALPHA); pygame.display.set_caption("2048", "2048"); LOGO = pygame.image.load(os.path.join(DIR_BRANDING, "Logo.png")).convert_alpha(); pygame.display.set_icon(LOGO); MARGIN = WINDOW.width / 100; OPTIONS_WIDTH = WINDOW.width / 20

COLOUR_BLACK = (0, 0, 0); COLOUR_DARK = (30, 30, 30); COLOUR_WHITE = (255, 255, 255)
FONT_SIZE_1 = pygame.freetype.Font(os.path.join(DIR_PROPS, "Font.otf"), WINDOW.height / 4); FONT_SIZE_2 = pygame.freetype.Font(os.path.join(DIR_PROPS, "Font.otf"), WINDOW.height / 6); FONT_SIZE_3 = pygame.freetype.Font(os.path.join(DIR_PROPS, "Font.otf"), WINDOW.height / 8); FONT_SIZE_4 = pygame.freetype.Font(os.path.join(DIR_PROPS, "Font.otf"), WINDOW.height / 10)
def image_shaders(image, colour): image = image.copy(); image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT); image.fill(colour + (0,), None, pygame.BLEND_RGBA_ADD); return image
IMAGE_BUTTON_CLOSE = pygame.transform.scale(pygame.image.load(os.path.join(DIR_PROPS, "Close#Button.png")).convert_alpha(), (OPTIONS_WIDTH, OPTIONS_WIDTH)); CLOSE_X = (WINDOW.width - OPTIONS_WIDTH) - MARGIN; IMAGE_BUTTON_HELP = pygame.transform.scale(pygame.image.load(os.path.join(DIR_PROPS, "Settings-Help#Button.png")).convert_alpha(), (OPTIONS_WIDTH, OPTIONS_WIDTH)); IMAGE_BUTTON_dark_ON = pygame.transform.scale(pygame.image.load(os.path.join(DIR_PROPS, "Settings-Dark=True#Button.png")).convert_alpha(), (OPTIONS_WIDTH, OPTIONS_WIDTH)); IMAGE_BUTTON_dark_OFF = pygame.transform.scale(pygame.image.load(os.path.join(DIR_PROPS, "Settings-Dark=False#Button.png")).convert_alpha(), (OPTIONS_WIDTH, OPTIONS_WIDTH))
statistics = open(os.path.join(DIR_DATA, "statistics")).readlines(); victories = eval(statistics[0]); defeats = eval(statistics[1]); best_scores = eval(statistics[2])
board = eval(open(os.path.join(DIR_DATA, "board"), "r").readlines()[0])
for BOARD_SIZE in range(2, 7):
    if all(board[BOARD_SIZE]["blocks"][space] <= 8 for space in range(0, 36)): board[BOARD_SIZE] = {"score": 0, "blocks": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}; game_state = [False, False, -1]
    else: game_state = [True, None, -1]
BOARD = pygame.Surface(((WINDOW.width / 3) + (WINDOW.width / 8), (WINDOW.width / 3) + (WINDOW.width / 8)), pygame.SRCALPHA); pygame.draw.rect(BOARD, COLOUR_BLACK, (0, 0, BOARD.width, BOARD.width), border_radius=int(MARGIN * 2)); BOARD_X = (WINDOW.width / 2) - (BOARD.width / 2); BOARD_Y = MARGIN if not game_state[0] else WINDOW.height - MARGIN - BOARD.height
BLOCKS = {0: pygame.image.load(os.path.join(DIR_PROPS, "Block=0.png")).convert_alpha(), 2: pygame.image.load(os.path.join(DIR_PROPS, "Block=2.png")).convert_alpha(), 4: pygame.image.load(os.path.join(DIR_PROPS, "Block=4.png")).convert_alpha(), 8: pygame.image.load(os.path.join(DIR_PROPS, "Block=8.png")).convert_alpha(), 16: pygame.image.load(os.path.join(DIR_PROPS, "Block=16.png")).convert_alpha(), 32: pygame.image.load(os.path.join(DIR_PROPS, "Block=32.png")).convert_alpha(), 64: pygame.image.load(os.path.join(DIR_PROPS, "Block=64.png")).convert_alpha(), 128: pygame.image.load(os.path.join(DIR_PROPS, "Block=128.png")).convert_alpha(), 256: pygame.image.load(os.path.join(DIR_PROPS, "Block=256.png")).convert_alpha(), 512: pygame.image.load(os.path.join(DIR_PROPS, "Block=512.png")).convert_alpha(), 1024: pygame.image.load(os.path.join(DIR_PROPS, "Block=1024.png")).convert_alpha(), 2048: pygame.image.load(os.path.join(DIR_PROPS, "Block=2048.png")).convert_alpha(), 4096: pygame.image.load(os.path.join(DIR_PROPS, "Block=4096.png")).convert_alpha(), 8192: pygame.image.load(os.path.join(DIR_PROPS, "Block=8192.png")).convert_alpha(), 16384: pygame.image.load(os.path.join(DIR_PROPS, "Block=16384.png")).convert_alpha()}
class Space:
    def __init__(self, position: list, value: int | None = 0): self.position = position; self.value = value
    def move(self, space: int) -> bool:
        if not 0 <= space < 36: return None
        if spaces[space].value == 0: spaces[space].value = self.value; self.value = 0; return True
        elif spaces[space].value == self.value: spaces[space].value += self.value; self.value = 0; board[BOARD_SIZE]["score"] += spaces[space].value; best_scores[BOARD_SIZE-2] = board[BOARD_SIZE]["score"] if board[BOARD_SIZE]["score"] > best_scores[BOARD_SIZE-2] else best_scores[BOARD_SIZE-2]; TEXTS["score"]["surface"] = FONT_SIZE_1.render(f"{board[BOARD_SIZE]["score"]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["score"]["position"][0] = (WINDOW.width / 2) - (TEXTS["score"]["surface"].width / 2); TEXTS["best score"]["surface"] = FONT_SIZE_1.render(f"{best_scores[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["best score"]["position"][0] = BOARD_X + BOARD.width + ((WINDOW.width - (BOARD_X + BOARD.width)) / 2) - (TEXTS["best score"]["surface"].width / 2); return True
        return False
preferences = open(os.path.join(DIR_DATA, "preferences"), "r").readlines(); dark = bool(int(preferences[0])); FONT_COLOUR = COLOUR_WHITE if dark else COLOUR_BLACK; COLOUR_DEFAULT = COLOUR_DARK if dark else COLOUR_WHITE; BLOCKS[0] = image_shaders(BLOCKS[0], COLOUR_DEFAULT); BOARD_SIZE = int(preferences[1])
BOARD_SIZE_GOAL = {2: 512, 3: 1024, 4: 2048, 5: 4096, 6: 16384}
BOARD_SIZE_RELEVANT_SPACES = {2: {"A": [0, 1, 6, 7], "U": [6, 7], "L": [1, 7], "D": [0, 1], "R": [0, 6]}, 3: {"A": [0, 1, 2, 6, 7, 8, 12, 13, 14], "U": [6, 7, 8, 12, 13, 14], "L": [1, 2, 7, 8, 13, 14], "D": [8, 7, 6, 2, 1, 0], "R": [13, 12, 7, 6, 1, 0]}, 4: {"A": [0, 1, 2, 3, 6, 7, 8, 9, 12, 13, 14, 15, 18, 19, 20, 21], "U": [6, 7, 8, 9, 12, 13, 14, 15, 18, 19, 20, 21], "L": [1, 2, 3, 7, 8, 9, 13, 14, 15, 19, 20, 21], "D": [15, 14, 13, 12, 9, 8, 7, 6, 3, 2, 1, 0], "R": [20, 19, 18, 14, 13, 12, 8, 7, 6, 2, 1, 0]}, 5: {"A": [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28], "U": [6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28], "L": [1, 2, 3, 4, 7, 8, 9, 10, 13, 14, 15, 16, 19, 20, 21, 22, 25, 26, 27, 28], "D": [22, 21, 20, 19, 18, 16, 15, 14, 13, 12, 10, 9, 8, 7, 6, 4, 3, 2, 1, 0], "R": [27, 26, 25, 24, 21, 20, 19, 18, 15, 14, 13, 12, 9, 8, 7, 6, 3, 2, 1, 0]}, 6: {"A": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], "U": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], "L": [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35], "D": [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], "R": [34, 33, 32, 31, 30, 28, 27, 26, 25, 24, 22, 21, 20, 19, 18, 16, 15, 14, 13, 12, 10, 9, 8, 7, 6, 4, 3, 2, 1, 0]}}
SPACE_WIDTH = (BOARD.width - ((MARGIN / 2) * (BOARD_SIZE+1))) / BOARD_SIZE; spaces = []
for BLOCK in BLOCKS: BLOCKS[BLOCK] = pygame.transform.scale(BLOCKS[BLOCK], (SPACE_WIDTH, SPACE_WIDTH))
for board_column, board_row in ((board_column, board_row) for board_row in range(6) for board_column in range(6)): space = (6 * board_row) + board_column; spaces.append(Space([BOARD_X + (MARGIN * (0.5 * (board_column + 1))) + (SPACE_WIDTH * board_column), BOARD_Y + (MARGIN * (0.5 * (board_row + 1))) + (SPACE_WIDTH * board_row)], board[BOARD_SIZE]["blocks"][space]))
del board_row, board_column, space
TEXTS = {":victories:": {"surface": FONT_SIZE_3.render(":victories:", FONT_COLOUR)[0].convert_alpha()}, "victories": {"surface": FONT_SIZE_1.render(f"{victories[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha()}, "score": {"surface": FONT_SIZE_1.render(f"{board[BOARD_SIZE]["score"]}", FONT_COLOUR)[0].convert_alpha()}, "board size": {"surface": FONT_SIZE_1.render(f"{BOARD_SIZE}", FONT_COLOUR)[0].convert_alpha()}, "you jammed the board!": {"surface": FONT_SIZE_3.render("you jammed the board!", FONT_COLOUR)[0].convert_alpha()}, ":best score:": {"surface": FONT_SIZE_3.render(":best score:", FONT_COLOUR)[0].convert_alpha()}, "best score": {"surface": FONT_SIZE_1.render(f"{best_scores[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha()}}
TEXTS[":victories:"]["position"] = [((WINDOW.width - BOARD.width) / 4) - (TEXTS[":victories:"]["surface"].width / 2), (WINDOW.height / 2) - (OPTIONS_WIDTH * 1.5) - MARGIN - TEXTS[":victories:"]["surface"].height]; TEXTS["victories"]["position"] = [((WINDOW.width - BOARD.width) / 4) - (TEXTS["victories"]["surface"].width / 2), (WINDOW.height / 2) + (OPTIONS_WIDTH * 1.5) + MARGIN]; TEXTS["score"]["position"] = [(WINDOW.width / 2) - (TEXTS["score"]["surface"].width / 2), -TEXTS["score"]["surface"].height if not game_state[0] else MARGIN]; TEXTS["board size"]["position"] = [(WINDOW.width / 2) - (TEXTS["board size"]["surface"].width / 2), WINDOW.height - MARGIN - TEXTS["board size"]["surface"].height if not game_state[0] else WINDOW.height]; TEXTS["you jammed the board!"]["position"] = [(WINDOW.width / 2) - (TEXTS["you jammed the board!"]["surface"].width / 2), -TEXTS["you jammed the board!"]["surface"].height]; TEXTS[":best score:"]["position"] = [BOARD_X + BOARD.width + ((WINDOW.width - (BOARD_X + BOARD.width)) / 2) - (TEXTS[":best score:"]["surface"].width / 2), (WINDOW.height / 2) - (TEXTS["best score"]["surface"].height / 2) - MARGIN - TEXTS[":best score:"]["surface"].height]; TEXTS["best score"]["position"] = [BOARD_X + BOARD.width + ((WINDOW.width - (BOARD_X + BOARD.width)) / 2) - (TEXTS["best score"]["surface"].width / 2), (WINDOW.height / 2) - (TEXTS["best score"]["surface"].height / 2)]
LOGO_X = ((WINDOW.width - BOARD.width) / 4) - (OPTIONS_WIDTH * 1.5); LOGO_Y = (WINDOW.height / 2) - (OPTIONS_WIDTH * 1.5)
BUTTON_BOARD_SIZE_DECREASE = [[TEXTS["board size"]["position"][0] - MARGIN - OPTIONS_WIDTH, TEXTS["board size"]["position"][1] + (TEXTS["board size"]["surface"].height / 2)], [TEXTS["board size"]["position"][0] - MARGIN, TEXTS["board size"]["position"][1] + (TEXTS["board size"]["surface"].height / 2) - (OPTIONS_WIDTH / 2)], [TEXTS["board size"]["position"][0] - MARGIN, TEXTS["board size"]["position"][1] + (TEXTS["board size"]["surface"].height / 2) + (OPTIONS_WIDTH / 2)]]; BUTTON_BOARD_SIZE_INCREASE = [[TEXTS["board size"]["position"][0] + TEXTS["board size"]["surface"].width + MARGIN, TEXTS["board size"]["position"][1] + (TEXTS["board size"]["surface"].height / 2) - (OPTIONS_WIDTH / 2)], [TEXTS["board size"]["position"][0] + TEXTS["board size"]["surface"].width + MARGIN, TEXTS["board size"]["position"][1] + (TEXTS["board size"]["surface"].height / 2) + (OPTIONS_WIDTH / 2)], [TEXTS["board size"]["position"][0] + TEXTS["board size"]["surface"].width + MARGIN + OPTIONS_WIDTH, TEXTS["board size"]["position"][1] + (TEXTS["board size"]["surface"].height / 2)]]; BUTTON_CONTINUE = [[BOARD_X + BOARD.width - MARGIN - (OPTIONS_WIDTH * 2), BOARD_Y + BOARD.height + MARGIN], [BOARD_X + BOARD.width - MARGIN, BOARD_Y + BOARD.height + MARGIN], [BOARD_X + BOARD.width - MARGIN - OPTIONS_WIDTH, BOARD_Y + BOARD.height + MARGIN + (OPTIONS_WIDTH / 2)]]


def main(direction: str | None = ""):
    global game_state, victories, best_scores, defeats, spaces, BOARD_Y, LOGO_X, LOGO_Y, BUTTON_CONTINUE
    
    WINDOW.fill(COLOUR_DEFAULT)
    WINDOW.blit(IMAGE_BUTTON_CLOSE if dark else image_shaders(IMAGE_BUTTON_CLOSE, COLOUR_BLACK), (CLOSE_X, MARGIN)); WINDOW.blit(IMAGE_BUTTON_dark_ON if dark else IMAGE_BUTTON_dark_OFF, (MARGIN, MARGIN)); WINDOW.blit(IMAGE_BUTTON_HELP if dark else image_shaders(IMAGE_BUTTON_HELP, COLOUR_BLACK), (MARGIN, OPTIONS_WIDTH + (MARGIN * 2)))
    if board[BOARD_SIZE]["score"] > best_scores[BOARD_SIZE-2]: best_scores[BOARD_SIZE-2] = board[BOARD_SIZE]["score"]
    if victories[BOARD_SIZE-2] > 0: WINDOW.blit(pygame.transform.scale(BLOCKS[BOARD_SIZE_GOAL[BOARD_SIZE]], (OPTIONS_WIDTH * 3, OPTIONS_WIDTH * 3)), (LOGO_X, LOGO_Y)); WINDOW.blit(TEXTS[":victories:"]["surface"], TEXTS[":victories:"]["position"]); WINDOW.blit(TEXTS["victories"]["surface"], TEXTS["victories"]["position"])
    
    if direction:
        other_space = -6 if direction == "U" else -1 if direction == "L" else +1 if direction == "R" else +6 if direction == "D" else -36
        for _ in range(BOARD_SIZE):
            for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE][direction]:
                if spaces[space].value == 0: continue
                spaces[space].move(space+other_space)
        del other_space
    WINDOW.blit(BOARD, (BOARD_X, BOARD_Y))
    for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]: board[BOARD_SIZE]["blocks"][space] = spaces[space].value; WINDOW.blit(BLOCKS[spaces[space].value], (spaces[space].position[0], spaces[space].position[1]))
    save_progress("board"); WINDOW.blit(TEXTS["score"]["surface"], TEXTS["score"]["position"]); WINDOW.blit(TEXTS[":best score:"]["surface"], TEXTS[":best score:"]["position"]); WINDOW.blit(TEXTS["best score"]["surface"], TEXTS["best score"]["position"]); pygame.display.update()
    
    if game_state[0]:
        if all(spaces[space].value and spaces[space].value != BOARD_SIZE_GOAL[BOARD_SIZE] for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]) and all(spaces[space].value != spaces[space-6].value for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["U"]) and all(spaces[space].value != spaces[space-1].value for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["L"]) and all(spaces[space].value != spaces[space+1].value for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["R"]) and all(spaces[space].value != spaces[space+6].value for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["D"]): game_state = [True, False, -1]
        if game_state[1]:
            victories[BOARD_SIZE-2] += 1; save_progress("statistics"); board[BOARD_SIZE]["blocks"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; save_progress("board"); pygame.time.wait(1500)
            WINDOW.blit(BLOCKS[0], (spaces[game_state[2]].position[0], spaces[game_state[2]].position[1])); SNAPSHOT = WINDOW.copy(); space_x_step = (LOGO_X - spaces[game_state[2]].position[0]) / 500; space_y_step = (LOGO_Y - spaces[game_state[2]].position[1]) / 500; space_width_step = ((OPTIONS_WIDTH * 3) - SPACE_WIDTH) / 500
            for space_step in range(501): WINDOW.blit(SNAPSHOT, (0, 0)); WINDOW.blit(pygame.transform.scale(BLOCKS[spaces[game_state[2]].value], (SPACE_WIDTH + (space_width_step * space_step), SPACE_WIDTH + (space_width_step * space_step))), (spaces[game_state[2]].position[0] + (space_x_step * space_step), spaces[game_state[2]].position[1] + (space_y_step * space_step))); pygame.display.update()
            del SNAPSHOT, space_step, space_x_step, space_y_step, space_width_step; spaces[game_state[2]].value = 0; pygame.time.wait(1000)
            COLOUR_ALPHA = 12.75; dissappear = True
            while BOARD.get_alpha() > 0:
                BOARD.set_alpha(BOARD.get_alpha() - int(COLOUR_ALPHA))
                if TEXTS["victories"]["surface"].get_alpha() <= 0: dissappear = False; TEXTS["victories"]["surface"] = FONT_SIZE_1.render(f"{victories[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["victories"]["surface"].set_alpha(0)
                TEXTS["victories"]["surface"].set_alpha(TEXTS["victories"]["surface"].get_alpha() - int((COLOUR_ALPHA if dissappear else -COLOUR_ALPHA) * 2))
                for BLOCK in BLOCKS: BLOCKS[BLOCK].set_alpha(BLOCKS[BLOCK].get_alpha() - int(COLOUR_ALPHA))
                pygame.draw.rect(WINDOW, COLOUR_DEFAULT, (BOARD_X, BOARD_Y, BOARD.width, BOARD.width)); WINDOW.blit(BOARD, (BOARD_X, BOARD_Y))
                for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]: WINDOW.blit(BLOCKS[spaces[space].value], (spaces[space].position[0], spaces[space].position[1]))
                pygame.draw.rect(WINDOW, COLOUR_DEFAULT, (TEXTS["victories"]["position"][0], TEXTS["victories"]["position"][1], TEXTS["victories"]["surface"].width, TEXTS["victories"]["surface"].height)); WINDOW.blit(TEXTS["victories"]["surface"], TEXTS["victories"]["position"])
                pygame.display.update()
            for space in spaces: space.value = 0
            for BLOCK in BLOCKS: BLOCKS[BLOCK].set_alpha(255)
            BOARD.set_alpha(255); game_state = [True, None, -1]; del COLOUR_ALPHA, dissappear; main()
        elif game_state[1] == False:
            defeats[BOARD_SIZE-2] += 1; save_progress("statistics"); board[BOARD_SIZE] = {"score": 0, "blocks": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}; save_progress("board")
            pygame.time.wait(2000)
            while TEXTS["score"]["position"][1] > -TEXTS["score"]["surface"].height:
                if TEXTS["you jammed the board!"]["position"][1] < (BOARD_Y / 2) - (TEXTS["you jammed the board!"]["surface"].height / 2): TEXTS["you jammed the board!"]["position"][1] += MARGIN / 8
                TEXTS["score"]["position"][1] -= MARGIN / 8
                pygame.draw.rect(WINDOW, COLOUR_DEFAULT, ((WINDOW.width / 2) - (TEXTS["you jammed the board!"]["surface"].width / 2), 0, TEXTS["you jammed the board!"]["surface"].width, BOARD_Y)); WINDOW.blit(TEXTS["you jammed the board!"]["surface"], TEXTS["you jammed the board!"]["position"]); WINDOW.blit(TEXTS["score"]["surface"], TEXTS["score"]["position"])
                pygame.display.update()
            pygame.time.wait(2000)
            COLOUR_ALPHA = 12.75; BOARD_displacement = BOARD_Y - MARGIN
            while BOARD_Y > MARGIN:
                if TEXTS["you jammed the board!"]["position"][1] > -TEXTS["you jammed the board!"]["surface"].height: TEXTS["you jammed the board!"]["position"][1] -= MARGIN / 8
                BOARD_Y -= MARGIN / 8
                if BOARD_Y - MARGIN <= BOARD_displacement / 2:
                    BOARD.set_alpha(BOARD.get_alpha() - int(COLOUR_ALPHA))
                    for BLOCK in BLOCKS: BLOCKS[BLOCK].set_alpha(BLOCKS[BLOCK].get_alpha() - int(COLOUR_ALPHA))
                for space in spaces: space.position[1] -= MARGIN / 8
                if TEXTS["board size"]["position"][1] > WINDOW.height - MARGIN - TEXTS["board size"]["surface"].height: BUTTON_BOARD_SIZE_DECREASE[0][1] -= MARGIN / 8; BUTTON_BOARD_SIZE_DECREASE[1][1] -= MARGIN / 8; BUTTON_BOARD_SIZE_DECREASE[2][1] -= MARGIN / 8; TEXTS["board size"]["position"][1] -= MARGIN / 8; BUTTON_BOARD_SIZE_INCREASE[0][1] -= MARGIN / 8; BUTTON_BOARD_SIZE_INCREASE[1][1] -= MARGIN / 8; BUTTON_BOARD_SIZE_INCREASE[2][1] -= MARGIN / 8; BUTTON_CONTINUE[0][1] -= MARGIN / 8; BUTTON_CONTINUE[1][1] -= MARGIN / 8; BUTTON_CONTINUE[2][1] -= MARGIN / 8
                pygame.draw.rect(WINDOW, COLOUR_DEFAULT, ((WINDOW.width / 2) - (TEXTS["you jammed the board!"]["surface"].width / 2), 0, TEXTS["you jammed the board!"]["surface"].width, WINDOW.height))
                WINDOW.blit(TEXTS["you jammed the board!"]["surface"], TEXTS["you jammed the board!"]["position"]); WINDOW.blit(BOARD, (BOARD_X, BOARD_Y)); pygame.draw.polygon(WINDOW, (COLOUR_DEFAULT) if BOARD_SIZE == 2 else FONT_COLOUR, BUTTON_BOARD_SIZE_DECREASE); WINDOW.blit(TEXTS["board size"]["surface"], TEXTS["board size"]["position"]); pygame.draw.polygon(WINDOW, (COLOUR_DEFAULT) if BOARD_SIZE == 6 else FONT_COLOUR, BUTTON_BOARD_SIZE_INCREASE); pygame.draw.polygon(WINDOW, FONT_COLOUR, BUTTON_CONTINUE)
                for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]: WINDOW.blit(BLOCKS[spaces[space].value], (spaces[space].position[0], spaces[space].position[1]))
                pygame.display.update()
            for space in spaces: space.value = 0
            for BLOCK in BLOCKS: BLOCKS[BLOCK].set_alpha(255)
            BOARD.set_alpha(255); game_state[0] = False; del COLOUR_ALPHA, BOARD_displacement; main()
        else:
            if direction: space = random.choice(BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]); spaces[space].value = random.choice((0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 8)) if spaces[space].value == 0 else spaces[space].value
    else:
        if game_state[1]:
            board_irrelevant = all(board[BOARD_SIZE]["blocks"][space] <= 8 and not all(board[BOARD_SIZE]["blocks"][space] == 0 for space in range(0, 36)) for space in range(0, 36))
            if board_irrelevant: board[BOARD_SIZE] = {"score": 0, "blocks": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}; COLOUR_ALPHA = 12.75; BOARD_displacement = BOARD_Y - MARGIN
            while BOARD_Y > MARGIN:
                if TEXTS["board size"]["position"][1] > WINDOW.height - MARGIN - TEXTS["board size"]["surface"].height: BUTTON_BOARD_SIZE_DECREASE[0][1] -= MARGIN / 8; BUTTON_BOARD_SIZE_DECREASE[1][1] -= MARGIN / 8; BUTTON_BOARD_SIZE_DECREASE[2][1] -= MARGIN / 8; TEXTS["board size"]["position"][1] -= MARGIN / 8; BUTTON_BOARD_SIZE_INCREASE[0][1] -= MARGIN / 8; BUTTON_BOARD_SIZE_INCREASE[1][1] -= MARGIN / 8; BUTTON_BOARD_SIZE_INCREASE[2][1] -= MARGIN / 8; BUTTON_CONTINUE[0][1] -= MARGIN / 8; BUTTON_CONTINUE[1][1] -= MARGIN / 8; BUTTON_CONTINUE[2][1] -= MARGIN / 8
                BOARD_Y -= MARGIN / 8
                if board_irrelevant and BOARD_Y - MARGIN <= BOARD_displacement / 8:
                    BOARD.set_alpha(BOARD.get_alpha() - int(COLOUR_ALPHA))
                    for BLOCK in BLOCKS: BLOCKS[BLOCK].set_alpha(BLOCKS[BLOCK].get_alpha() - int(COLOUR_ALPHA))
                for space in spaces: space.position[1] -= MARGIN / 8
                if TEXTS["score"]["position"][1] > -TEXTS["score"]["surface"].height: TEXTS["score"]["position"][1] -= MARGIN / 8
                pygame.draw.rect(WINDOW, COLOUR_DEFAULT, (BOARD_X, 0, BOARD.width, WINDOW.height))
                WINDOW.blit(TEXTS["score"]["surface"], TEXTS["score"]["position"]); WINDOW.blit(BOARD, (BOARD_X, BOARD_Y)); pygame.draw.polygon(WINDOW, (COLOUR_DEFAULT) if BOARD_SIZE == 2 else FONT_COLOUR, BUTTON_BOARD_SIZE_DECREASE); WINDOW.blit(TEXTS["board size"]["surface"], TEXTS["board size"]["position"]); pygame.draw.polygon(WINDOW, (COLOUR_DEFAULT) if BOARD_SIZE == 6 else FONT_COLOUR, BUTTON_BOARD_SIZE_INCREASE); pygame.draw.polygon(WINDOW, FONT_COLOUR, BUTTON_CONTINUE)
                for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]: WINDOW.blit(BLOCKS[spaces[space].value], (spaces[space].position[0], spaces[space].position[1]))
                pygame.display.update()
            if board_irrelevant:
                for space in spaces: space.value = 0
                for BLOCK in BLOCKS: BLOCKS[BLOCK].set_alpha(255)
                BOARD.set_alpha(255); game_state[1] = False; del board_irrelevant, COLOUR_ALPHA, BOARD_displacement
            else: game_state[1] = False
            main()
        elif game_state[1] == False: pygame.draw.polygon(WINDOW, (COLOUR_DEFAULT) if BOARD_SIZE == 2 else FONT_COLOUR, BUTTON_BOARD_SIZE_DECREASE); WINDOW.blit(TEXTS["board size"]["surface"], TEXTS["board size"]["position"]); pygame.draw.polygon(WINDOW, (COLOUR_DEFAULT) if BOARD_SIZE == 6 else FONT_COLOUR, BUTTON_BOARD_SIZE_INCREASE); pygame.draw.polygon(WINDOW, FONT_COLOUR, BUTTON_CONTINUE)
        elif game_state[1] == None:
            while BOARD_Y + BOARD.height < WINDOW.height - MARGIN:
                if BUTTON_CONTINUE[0][1] < WINDOW.height: BUTTON_BOARD_SIZE_DECREASE[0][1] += MARGIN / 8; BUTTON_BOARD_SIZE_DECREASE[1][1] += MARGIN / 8; BUTTON_BOARD_SIZE_DECREASE[2][1] += MARGIN / 8; TEXTS["board size"]["position"][1] += MARGIN / 8; BUTTON_BOARD_SIZE_INCREASE[0][1] += MARGIN / 8; BUTTON_BOARD_SIZE_INCREASE[1][1] += MARGIN / 8; BUTTON_BOARD_SIZE_INCREASE[2][1] += MARGIN / 8; BUTTON_CONTINUE[0][1] += MARGIN / 8; BUTTON_CONTINUE[1][1] += MARGIN / 8; BUTTON_CONTINUE[2][1] += MARGIN / 8
                BOARD_Y += MARGIN / 8
                for space in spaces: space.position[1] += MARGIN / 8
                if TEXTS["score"]["position"][1] < MARGIN: TEXTS["score"]["position"][1] += MARGIN / 8
                pygame.draw.rect(WINDOW, COLOUR_DEFAULT, (BOARD_X, 0, BOARD.width, WINDOW.height))
                WINDOW.blit(TEXTS["score"]["surface"], TEXTS["score"]["position"]); WINDOW.blit(BOARD, (BOARD_X, BOARD_Y)); pygame.draw.polygon(WINDOW, (COLOUR_DEFAULT) if BOARD_SIZE == 2 else FONT_COLOUR, BUTTON_BOARD_SIZE_DECREASE); WINDOW.blit(TEXTS["board size"]["surface"], TEXTS["board size"]["position"]); pygame.draw.polygon(WINDOW, (COLOUR_DEFAULT) if BOARD_SIZE == 6 else FONT_COLOUR, BUTTON_BOARD_SIZE_INCREASE); pygame.draw.polygon(WINDOW, FONT_COLOUR, BUTTON_CONTINUE)
                for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]: WINDOW.blit(BLOCKS[spaces[space].value], (spaces[space].position[0], spaces[space].position[1]))
                pygame.display.update()
            game_state[0] = True
    pygame.display.update()

def save_progress(progress: str):
    with open(os.path.join(DIR_DATA, f"{progress}#temporary"), "w") as save: save.write(str(board) if progress == "board" else f"{1 if dark else 0}\n{BOARD_SIZE}" if progress == "preferences" else f"{victories}\n{defeats}\n{best_scores}" if progress == "statistics" else f"Guide for 2048\n================================================================================\n\n* Controls:\n  * Setting:\n    * 'esc' closes the game;\n    * '-' & '=' toggle COLOUR_DARKness;\n    * '/' or 'h' opens this [guide];\n    * 'left' or 'right' change the board's width;\n  * Playing:\n    * 'enter' or 'space' start the game;\n    * 'w' or 'up' shift the blocks up;\n    * 'a' or 'left' shift the blocks left;\n    * 's' or 'down' shift the blocks down;\n    * 'd' or 'right' shift the blocks right;\n    * 'r' clears the board & score;\n\n* Statistics:\n  * Victories:\n    * on a 2-wide board -- requires '512': {victories[0]};\n    * on a 3-wide board -- requires '1024': {victories[1]};\n    * on a 4-wide board -- requires '2048': {victories[2]};\n    * on a 5-wide board -- requires '4096': {victories[3]};\n    * on a 6-wide board -- requires '16384': {victories[4]};\n  * Defeats:\n    * on a 2-wide board: {defeats[0]};\n    * on a 3-wide board: {defeats[1]};\n    * on a 4-wide board: {defeats[2]};\n    * on a 5-wide board: {defeats[3]};\n    * on a 6-wide board: {defeats[4]};\n  * Best scores:\n    * on a 2-wide board: {best_scores[0]};\n    * on a 3-wide board: {best_scores[1]};\n    * on a 4-wide board: {best_scores[2]};\n    * on a 5-wide board: {best_scores[3]};\n    * on a 6-wide board: {best_scores[4]};")
    os.replace(os.path.join(DIR_DATA, f"{progress}#temporary"), os.path.join(DIR_DATA, f"{progress}"))

key_pressed = False; CLOCK = pygame.time.Clock(); main()
while game_state[0] != None: # `game_state[0]` -- "is player playing the game?"; `game_state[1]` -- "has the player won?"; `game_state[2]` -- "space the player won on":
    # [None, False, -1]: Terminate
    # [False, False, -1]: Main menu
    # [False, True, -1]: Animate BOARD_SIZE selector & BOARD & score go up -> [False, False, -1]
    # [False, None, -1]: Animate BOARD_SIZE selector & BOARD down with score coming from above -> [True, None, -1]
    # [True, None, -1]: Play game -> [True, False, -1] or [True, True, -1<int<36] or [False, True, -1]
    # [True, False, -1]: Animate score going up & "you jammed the board" going down; then "you jammed the board" & BOARD go up -- BOARD flashing its values blank, with BOARD_SIZE selector coming from below -> [False, False, -1]
    # [True, True, -1<int<36]: Animate block = spaces[-1<int<36] going to the 'times won' place; then BOARD flashing its values blank -- continuing the game -> [True, None, -1]
    CLOCK.tick(100) # 99.9+% of the lag is caused by this: limiting my game to 100 frames per Second
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_SLASH or event.key == pygame.K_h or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: pygame.time.wait(100); key_pressed = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if CLOSE_X <= mouse_x <= CLOSE_X + OPTIONS_WIDTH and MARGIN <= mouse_y <= MARGIN + OPTIONS_WIDTH: game_state = [False, True, -1] if game_state[0] else [None, False, -1]; main()
            if MARGIN <= mouse_x <= MARGIN + OPTIONS_WIDTH and MARGIN <= mouse_y <= MARGIN + OPTIONS_WIDTH: dark = False if dark else True; save_progress("preferences"); FONT_COLOUR = COLOUR_WHITE if dark else COLOUR_BLACK; COLOUR_DEFAULT = COLOUR_DARK if dark else COLOUR_WHITE; BLOCKS[0] = image_shaders(BLOCKS[0], COLOUR_DEFAULT); TEXTS[":victories:"]["surface"] = FONT_SIZE_3.render(":victories:", FONT_COLOUR)[0].convert_alpha(); TEXTS["victories"]["surface"] = FONT_SIZE_1.render(f"{victories[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["score"]["surface"] = FONT_SIZE_1.render(f"{board[BOARD_SIZE]["score"]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["board size"]["surface"] = FONT_SIZE_1.render(f"{BOARD_SIZE}", FONT_COLOUR)[0].convert_alpha(); TEXTS["you jammed the board!"]["surface"] = FONT_SIZE_3.render("you jammed the board!", FONT_COLOUR)[0].convert_alpha(); TEXTS[":best score:"]["surface"] = FONT_SIZE_3.render(":best score:", FONT_COLOUR)[0].convert_alpha(); TEXTS["best score"]["surface"] = FONT_SIZE_1.render(f"{best_scores[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); main()
            if MARGIN <= mouse_x <= MARGIN + OPTIONS_WIDTH and MARGIN + OPTIONS_WIDTH + MARGIN <= mouse_y <= MARGIN + (OPTIONS_WIDTH * 2) + MARGIN: save_progress("Help.txt"); os.startfile(os.path.join(DIR_DATA, "Help.txt")) if sys.platform.startswith("win") else subprocess.run(["open", os.path.join(DIR_DATA, "Help.txt")]) if sys.platform == "darwin" else subprocess.run(["xdg-open", os.path.join(DIR_DATA, "Help.txt")])
            if game_state[0]:
                pass
            else:
                if game_state[1] == False:
                    if (BUTTON_BOARD_SIZE_DECREASE[0][0] <= mouse_x <= BUTTON_BOARD_SIZE_DECREASE[1][0] and BUTTON_BOARD_SIZE_DECREASE[1][1] <= mouse_y <= BUTTON_BOARD_SIZE_DECREASE[2][1]) and BOARD_SIZE > 2: 
                        BOARD_SIZE -= 1; save_progress("preferences"); SPACE_WIDTH = (BOARD.width - ((MARGIN / 2) * (BOARD_SIZE+1))) / BOARD_SIZE; spaces = []
                        for BLOCK in BLOCKS: BLOCKS[BLOCK] = pygame.transform.scale(BLOCKS[BLOCK], (SPACE_WIDTH, SPACE_WIDTH))
                        for board_column, board_row in ((board_column, board_row) for board_row in range(6) for board_column in range(6)): space = (6 * board_row) + board_column; spaces.append(Space([BOARD_X + (MARGIN * (0.5 * (board_column + 1))) + (SPACE_WIDTH * board_column), BOARD_Y + (MARGIN * (0.5 * (board_row + 1))) + (SPACE_WIDTH * board_row)], board[BOARD_SIZE]["blocks"][space]))
                        del board_row, board_column, space
                        TEXTS["victories"]["surface"] = FONT_SIZE_1.render(f"{victories[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["score"]["surface"] = FONT_SIZE_1.render(f"{board[BOARD_SIZE]["score"]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["board size"]["surface"] = FONT_SIZE_1.render(f"{BOARD_SIZE}", FONT_COLOUR)[0].convert_alpha(); TEXTS["best score"]["surface"] = FONT_SIZE_1.render(f"{best_scores[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["victories"]["position"] = [((WINDOW.width - BOARD.width) / 4) - (TEXTS["victories"]["surface"].width / 2), (WINDOW.height / 2) + (OPTIONS_WIDTH * 1.5) + MARGIN]; TEXTS["score"]["position"] = [(WINDOW.width / 2) - (TEXTS["score"]["surface"].width / 2), -TEXTS["score"]["surface"].height if not game_state[0] else MARGIN]; TEXTS["best score"]["position"][0] = BOARD_X + BOARD.width + ((WINDOW.width - (BOARD_X + BOARD.width)) / 2) - (TEXTS["best score"]["surface"].width / 2); main()
                        main()
                    if (BUTTON_BOARD_SIZE_INCREASE[0][0] <= mouse_x <= BUTTON_BOARD_SIZE_INCREASE[2][0] and BUTTON_BOARD_SIZE_INCREASE[0][1] <= mouse_y <= BUTTON_BOARD_SIZE_INCREASE[1][1]) and BOARD_SIZE < 6:
                        BOARD_SIZE += 1; save_progress("preferences"); SPACE_WIDTH = (BOARD.width - ((MARGIN / 2) * (BOARD_SIZE+1))) / BOARD_SIZE; spaces = []
                        for BLOCK in BLOCKS: BLOCKS[BLOCK] = pygame.transform.scale(BLOCKS[BLOCK], (SPACE_WIDTH, SPACE_WIDTH))
                        for board_column, board_row in ((board_column, board_row) for board_row in range(6) for board_column in range(6)): space = (6 * board_row) + board_column; spaces.append(Space([BOARD_X + (MARGIN * (0.5 * (board_column + 1))) + (SPACE_WIDTH * board_column), BOARD_Y + (MARGIN * (0.5 * (board_row + 1))) + (SPACE_WIDTH * board_row)], board[BOARD_SIZE]["blocks"][space]))
                        del board_row, board_column, space
                        TEXTS["victories"]["surface"] = FONT_SIZE_1.render(f"{victories[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["score"]["surface"] = FONT_SIZE_1.render(f"{board[BOARD_SIZE]["score"]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["board size"]["surface"] = FONT_SIZE_1.render(f"{BOARD_SIZE}", FONT_COLOUR)[0].convert_alpha(); TEXTS["best score"]["surface"] = FONT_SIZE_1.render(f"{best_scores[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["victories"]["position"] = [((WINDOW.width - BOARD.width) / 4) - (TEXTS["victories"]["surface"].width / 2), (WINDOW.height / 2) + (OPTIONS_WIDTH * 1.5) + MARGIN]; TEXTS["score"]["position"] = [(WINDOW.width / 2) - (TEXTS["score"]["surface"].width / 2), -TEXTS["score"]["surface"].height if not game_state[0] else MARGIN]; TEXTS["best score"]["position"][0] = BOARD_X + BOARD.width + ((WINDOW.width - (BOARD_X + BOARD.width)) / 2) - (TEXTS["best score"]["surface"].width / 2); main()
                        main()
                    if BUTTON_CONTINUE[0][0] <= mouse_x <= BUTTON_CONTINUE[1][0] and BUTTON_CONTINUE[0][1] <= mouse_y <= BUTTON_CONTINUE[2][1]:
                        space = random.choice(BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]); spaces[space].value = random.choice((0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 8)) if sum(board[BOARD_SIZE]["blocks"]) == 0 else spaces[space].value; space = random.choice(BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]); spaces[space].value = random.choice((0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 8)) if sum(board[BOARD_SIZE]["blocks"]) == 0 else spaces[space].value
                        game_state[1] = None; main()
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_ESCAPE] and not key_pressed: key_pressed = True; game_state = [False, True, -1] if game_state[0] else [None, False, -1]; main()
    if (pressed_key[pygame.K_SLASH] or pressed_key[pygame.K_h]) and not key_pressed: key_pressed = True; save_progress("Help.txt"); os.startfile(os.path.join(DIR_DATA, "Help.txt")) if sys.platform.startswith("win") else subprocess.run(["open", os.path.join(DIR_DATA, "Help.txt")]) if sys.platform == "darwin" else subprocess.run(["xdg-open", os.path.join(DIR_DATA, "Help.txt")])
    if pressed_key[pygame.K_MINUS] and not dark: dark = True; save_progress("preferences"); FONT_COLOUR = COLOUR_WHITE; COLOUR_DEFAULT = COLOUR_DARK; BLOCKS[0] = image_shaders(BLOCKS[0], COLOUR_DARK); TEXTS[":victories:"]["surface"] = FONT_SIZE_3.render(":victories:", COLOUR_WHITE)[0]; TEXTS["victories"]["surface"] = FONT_SIZE_1.render(f"{victories[BOARD_SIZE-2]}", COLOUR_WHITE)[0]; TEXTS["score"]["surface"] = FONT_SIZE_1.render(f"{board[BOARD_SIZE]["score"]}", COLOUR_WHITE)[0]; TEXTS["board size"]["surface"] = FONT_SIZE_1.render(f"{BOARD_SIZE}", COLOUR_WHITE)[0]; TEXTS["you jammed the board!"]["surface"] = FONT_SIZE_3.render("you jammed the board!", COLOUR_WHITE)[0]; TEXTS[":best score:"]["surface"] = FONT_SIZE_3.render(":best score:", COLOUR_WHITE)[0]; TEXTS["best score"]["surface"] = FONT_SIZE_1.render(f"{best_scores[BOARD_SIZE-2]}", COLOUR_WHITE)[0]; main()
    if pressed_key[pygame.K_EQUALS] and dark: dark = False; save_progress("preferences"); FONT_COLOUR = COLOUR_BLACK; COLOUR_DEFAULT = COLOUR_WHITE; BLOCKS[0] = image_shaders(BLOCKS[0], COLOUR_WHITE); TEXTS[":victories:"]["surface"] = FONT_SIZE_3.render(":victories:", COLOUR_BLACK)[0].convert_alpha(); TEXTS["victories"]["surface"] = FONT_SIZE_1.render(f"{victories[BOARD_SIZE-2]}", COLOUR_BLACK)[0].convert_alpha(); TEXTS["score"]["surface"] = FONT_SIZE_1.render(f"{board[BOARD_SIZE]["score"]}", COLOUR_BLACK)[0].convert_alpha(); TEXTS["board size"]["surface"] = FONT_SIZE_1.render(f"{BOARD_SIZE}", COLOUR_BLACK)[0].convert_alpha(); TEXTS["you jammed the board!"]["surface"] = FONT_SIZE_3.render("you jammed the board!", COLOUR_BLACK)[0].convert_alpha(); TEXTS[":best score:"]["surface"] = FONT_SIZE_3.render(":best score:", COLOUR_BLACK)[0].convert_alpha(); TEXTS["best score"]["surface"] = FONT_SIZE_1.render(f"{best_scores[BOARD_SIZE-2]}", COLOUR_BLACK)[0].convert_alpha(); main()
    if game_state[0]:
        if game_state[1] == None:
            if pressed_key[pygame.K_r]:
                COLOUR_ALPHA = 255
                while COLOUR_ALPHA > 0:
                    COLOUR_ALPHA -= 12.75; BOARD.set_alpha(COLOUR_ALPHA)
                    for BLOCK in BLOCKS: BLOCKS[BLOCK].set_alpha(COLOUR_ALPHA)
                    pygame.draw.rect(WINDOW, COLOUR_DEFAULT, (BOARD_X, BOARD_Y, BOARD.width, BOARD.width)); WINDOW.blit(BOARD, (BOARD_X, BOARD_Y))
                    for space in BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]: WINDOW.blit(BLOCKS[spaces[space].value], (spaces[space].position[0], spaces[space].position[1]))
                    pygame.display.update()
                for space in spaces: space.value = 0
                for BLOCK in BLOCKS: BLOCKS[BLOCK].set_alpha(255)
                BOARD.set_alpha(255); del COLOUR_ALPHA
                board[BOARD_SIZE]["score"] = 0; TEXTS["score"]["surface"] = FONT_SIZE_1.render(f"{board[BOARD_SIZE]["score"]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["score"]["position"][0] = (WINDOW.width / 2) - (TEXTS["score"]["surface"].width / 2); spaces[random.randint(0, 35)].value = random.choice((0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 8)); main()
            if pressed_key[pygame.K_w] or pressed_key[pygame.K_UP]: main("U")
            if pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]: main("L")
            if pressed_key[pygame.K_s] or pressed_key[pygame.K_DOWN]: main("D")
            if pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]: main("R")
    else:
        if game_state[1] == False:
            if pressed_key[pygame.K_LEFT] and BOARD_SIZE > 2 and not key_pressed:
                key_pressed = True; BOARD_SIZE -= 1; save_progress("preferences"); SPACE_WIDTH = (BOARD.width - ((MARGIN / 2) * (BOARD_SIZE+1))) / BOARD_SIZE; spaces = []
                for BLOCK in BLOCKS: BLOCKS[BLOCK] = pygame.transform.scale(BLOCKS[BLOCK], (SPACE_WIDTH, SPACE_WIDTH))
                for board_column, board_row in ((board_column, board_row) for board_row in range(6) for board_column in range(6)): space = (6 * board_row) + board_column; spaces.append(Space([BOARD_X + (MARGIN * (0.5 * (board_column + 1))) + (SPACE_WIDTH * board_column), BOARD_Y + (MARGIN * (0.5 * (board_row + 1))) + (SPACE_WIDTH * board_row)], board[BOARD_SIZE]["blocks"][space]))
                del board_row, board_column, space
                TEXTS["victories"]["surface"] = FONT_SIZE_1.render(f"{victories[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["score"]["surface"] = FONT_SIZE_1.render(f"{board[BOARD_SIZE]["score"]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["board size"]["surface"] = FONT_SIZE_1.render(f"{BOARD_SIZE}", FONT_COLOUR)[0].convert_alpha(); TEXTS["best score"]["surface"] = FONT_SIZE_1.render(f"{best_scores[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["victories"]["position"] = [((WINDOW.width - BOARD.width) / 4) - (TEXTS["victories"]["surface"].width / 2), (WINDOW.height / 2) + (OPTIONS_WIDTH * 1.5) + MARGIN]; TEXTS["score"]["position"] = [(WINDOW.width / 2) - (TEXTS["score"]["surface"].width / 2), -TEXTS["score"]["surface"].height if not game_state[0] else MARGIN]; TEXTS["best score"]["position"][0] = BOARD_X + BOARD.width + ((WINDOW.width - (BOARD_X + BOARD.width)) / 2) - (TEXTS["best score"]["surface"].width / 2); main()
            if pressed_key[pygame.K_RIGHT] and BOARD_SIZE < 6 and not key_pressed:
                key_pressed = True; BOARD_SIZE += 1; save_progress("preferences"); SPACE_WIDTH = (BOARD.width - ((MARGIN / 2) * (BOARD_SIZE+1))) / BOARD_SIZE; spaces = []
                for BLOCK in BLOCKS: BLOCKS[BLOCK] = pygame.transform.scale(BLOCKS[BLOCK], (SPACE_WIDTH, SPACE_WIDTH))
                for board_column, board_row in ((board_column, board_row) for board_row in range(6) for board_column in range(6)): space = (6 * board_row) + board_column; spaces.append(Space([BOARD_X + (MARGIN * (0.5 * (board_column + 1))) + (SPACE_WIDTH * board_column), BOARD_Y + (MARGIN * (0.5 * (board_row + 1))) + (SPACE_WIDTH * board_row)], board[BOARD_SIZE]["blocks"][space]))
                del board_row, board_column, space
                TEXTS["victories"]["surface"] = FONT_SIZE_1.render(f"{victories[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["score"]["surface"] = FONT_SIZE_1.render(f"{board[BOARD_SIZE]["score"]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["board size"]["surface"] = FONT_SIZE_1.render(f"{BOARD_SIZE}", FONT_COLOUR)[0].convert_alpha(); TEXTS["best score"]["surface"] = FONT_SIZE_1.render(f"{best_scores[BOARD_SIZE-2]}", FONT_COLOUR)[0].convert_alpha(); TEXTS["victories"]["position"] = [((WINDOW.width - BOARD.width) / 4) - (TEXTS["victories"]["surface"].width / 2), (WINDOW.height / 2) + (OPTIONS_WIDTH * 1.5) + MARGIN]; TEXTS["score"]["position"] = [(WINDOW.width / 2) - (TEXTS["score"]["surface"].width / 2), -TEXTS["score"]["surface"].height if not game_state[0] else MARGIN]; TEXTS["best score"]["position"][0] = BOARD_X + BOARD.width + ((WINDOW.width - (BOARD_X + BOARD.width)) / 2) - (TEXTS["best score"]["surface"].width / 2); main()
            if pressed_key[pygame.K_RETURN] or pressed_key[pygame.K_DOWN]: space = random.choice(BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]); spaces[space].value = random.choice((0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 8)) if sum(board[BOARD_SIZE]["blocks"]) == 0 else spaces[space].value; space = random.choice(BOARD_SIZE_RELEVANT_SPACES[BOARD_SIZE]["A"]); spaces[space].value = random.choice((0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 8)) if sum(board[BOARD_SIZE]["blocks"]) == 0 else spaces[space].value; game_state[1] = None; main()
pygame.quit()