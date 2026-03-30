"""
Utilītu bibliotēka darbam ar virkņu, skaitļu un sarakstu datiem.
"""

# -----------------------------
#   VIRKŅU FUNKCIJAS
# -----------------------------

def capitalize(text):
    """
    Pārveido pirmo burtu par lielo.

    Args:
        text (str): ievades virkne

    Returns:
        str: virkne ar lielo pirmo burtu

    Example:
        >>> capitalize("hello")
        'Hello'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        return ""
    return text[0].upper() + text[1:]


def truncate(text, max_len=20):
    """
    Apgriež tekstu līdz max_len un pievieno '...' ja nepieciešams.

    Args:
        text (str): ievades virkne
        max_len (int): maksimālais garums (noklusējums 20)

    Returns:
        str: apgriezta virkne

    Example:
        >>> truncate("Hello world!", 5)
        'He...'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if max_len < 3:
        raise ValueError("max_len must be at least 3")
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def count_words(text):
    """
    Saskaita vārdus tekstā.

    Args:
        text (str): ievades virkne

    Returns:
        int: vārdu skaits

    Example:
        >>> count_words("Hello world")
        2
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    words = text.split()
    return len(words)


# -----------------------------
#   SKAITĻU FUNKCIJAS
# -----------------------------

def clamp(num, low, high):
    """
    Ierobežo skaitli norādītajā diapazonā.

    Args:
        num (int/float): skaitlis
        low (int/float): minimālā robeža
        high (int/float): maksimālā robeža

    Returns:
        int/float: ierobežotā vērtība

    Example:
        >>> clamp(15, 0, 10)
        10
    """
    if low > high:
        raise ValueError("low cannot be greater than high")
    return max(low, min(num, high))


def is_prime(num):
    """
    Nosaka, vai skaitlis ir pirmskaitlis.

    Args:
        num (int): pārbaudāmais skaitlis

    Returns:
        bool: True, ja pirmskaitlis

    Example:
        >>> is_prime(7)
        True
    """
    if not isinstance(num, int):
        raise TypeError("num must be an integer")
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def factorial(n):
    """
    Aprēķina faktoriālu n! (n >= 0).

    Args:
        n (int): skaitlis

    Returns:
        int: n faktoriāls

    Example:
        >>> factorial(5)
        120
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# -----------------------------
#   SARAKSTU FUNKCIJAS
# -----------------------------

def total(numbers):
    """
    Aprēķina saraksta summu (bez sum()).

    Args:
        numbers (list): saraksts ar skaitļiem

    Returns:
        int/float: summa

    Example:
        >>> total([1, 2, 3])
        6
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")

    s = 0
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise TypeError("all elements must be numbers")
        s += n
    return s


def average(numbers):
    """
    Aprēķina saraksta vidējo vērtību.

    Args:
        numbers (list): saraksts ar skaitļiem

    Returns:
        float: vidējais aritmētiskais

    Example:
        >>> average([1, 2, 3])
        2.0
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if len(numbers) == 0:
        raise ValueError("numbers cannot be empty")

    return total(numbers) / len(numbers)


# -----------------------------
#   DEMONSTRĀCIJA
# -----------------------------

if __name__ == "__main__":
    print("Demonstrācija:")
    print(capitalize("hello"))
    print(truncate("Šis ir ļoti garš teikums, kas jāapgriež.", 15))
    print(count_words("Cik daudz vārdu ir šajā teikumā"))
    print(clamp(15, 0, 10))
    print(is_prime(29))
    print(factorial(6))
    print(total([1, 2, 3, 4]))
    print(average([10, 20, 30]))

