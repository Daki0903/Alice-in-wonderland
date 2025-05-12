import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

# Zvukovi
click_sound = pygame.mixer.Sound("assets/click_sound.wav")
correct_sound = pygame.mixer.Sound("assets/correct_sound.wav")
wrong_sound = pygame.mixer.Sound("assets/wrong_sound.wav")

WIDTH, HEIGHT = 960, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alice: Lost in Wonderland")

# Učitavanje slika
scenes = {
    "intro": pygame.image.load("assets/intro.png"),
    "woods": pygame.image.load("assets/whispering_woods.png"),
    "tea": pygame.image.load("assets/mad_tea_garden.png"),
    "queen": pygame.image.load("assets/card_kingdom.png"),
    "mirror": pygame.image.load("assets/mirror_forest.png"),
    "finale": pygame.image.load("assets/final_escape.png")
}

# Font i boje
font = pygame.font.SysFont("georgia", 28)
WHITE = (255, 255, 255)

def draw_text(text, x, y, surface, size=28, color=WHITE):
    font = pygame.font.SysFont("georgia", size)
    lines = text.split("\n")
    for i, line in enumerate(lines):
        rendered = font.render(line, True, color)
        surface.blit(rendered, (x, y + i * size * 1.5))

def text_input(prompt_text):
    user_text = ''
    input_active = True

    while input_active:
        screen.fill((0, 0, 0))
        draw_text(prompt_text, 30, 100, screen, 32)
        draw_text(user_text, 30, 200, screen, 32, (200, 255, 200))
        input_box = pygame.Rect(25, 190, 600, 40)
        pygame.draw.rect(screen, (255, 255, 255), input_box, 2)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_text
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if len(user_text) < 30:
                        user_text += event.unicode

def show_scene(image, text, wait_for_key=True):
    screen.blit(pygame.transform.scale(image, (WIDTH, HEIGHT)), (0, 0))
    draw_text(text, 30, 400, screen)
    pygame.display.flip()
    if wait_for_key:
        wait()

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

def realm_woods():
    show_scene(
        scenes["woods"],
        "White Rabbit: 'Solve my riddle!\nI speak without a mouth and hear without ears.\nWhat am I?'",
        wait_for_key=False
    )
    answer = text_input("Your answer:")
    if "echo" in answer.lower():
        correct_sound.play()
        return True
    wrong_sound.play()
    return False

def realm_tea():
    show_scene(
        scenes["tea"],
        "Mad Hatter: 'Remember the order of cups! (simulated)\nPress any key to continue.'"
    )
    click_sound.play()
    return True

def realm_queen():
    show_scene(
        scenes["queen"],
        "Queen of Hearts: 'Guess my secret number (1-10). Three tries!'",
        wait_for_key=False
    )
    number = random.randint(1, 10)
    for attempt in range(3):
        try:
            guess = text_input(f"Try {attempt + 1}/3: Your guess:")
            if int(guess) == number:
                correct_sound.play()
                return True
        except:
            pass
    wrong_sound.play()
    return False

def realm_mirror():
    show_scene(
        scenes["mirror"],
        "Mirror Forest: 'Which Alice are you?'\nChoose: Brave, Clever, Kind",
        wait_for_key=False
    )
    choice = text_input("Your choice:")
    if choice.lower() in ["brave", "clever", "kind"]:
        correct_sound.play()
        return True
    wrong_sound.play()
    return False

def finale():
    show_scene(
        scenes["finale"],
        "You collected all 5 keys!\nA portal opens and Wonderland fades...\n\nTHE END"
    )
    click_sound.play()

def main_menu():
    menu_running = True
    while menu_running:
        screen.fill((0, 0, 0))
        draw_text("Alice: Lost in Wonderland", WIDTH // 3, HEIGHT // 4, screen, 48, WHITE)
        draw_text("Press Enter to Start", WIDTH // 3, HEIGHT // 2, screen, 32, WHITE)
        draw_text("Press ESC to Quit", WIDTH // 3, HEIGHT // 1.5, screen, 32, WHITE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    click_sound.play()
                    menu_running = False
                    main()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def main():
    show_scene(
        scenes["intro"],
        "You wake up in Wonderland.\nFind the 5 keys to return home."
    )
    keys = 0

    if realm_woods():
        keys += 1
        print("Key 1 obtained!")
    if realm_tea():
        keys += 1
        print("Key 2 obtained!")
    if realm_queen():
        keys += 1
        print("Key 3 obtained!")
    if realm_mirror():
        keys += 1
        print("Key 4 obtained!")

    final_answer = text_input("Final Riddle:\n'The more you take, the more you leave behind.'\nYour answer:")
    if "footstep" in final_answer.lower():
        keys += 1
        print("Key 5 obtained!")

    if keys == 5:
        finale()
    else:
        print("You failed to collect all keys. Try again.")
        pygame.quit()

if __name__ == "__main__":
    main_menu()

