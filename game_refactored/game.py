import random
from utils import get_number_input
from messages import hint_too_low, hint_too_high, win_message, lose_message


def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("\nEs esmu izvēlējies skaitli no 1 līdz 100. Uzmini to!")
    print(f"Tev ir {max_attempts} mēģinājumi.")

    while True:
        guess = get_number_input("Tavs minējums: ")
        attempts += 1

        if guess == secret:
            win_message(attempts)
            break
        elif guess < secret:
            hint_too_low()
        else:
            hint_too_high()

        if attempts >= max_attempts:
            lose_message(secret)
            break
