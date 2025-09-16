import pygame

class Piano_Functions():
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