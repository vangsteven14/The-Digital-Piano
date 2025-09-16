import pygame
from pygame import mixer

pygame.init()
pygame.mixer.set_num_channels(50)

# Initial setup and global variables
class Piano_Init():
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

        self.left_hand = ['Z', 'S', 'X', 'D', 'C', 'V', 'G', 'B', 'H', 'N', 'J', 'M']
        self.right_hand = ['Y', '7', 'U', '8', 'I', 'O', '0', 'P', '-', '[', '=', ']']

        self.piano_notes = ['A0', 'A0#', 'B0', 'C1', 'C1#', 'D1', 'D1#', 'E1', 'F1', 'F1#', 'G1', 'G1#',
                    'A1', 'A1#', 'B1', 'C2', 'C2#', 'D2', 'D2#', 'E2', 'F2', 'F2#', 'G2', 'G2#',
                    'A2', 'A2#', 'B2', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#',
                    'A3', 'A3#', 'B3', 'C4', 'C4#', 'D4', 'D4#', 'E4', 'F4', 'F4#', 'G4', 'G4#',
                    'A4', 'A4#', 'B4', 'C5', 'C5#', 'D5', 'D5#', 'E5', 'F5', 'F5#', 'G5', 'G5#',
                    'A5', 'A5#', 'B5', 'C6', 'C6#', 'D6', 'D6#', 'E6', 'F6', 'F6#', 'G6', 'G6#',
                    'A6', 'A6#', 'B6', 'C7', 'C7#', 'D7', 'D7#', 'E7', 'F7', 'F7#', 'G7', 'G7#',
                    'A7', 'A7#', 'B7', 'C8']

        self.white_notes = ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1',
                    'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2',
                    'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3',
                    'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4',
                    'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5',
                    'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6',
                    'A6', 'B6', 'C7', 'D7', 'E7', 'F7', 'G7',
                    'A7', 'B7', 'C8']

        self.black_notes = ['Bb0', 'Db1', 'Eb1', 'Gb1', 'Ab1',
                    'Bb1', 'Db2', 'Eb2', 'Gb2', 'Ab2',
                    'Bb2', 'Db3', 'Eb3', 'Gb3', 'Ab3',
                    'Bb3', 'Db4', 'Eb4', 'Gb4', 'Ab4',
                    'Bb4', 'Db5', 'Eb5', 'Gb5', 'Ab5',
                    'Bb5', 'Db6', 'Eb6', 'Gb6', 'Ab6',
                    'Bb6', 'Db7', 'Eb7', 'Gb7', 'Ab7',
                    'Bb7']

        self.black_labels = ['A#0', 'C#1', 'D#1', 'F#1', 'G#1',
                        'A#1', 'C#2', 'D#2', 'F#2', 'G#2',
                        'A#2', 'C#3', 'D#3', 'F#3', 'G#3',
                        'A#3', 'C#4', 'D#4', 'F#4', 'G#4',
                        'A#4', 'C#5', 'D#5', 'F#5', 'G#5',
                        'A#5', 'C#6', 'D#6', 'F#6', 'G#6',
                        'A#6', 'C#7', 'D#7', 'F#7', 'G#7',
                        'A#7']

        self.left_octave = 4
        self.right_octave = 5

        for i in range(len(self.white_notes)):
            self.white_sounds.append(mixer.Sound(f'assets/notes/{self.white_notes[i]}.wav'))

        for i in range(len(self.black_notes)):
            self.black_sounds.append(mixer.Sound(f'assets/notes/{self.black_notes[i]}.wav'))