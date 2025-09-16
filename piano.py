import pygame
from piano_init import Piano_Init
from piano_funcs import Piano_Functions

class Piano_Main(Piano_Init, Piano_Functions):
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
    piano = Piano_Main()
    piano.run_piano()

if __name__ == "__main__":
    main()