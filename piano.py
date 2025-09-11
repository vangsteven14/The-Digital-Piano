import pygame
import piano_lists as pl
from pygame import mixer

pygame.init()
pygame.mixer.set_num_channels(50)

# Initial setup and global variables
class Piano_Setup():
    def __init__(self):
        self.font = pygame.font.Font("assets/Roboto-Semibold.ttf", 48)
        self.medium_font = pygame.font.Font("assets/Roboto-Semibold.ttf", 28)
        self.small_font = pygame.font.Font("assets/Roboto-Semibold.ttf", 16)
        self.real_small_font = pygame.font.Font("assets/Roboto-Semibold.ttf", 10)

        self.fps = 60
        self.timer = pygame.time.Clock()
        self.WIDTH = 52 * 35
        self.HEIGHT = 400

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("The Digital Piano!")

        self.active_whites = []
        self.active_blacks = []
        self.white_sounds = []
        self.black_sounds = []

        self.left_hand = pl.left_hand
        self.right_hand = pl.right_hand
        self.piano_notes = pl.piano_notes
        self.white_notes = pl.white_notes
        self.black_notes = pl.black_notes
        self.black_labels = pl.black_labels

        self.left_octave = 4
        self.right_octave = 5

        for i in range(len(self.white_notes)):
            self.white_sounds.append(mixer.Sound(f'assets/notes/{self.white_notes[i]}.wav'))

        for i in range(len(self.black_notes)):
            self.black_sounds.append(mixer.Sound(f'assets/notes/{self.black_notes[i]}.wav'))

    def draw_hands(self, right_oct, left_oct, rightHand, leftHand):
        # Left hand keys
        pygame.draw.rect(self.screen, (10, 149, 242), [(left_oct * 245) - 175, self.HEIGHT - 60, 245, 30], 0, 4)
        pygame.draw.rect(self.screen, "black", [(left_oct * 245) - 175, self.HEIGHT - 60, 245, 30], 4, 4)
        text = self.small_font.render(leftHand[0], True, 'white')
        self.screen.blit(text, ((left_oct * 245) - 165, self.HEIGHT - 55))
        text = self.small_font.render(leftHand[2], True, 'white')
        self.screen.blit(text, ((left_oct * 245) - 130, self.HEIGHT - 55))
        text = self.small_font.render(leftHand[4], True, 'white')
        self.screen.blit(text, ((left_oct * 245) - 95, self.HEIGHT - 55))
        text = self.small_font.render(leftHand[5], True, 'white')
        self.screen.blit(text, ((left_oct * 245) - 60, self.HEIGHT - 55))
        text = self.small_font.render(leftHand[7], True, 'white')
        self.screen.blit(text, ((left_oct * 245) - 25, self.HEIGHT - 55))
        text = self.small_font.render(leftHand[9], True, 'white')
        self.screen.blit(text, ((left_oct * 245) + 10, self.HEIGHT - 55))
        text = self.small_font.render(leftHand[11], True, 'white')
        self.screen.blit(text, ((left_oct * 245) + 45, self.HEIGHT - 55))
        text = self.small_font.render(leftHand[1], True, 'black')
        self.screen.blit(text, ((left_oct * 245) - 148, self.HEIGHT - 55))
        text = self.small_font.render(leftHand[3], True, 'black')
        self.screen.blit(text, ((left_oct * 245) - 113, self.HEIGHT - 55))
        text = self.small_font.render(leftHand[6], True, 'black')
        self.screen.blit(text, ((left_oct * 245) - 43, self.HEIGHT - 55))
        text = self.small_font.render(leftHand[8], True, 'black')
        self.screen.blit(text, ((left_oct * 245) - 8, self.HEIGHT - 55))
        text = self.small_font.render(leftHand[10], True, 'black')
        self.screen.blit(text, ((left_oct * 245) + 27, self.HEIGHT - 55))

        # Right hand keys
        pygame.draw.rect(self.screen, (10, 149, 242), [(right_oct * 245) - 175, self.HEIGHT - 60, 245, 30], 0, 4)
        pygame.draw.rect(self.screen, "black", [(right_oct * 245) - 175, self.HEIGHT - 60, 245, 30], 4, 4)
        text = self.small_font.render(rightHand[0], True, 'white')
        self.screen.blit(text, ((right_oct * 245) - 165, self.HEIGHT - 55))
        text = self.small_font.render(rightHand[2], True, 'white')
        self.screen.blit(text, ((right_oct * 245) - 130, self.HEIGHT - 55))
        text = self.small_font.render(rightHand[4], True, 'white')
        self.screen.blit(text, ((right_oct * 245) - 95, self.HEIGHT - 55))
        text = self.small_font.render(rightHand[5], True, 'white')
        self.screen.blit(text, ((right_oct * 245) - 60, self.HEIGHT - 55))
        text = self.small_font.render(rightHand[7], True, 'white')
        self.screen.blit(text, ((right_oct * 245) - 25, self.HEIGHT - 55))
        text = self.small_font.render(rightHand[9], True, 'white')
        self.screen.blit(text, ((right_oct * 245) + 10, self.HEIGHT - 55))
        text = self.small_font.render(rightHand[11], True, 'white')
        self.screen.blit(text, ((right_oct * 245) + 45, self.HEIGHT - 55))
        text = self.small_font.render(rightHand[1], True, 'black')
        self.screen.blit(text, ((right_oct * 245) - 148, self.HEIGHT - 55))
        text = self.small_font.render(rightHand[3], True, 'black')
        self.screen.blit(text, ((right_oct * 245) - 113, self.HEIGHT - 55))
        text = self.small_font.render(rightHand[6], True, 'black')
        self.screen.blit(text, ((right_oct * 245) - 43, self.HEIGHT - 55))
        text = self.small_font.render(rightHand[8], True, 'black')
        self.screen.blit(text, ((right_oct * 245) - 8, self.HEIGHT - 55))
        text = self.small_font.render(rightHand[10], True, 'black')
        self.screen.blit(text, ((right_oct * 245) + 27, self.HEIGHT - 55))

    def draw_piano(self, whites, blacks):
        white_rects = []
        black_rects = []
        skip_count = 0
        last_skip = 2
        skip_track = 2

        # Draw white keys
        for i in range(52):
            rect = pygame.draw.rect(self.screen, "white", [i * 35, self.HEIGHT - 300, 35, 300], 0, 2)
            white_rects.append(rect)
            pygame.draw.rect(self.screen, "black", [i * 35, self.HEIGHT - 300, 35, 300], 2, 2)
            key_label = self.small_font.render(self.white_notes[i], True, "black")
            self.screen.blit(key_label, (i * 35 + 3, self.HEIGHT - 20))

        # Draw black keys
        for i in range(36):
            rect = pygame.draw.rect(self.screen, "black", [23 + (i * 35) + (skip_count * 35), self.HEIGHT - 300, 24, 200], 0, 2)

            # Draw active black keys being played via green rectangles
            for j in range(len(blacks)):
                if blacks[j][0] == i:
                    if blacks[j][1] > 0:
                        pygame.draw.rect(self.screen, "green", [23 + (i * 35) + (skip_count * 35), self.HEIGHT - 300, 24, 200], 2, 2)
                        blacks[j][1] -= 1

            key_label = self.real_small_font.render(self.black_labels[i], True, "white")
            self.screen.blit(key_label, (25 + (i * 35) + (skip_count * 35), self.HEIGHT - 20))
            black_rects.append(rect)
            skip_track += 1

            if last_skip == 2 and skip_track == 3:
                last_skip = 3
                skip_track = 0
                skip_count += 1
            elif last_skip == 3 and skip_track == 2:
                last_skip = 2
                skip_track = 0
                skip_count += 1

        # Draw active white keys being played via green rectangles
        for i in range(len(whites)):
            if whites[i][1] > 0:
                j = whites[i][0]
                pygame.draw.rect(self.screen, "green", [j * 35, self.HEIGHT - 100, 35, 100], 2, 2)
                whites[i][1] -= 1

        return white_rects, black_rects, whites, blacks
    
    def draw_title_bar(self):
        instruction_text_left = self.medium_font.render("Up/Down Arrows for Left Hand Octaves", True, "black")
        self.screen.blit(instruction_text_left, (self.WIDTH - 550, 10))
        instruction_text_right = self.medium_font.render("Left/Right Arrows for Right Hand Octaves", True, "black")
        self.screen.blit(instruction_text_right, (self.WIDTH - 550, 50))
        img = pygame.transform.scale(pygame.image.load("assets/svang_logo.png"), [80, 80])
        self.screen.blit(img, (10, 5))
        title_text = self.font.render("The Digital Piano!", True, "white")
        self.screen.blit(title_text, (298, 18))
        title_text = self.font.render("The Digital Piano!", True, "black")
        self.screen.blit(title_text, (300, 20))

    def run_piano(self):
        run = True

        while run:
            # Create dictionaries for left and right hand key mappings
            left_dict = {
                "Z": f'C{self.left_octave}',
                "S": f'C#{self.left_octave}',
                "X": f'D{self.left_octave}',
                "D": f'D#{self.left_octave}',
                "C": f'E{self.left_octave}',
                "V": f'F{self.left_octave}',
                "G": f'F#{self.left_octave}',
                "B": f'G{self.left_octave}',
                "H": f'G#{self.left_octave}',
                "N": f'A{self.left_octave}',
                "J": f'A#{self.left_octave}',
                "M": f'B{self.left_octave}'
            }

            right_dict = {
                "Y": f'C{self.right_octave}',
                "7": f'C#{self.right_octave}',
                "U": f'D{self.right_octave}',
                "8": f'D#{self.right_octave}',
                "I": f'E{self.right_octave}',
                "O": f'F{self.right_octave}',
                "0": f'F#{self.right_octave}',
                "P": f'G{self.right_octave}',
                "-": f'G#{self.right_octave}',
                "[": f'A{self.right_octave}',
                "=": f'A#{self.right_octave}',
                "]": f'B{self.right_octave}'
            }

            # Functions for running the piano application
            self.timer.tick(self.fps)
            self.screen.fill((10, 149, 242))
            white_keys, black_keys, self.active_whites, self.active_blacks = self.draw_piano(self.active_whites, self.active_blacks)
            self.draw_hands(self.right_octave, self.left_octave, self.right_hand, self.left_hand)
            self.draw_title_bar()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    black_key = False

                    for i in range(len(black_keys)):
                        if black_keys[i].collidepoint(event.pos):
                            self.black_sounds[i].play(0, 1000)
                            black_key = True
                            self.active_blacks.append([i, 30])
                    for i in range(len(white_keys)):
                        if white_keys[i].collidepoint(event.pos) and not black_key:
                            self.white_sounds[i].play(0, 1000)
                            self.active_whites.append([i, 30])

                if event.type == pygame.TEXTINPUT:
                    if event.text.upper() in left_dict:
                        if left_dict[event.text.upper()][1] == "#":
                            index = self.black_labels.index(left_dict[event.text.upper()])
                            self.black_sounds[index].play(0, 1000)
                            self.active_blacks.append([index, 30])
                        else:
                            index = self.white_notes.index(left_dict[event.text.upper()])
                            self.white_sounds[index].play(0, 1000)
                            self.active_whites.append([index, 30])
                    if event.text.upper() in right_dict:
                        if right_dict[event.text.upper()][1] == "#":
                            index = self.black_labels.index(right_dict[event.text.upper()])
                            self.black_sounds[index].play(0, 1000)
                            self.active_blacks.append([index, 30])
                        else:
                            index = self.white_notes.index(right_dict[event.text.upper()])
                            self.white_sounds[index].play(0, 1000)
                            self.active_whites.append([index, 30])

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if self.right_octave < 8:
                            self.right_octave += 1
                    if event.key == pygame.K_LEFT:
                        if self.right_octave > 0:
                            self.right_octave -= 1
                    if event.key == pygame.K_UP:
                        if self.left_octave < 8:
                            self.left_octave += 1
                    if event.key == pygame.K_DOWN:
                        if self.left_octave > 0:
                            self.left_octave -= 1

            pygame.display.flip()
        pygame.quit()
        
def main():
    piano = Piano_Setup()
    piano.run_piano()

if __name__ == "__main__":
    main()