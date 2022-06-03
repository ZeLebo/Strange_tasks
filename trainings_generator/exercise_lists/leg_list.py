import random

warm_up = [
    "Гиперэстезия (4 x 12)",
]

squat = [
    ("Приседания (6 x 6-8)", "Приседания (5 x 12)"),
    ("Фронтальный присед (6 x 6-8)", "Фронтальный присед (5 x 12)"),
]

heavy_exercises = [
    ("Жим ногами 4 x 12", "Жим ногами 5 x 12"),
]

medium_exercises = [
    ("Выпады (5 х 12)", "Выпады (4 x 12)"),
]

required_exercises = [
    ("Разгибания ног (50, 30, 20, 15)", "Разгибания ног (30, 20, 15, 12)", "Разгибания ног (4 x 12)"),
    ("Сгибания ног (50, 30, 20, 15)", "Сгибания ног (30, 20, 15, 12)", "Сгибания ног (4 x 12)"),
]

optional_exercises = [
    ("Разведение ног (50, 30, 20, 15)", "Разведение ног (5 x 12)"),
    ("Сведение ног (50, 30, 20, 15)", "Сведение ног (5 x 12)"),
]

gastrocnemius = [
    ("Икроножные (4 x 12)", "Икроножные (50, 40, 30, 20)"),
]


def generate():
    result = [warm_up.pop()]
    i = random.choice(squat)
    result.append(i[random.randint(0, len(i) - 1)])
    i = random.choice(heavy_exercises)
    result.append(i[random.randint(0, len(i) - 1)]),
    i = random.choice(medium_exercises)
    result.append(i[random.randint(0, len(i) - 1)]),
    for i in required_exercises:
        result.append(i[random.randint(0, len(i) - 1)]),

    if random.randint(0, 1) == 0:
        for i in optional_exercises:
            result.append(i[random.randint(0, len(i) - 1)]),
    i = random.choice(gastrocnemius)
    result.append(i[random.randint(0, len(i) - 1)]),
    return result
