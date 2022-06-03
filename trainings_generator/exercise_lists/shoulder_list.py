import random

hard = "(4 x 6-8)"
medium = "(4 x 12)"
many = "(30, 20, 15, 10)"

heavy_mid = [
    (f"Армейский жим {hard}", f"Армейский жим {medium}"),
    (f"Жим гантелей сидя{medium}",),
    (f"Жим на середину в Hammer {hard}", f"Жим на середину в Hammer {medium}"),
]

medium_mid = [
    (f"Тяга штанги к подбородку {medium}", f"Тяга штанги к подбородку {many}"),
    (f"Разводки гантелей в стороны {medium}", f"Разводки гантелей в стороны {many}"),
    ]

heavy_front = [
    (f'Жим на передние дельты в Смитте {medium}', f'Жим на передние дельты в Смитте {many}'),
    (f"Подъем гантелей на передние дельты {medium}", f"Подъем гантелей на передние дельты {many}"),
    ]

medium_front = [
    (f"Тяга на передние дельты в crossover {many}", f"Тяга на передние дельты в crossover {medium}"),
]

combined = [
    (f"Жим Арнольда {medium}", f"Жим Арнольда {hard}"),
]

heavy_rear = [
    (f"Разведение гантелей на задние дельты {medium}",),
    (f"Butterfly на задние дельты {medium}", f"Butterfly на задние дельты {many}"),
    (f"Crossover на задние дельты {medium}", f"Crossover на задние дельты {many}"),
]


def generate():
    result = []

    i = random.choice(heavy_mid)
    result.append(i[random.randint(0, len(i) - 1)])
    i = random.choice(heavy_front)
    result.append(i[random.randint(0, len(i) - 1)])
    i = random.choice(combined)
    result.append(i[random.randint(0, len(i) - 1)])
    i = random.choice(heavy_rear)
    result.append(i[random.randint(0, len(i) - 1)])
    i = random.choice(medium_mid)
    result.append(i[random.randint(0, len(i) - 1)])
    i = random.choice(medium_front)
    result.append(i[random.randint(0, len(i) - 1)])

    return result
