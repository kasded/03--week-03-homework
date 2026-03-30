def get_number_input(prompt: str) -> int:
    """Droši nolasa skaitli no input()."""
    while True:
        value = input(prompt)

        if not value.isdigit():
            print("Kļūda: jāievada skaitlis!")
            continue

        return int(value)
