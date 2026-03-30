"""
Vienkārša validācijas funkciju bibliotēka.
"""

import re


def is_email(text):
    """
    Pārbauda, vai virkne izskatās pēc e-pasta adreses.
    Vienkārša validācija: satur '@' un '.' pēc '@'.

    Args:
        text (str): pārbaudāmā virkne

    Returns:
        bool: True, ja izskatās pēc e-pasta

    Example:
        >>> is_email("anna@inbox.lv")
        True
    """
    if not isinstance(text, str):
        return False

    if "@" not in text:
        return False

    local, _, domain = text.partition("@")
    return "." in domain and len(local) > 0 and len(domain) > 0


def is_phone_number(text):
    """
    Pārbauda Latvijas telefona numuru formātā:
    +371 XXXXXXXX (kopā 12 simboli, no kuriem 8 ir cipari).

    Args:
        text (str): pārbaudāmā virkne

    Returns:
        bool: True, ja atbilst formātam

    Example:
        >>> is_phone_number("+371 26123456")
        True
    """
    if not isinstance(text, str):
        return False

    pattern = r"^\+371 ?\d{8}$"
    return re.match(pattern, text) is not None


def is_valid_age(age):
    """
    Pārbauda, vai vecums ir vesels skaitlis 0–150.

    Args:
        age (int/str): vecums

    Returns:
        bool: True, ja derīgs vecums

    Example:
        >>> is_valid_age(25)
        True
    """
    try:
        age = int(age)
    except (ValueError, TypeError):
        return False

    return 0 <= age <= 150


def is_strong_password(text):
    """
    Pārbauda, vai parole ir pietiekami stipra:
    - vismaz 8 simboli
    - satur burtus
    - satur ciparus

    Args:
        text (str): parole

    Returns:
        bool: True, ja parole ir stipra

    Example:
        >>> is_strong_password("abc12345")
        True
    """
    if not isinstance(text, str):
        return False

    if len(text) < 8:
        return False

    has_letter = any(ch.isalpha() for ch in text)
    has_digit = any(ch.isdigit() for ch in text)

    return has_letter and has_digit


def is_valid_date(text):
    """
    Pārbauda datuma formātu YYYY-MM-DD.
    Pamata validācija (nepārbauda mēnešu dienu skaitu).

    Args:
        text (str): datums

    Returns:
        bool: True, ja atbilst formātam

    Example:
        >>> is_valid_date("2024-12-31")
        True
    """
    if not isinstance(text, str):
        return False

    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, text):
        return False

    year, month, day = text.split("-")

    try:
        y = int(year)
        m = int(month)
        d = int(day)
    except ValueError:
        return False

    return 1 <= m <= 12 and 1 <= d <= 31


# ---------------------------------------------------------
#   TESTI
# ---------------------------------------------------------

if __name__ == "__main__":
    print("=== Testi: is_email ===")
    print(is_email("anna@inbox.lv"))
    print(is_email("anna"))
    print(is_email("anna@"))
    print(is_email("@inbox.lv"))

    print("\n=== Testi: is_phone_number ===")
    print(is_phone_number("+371 26123456"))
    print(is_phone_number("+37126123456"))
    print(is_phone_number("26123456"))
    print(is_phone_number("+371 1234567"))  # par maz ciparu

    print("\n=== Testi: is_valid_age ===")
    print(is_valid_age(25))
    print(is_valid_age("150"))
    print(is_valid_age(-1))
    print(is_valid_age("abc"))

    print("\n=== Testi: is_strong_password ===")
    print(is_strong_password("abc12345"))
    print(is_strong_password("abcdefg"))   # nav ciparu
    print(is_strong_password("12345678"))  # nav burtu
    print(is_strong_password("a1b2c3"))    # par īsu

    print("\n=== Testi: is_valid_date ===")
    print(is_valid_date("2024-12-31"))
    print(is_valid_date("2024-02-30"))
    print(is_valid_date("24-12-31"))
    print(is_valid_date("2024/12/31"))

