import random

hard = "(4 x 6-8)"
medium = "(4 x 12)"
many = "(30, 20, 15, 10)"

upper_heavy = [
    (f'Жим штанги на верх груди {hard}', f'Жим штанги на верх груди {medium}'),
    (f'Жим гантелей на верх груди{hard}', f'Жим гантелей на верх груди {medium}'),
]

middle_heavy = [
    (f'Жим гантелей на середину груди {hard}', f'Жим гантелей на середину груди {medium}'),
    (f'Жим штанги на середину груди {hard}', f'Жим штанги на середину груди {medium}'),
    (f"Жим в Hammer {medium}", f"Жим в Hammer {many}"),
]

lower_heavy = [
    (f"Отжимания на брусьях {medium}", f"Отжимания на брусьях с отягощением {hard}"),
    (f"Отжимания с упором сзади {medium}", f"Отжимания с упором сзади {hard}")
    ]

upper_medium = [
    (f'Разводка с гантелями на верх груди {many}', f'Разводка с гантелями на верх груди {medium}'),
    (f'Butterfly {medium}', f'Butterfly {many}'),
    (f"Сведения на верх груди в crossover {medium}", f"Сведения на верх груди в crossover {many}"),
    ]

middle_medium = [
    (f"Разводка с гантелями на середину груди {medium}", f"Разводка с гантелями на середину груди {many}"),
    (f"Сведения на середину груди в crossover {medium}", f"Сведения на середину груди в crossover {many}"),
    (f"Жим Свенда {medium}", f"Жим Свенда {many}"),
]

lower_medium = [
    (f"Сведения на низ груди в crossover {many}", f"Сведения на низ груди в crossover {medium}"),
]


def generate():
    # collect
    result = []
    i = random.choice(upper_heavy)
    result.append(i[random.randint(0, len(i) - 1)])
    i = random.choice(middle_heavy)
    result.append(i[random.randint(0, len(i) - 1)])
    i = random.choice(lower_heavy)
    result.append(i[random.randint(0, len(i) - 1)])
    i = random.choice(upper_medium)
    result.append(i[random.randint(0, len(i) - 1)])
    for i in random.sample(middle_medium, 2):
        result.append(i[random.randint(0, len(i) - 1)])
    i = random.choice(lower_medium)
    result.append(i[random.randint(0, len(i) - 1)])
    return result
