from game import play_game
from messages import ask_play_again, goodbye


def main():
    print("Sveiks minēšanas spēlē!")

    while True:
        play_game()

        if not ask_play_again():
            goodbye()
            break


if __name__ == "__main__":
    main()

