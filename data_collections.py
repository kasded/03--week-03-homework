# --- A daļa: Saraksti ---

print("--- Saraksti ---")

# Izveido sarakstu ar 5+ skaitļiem
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pievieno elementu
numbers.append(11)

# Dzēš pēdējo elementu
numbers.pop()

# Aprēķina summu un vidējo ar for ciklu
total = 0
count = 0

for num in numbers:
    total += num
    count += 1

average = total / count

print(f"Summa: {total}, Vidējais: {average}")

# Filtrē tikai pāra skaitļus
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Pāra skaitļi: {even_numbers}")

# Šķēlumi (slice)
first_three = numbers[:3]
last_two = numbers[-2:]
every_second = numbers[::2]

print(f"Pirmie 3: {first_three}, Pēdējie 2: {last_two}")
print(f"Katrs otrais: {every_second}")


# --- B daļa: Vārdnīcas ---

print("\n--- Vārdnīcas ---")

students = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95
}

# Pievieno jaunu studentu
students["Mārtiņš"] = 88

# Maina esošu atzīmi
students["Jānis"] = 75

# Izvada visus studentus
for name, grade in students.items():
    print(f"{name}: {grade}")

# Atrod labāko studentu
best_name = None
best_grade = -1

for name, grade in students.items():
    if grade > best_grade:
        best_grade = grade
        best_name = name

print(f"Labākais students: {best_name} ({best_grade})")


# --- C daļa: Kombinācija ---

print("\n--- Studenti ar atzīmi >= 80 ---")

student_list = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 75},
    {"name": "Līga", "grade": 95},
    {"name": "Mārtiņš", "grade": 88}
]

# Filtrē tikai tos ar atzīmi >= 80
filtered = []
for s in student_list:
    if s["grade"] >= 80:
        filtered.append(s)

# Izvada ar enumerate()
for i, s in enumerate(filtered, start=1):
    print(f"{i}. {s['name']} — {s['grade']}")

