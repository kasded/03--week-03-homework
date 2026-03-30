def hint_too_low():
    print("Par mazu!")


def hint_too_high():
    print("Par lielu!")


def win_message(attempts):
    print(f"Pareizi! Tu uzminēji ar {attempts} mēģinājumiem.")


def lose_message(secret):
    print(f"\nMēģinājumi beigušies! Pareizā atbilde bija {secret}.")


def ask_play_again() -> bool:
    ans = input("\nVai vēlies spēlēt vēlreiz? (j/n): ").lower()
    return ans == "j"


def goodbye():
    print("Paldies par spēli!")

